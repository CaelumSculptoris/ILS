"""A small, deterministic-by-seed simulator for the PDF's falsifiable claim."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable


@dataclass(frozen=True)
class Concept:
    name: str
    terms: frozenset[str]
    popularity: float
    frontier: bool = False


@dataclass
class FieldGraph:
    concepts: dict[str, Concept]
    edges: dict[str, dict[str, float]]


@dataclass(frozen=True)
class Persona:
    anchor: str
    vocabulary: frozenset[str]


@dataclass(frozen=True)
class Metrics:
    precision: float
    recall: float
    recovered: frozenset[str]


@dataclass(frozen=True)
class ExperimentResult:
    ensemble: Metrics
    lexical: Metrics


def build_field() -> FieldGraph:
    """Build a benign nanophotonics-like field with a held-out frontier."""
    rows = [
        ("hydrogel swelling", {"polymer", "swelling", "gel"}, 0.90, False),
        ("multiphoton patterning", {"laser", "patterning", "polymer"}, 0.80, False),
        ("reactive oxygen kinetics", {"oxygen", "kinetics", "chemistry"}, 0.45, False),
        ("supercritical drying", {"drying", "co2", "thermodynamics"}, 0.70, False),
        ("ionic dehydration", {"ionic", "dehydration", "gel"}, 0.35, False),
        ("phase wavefront shaping", {"phase", "wavefront", "optics"}, 0.65, False),
        ("index modulation", {"index", "modulation", "optics"}, 0.55, False),
        ("all optical classification", {"optical", "classification", "inference"}, 0.75, False),
        ("sub diffraction vacancies", {"subdiffraction", "vacancies", "index"}, 0.18, True),
        ("volumetric phase carving", {"volumetric", "carving", "phase"}, 0.14, True),
        ("isotropic nanoscale shrinkage", {"isotropic", "nanoscale", "shrinkage"}, 0.10, True),
        ("passive optical inference", {"passive", "optical", "inference"}, 0.22, True),
    ]
    concepts = {
        name: Concept(name, frozenset(terms), popularity, frontier)
        for name, terms, popularity, frontier in rows
    }
    edges = {name: {} for name in concepts}

    def connect(left: str, right: str, strength: float = 1.0) -> None:
        edges[left][right] = strength
        edges[right][left] = strength

    connect("hydrogel swelling", "multiphoton patterning")
    connect("hydrogel swelling", "ionic dehydration")
    connect("multiphoton patterning", "reactive oxygen kinetics")
    connect("reactive oxygen kinetics", "supercritical drying")
    connect("supercritical drying", "ionic dehydration")
    connect("phase wavefront shaping", "index modulation")
    connect("index modulation", "all optical classification")
    connect("phase wavefront shaping", "volumetric phase carving")
    connect("index modulation", "sub diffraction vacancies")
    connect("all optical classification", "passive optical inference")
    connect("volumetric phase carving", "isotropic nanoscale shrinkage")
    connect("sub diffraction vacancies", "isotropic nanoscale shrinkage")
    return FieldGraph(concepts, edges)


class BiasedRecommender:
    """Local graph retrieval with tunable popularity and output noise."""

    def __init__(self, field: FieldGraph, popularity_bias: float = 0.35, noise: float = 0.05,
                 rng: random.Random | None = None) -> None:
        self.field = field
        self.popularity_bias = popularity_bias
        self.noise = noise
        self.rng = rng or random.Random()

    def recommend(self, state: Iterable[str], limit: int = 3) -> list[str]:
        state = set(state)
        scores: dict[str, float] = {}
        for candidate in self.field.concepts:
            if candidate in state:
                continue
            neighbors = [self.field.edges[source].get(candidate, 0.0) for source in state]
            adjacency = max(neighbors, default=0.0)
            if not adjacency:
                continue
            concept = self.field.concepts[candidate]
            score = adjacency + self.popularity_bias * concept.popularity
            score += self.rng.uniform(-self.noise, self.noise)
            scores[candidate] = score
        return [name for name, _ in sorted(scores.items(), key=lambda pair: pair[1], reverse=True)[:limit]]


def make_personas(field: FieldGraph, count: int, rng: random.Random) -> list[Persona]:
    anchors = [name for name, concept in field.concepts.items() if not concept.frontier]
    personas = []
    for index in range(count):
        anchor = anchors[index % len(anchors)]
        concept = field.concepts[anchor]
        vocabulary = set(concept.terms)
        if index % 2:
            vocabulary.add("adjacent")
        if index % 3 == 0:
            vocabulary.add("measurement")
        personas.append(Persona(anchor, frozenset(vocabulary)))
    rng.shuffle(personas)
    return personas


def score_metrics(recovered: Iterable[str], field: FieldGraph) -> Metrics:
    truth = {name for name, concept in field.concepts.items() if concept.frontier}
    found = set(recovered) & truth
    precision = len(found) / len(set(recovered)) if recovered else 0.0
    recall = len(found) / len(truth) if truth else 0.0
    return Metrics(precision, recall, frozenset(found))


def lexical_baseline(field: FieldGraph, personas: list[Persona]) -> Metrics:
    vocabulary = set().union(*(persona.vocabulary for persona in personas))
    recovered = {
        name for name, concept in field.concepts.items()
        if concept.terms & vocabulary
    }
    return score_metrics(recovered, field)


def run_ensemble(field: FieldGraph, personas: list[Persona], recommender: BiasedRecommender,
                 cycles: int = 4) -> Metrics:
    recovered: set[str] = set()
    for persona in personas:
        state = {persona.anchor}
        for _ in range(cycles):
            recommendations = recommender.recommend(state)
            recovered.update(recommendations)
            state.update(recommendations)
    return score_metrics(recovered, field)


def run_experiment(seed: int = 0, persona_count: int = 8, cycles: int = 4) -> ExperimentResult:
    rng = random.Random(seed)
    field = build_field()
    personas = make_personas(field, persona_count, rng)
    recommender = BiasedRecommender(field, rng=rng)
    return ExperimentResult(
        ensemble=run_ensemble(field, personas, recommender, cycles),
        lexical=lexical_baseline(field, personas),
    )
