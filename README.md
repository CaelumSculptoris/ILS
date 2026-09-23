# Information Landscape Sculpting Research Project

This project operationalizes the PDF thesis as a **safe, falsifiable offline
experiment**. It tests whether a heterogeneous ensemble of synthetic personas
can recover the hidden frontier of a specialized field from a popularity-biased
recommender, and compares that result with a lexical-search baseline.

It does **not** automate real accounts, target identifiable people, bypass
content controls, or contact commercial platforms. The simulator is the
research instrument; any future human-subject or platform study would require
review, consent, and authorization.

## Research question

Given a known synthetic field graph and a set of adjacent seed terms, does
ensemble probing recover more frontier concepts than lexical search?

The primary outcome is frontier precision/recall. A result is meaningful only
if it is reproducible across seeds and beats the lexical baseline on
out-of-index frontier terms. A null result is a valid result.

## Quick start

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m ils_simulator.cli --trials 30 --seed 7
```

## Model

- `FieldGraph`: synthetic concepts, semantic edges, popularity, and a held-out
  frontier.
- `BiasedRecommender`: scores adjacent concepts while favoring popularity.
- `Persona`: heterogeneous anchor and seed-term views of the same field.
- `run_ensemble`: iteratively probes each persona and intersects noisy results.
- `lexical_baseline`: retrieves only concepts matching the initial vocabulary.

The simulator deliberately exposes the assumptions identified in the PDF:
popularity bias, incomplete forward projection, simulator noise, and low
output signal-to-noise. It is not evidence that real recommender systems have
the required resolution.

## What the script showed

The initial simulator did not claim a real-world result. It showed that, in a
synthetic field with a held-out frontier and popularity-biased retrieval, the
ensemble method can recover more frontier concepts than a lexical baseline. In
our representative run:

- Ensemble: precision 0.333, recall 1.000
- Lexical baseline: precision 0.273, recall 0.750

This matters because the point of the simulation is not to prove the real-world
thesis; it is to make the core claim falsifiable. If a method cannot beat a
lexical baseline under these conditions, then the stronger claim is likely not
supported.

## Research package

- [docs/research_proposal.md](/Users/cal/Projects/ILS/docs/research_proposal.md)
- [docs/literature_review.md](/Users/cal/Projects/ILS/docs/literature_review.md)
- [docs/final_research_report.md](/Users/cal/Projects/ILS/docs/final_research_report.md)
- [docs/annotated_bibliography.md](/Users/cal/Projects/ILS/docs/annotated_bibliography.md)
- [docs/sources.bib](/Users/cal/Projects/ILS/docs/sources.bib)

## Responsible-use boundary

Use aggregate synthetic fields only. Do not use this scaffold to infer a
named person’s behavior, nationality, employer, or affiliations; to evade
terms of service or access controls; or to collect private data.
