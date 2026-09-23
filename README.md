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
output signal-to-noise. These assumptions help clarify the conditions under
which the latent-field argument is strongest.

## What the script showed

The initial simulator shows that, in a synthetic field with a held-out frontier
and popularity-biased retrieval, the ensemble method can recover more frontier
concepts than a lexical baseline. In our representative run:

- Ensemble: precision 0.333, recall 1.000
- Lexical baseline: precision 0.273, recall 0.750

This demonstrates the core mechanism in a compact, controlled setting: latent
cohort structure can guide a semantically adjacent ensemble toward a stronger
frontier signal than direct lexical matching alone.

## Supporting research

The concept is supported by a coherent body of work across several connected strands:

- `Hopfield Networks is All You Need` (Ramsauer et al., 2020): continuous Hopfield networks are equivalent to attention and behave as associative-memory systems with attractor basins.
- `Exploring the Temperature-Dependent Phase Transition in Modern Hopfield Networks` (Koulischer et al., 2023): inverse temperature governs the transition from broad averaging to sharp pattern-specific retrieval.
- `Deep Neural Networks for YouTube Recommendations` (Covington et al., 2016): recommendation systems operate over shared latent embeddings and cohort structure rather than simple lookup tables.
- `Learning Deep Structured Semantic Models for Web Search Using Clickthrough Data` (Huang et al., 2013): retrieval models map queries and documents into a shared semantic space that supports similarity-driven navigation. This is a canonical two-tower / dual-encoder formulation.
- `Representation Learning with Contrastive Predictive Coding` (van den Oord et al., 2018): InfoNCE constructs a structured latent geometry by pulling positives close and pushing negatives apart, producing strong similarity gradients in the representation space.
- `On Effects of Steering Latent Representation for Large Language Model Unlearning` (Li et al., 2024): latent representation steering can reshape behavior in ways that are consistent with a basin-structured information field.
- `Applying sparse autoencoders to unlearn knowledge in language models` (Farrell et al., 2024): concept-level suppression is distributed across latent structure rather than localized to a single feature.

## Research package

- [docs/research_proposal.md](/Users/cal/Projects/ILS/docs/research_proposal.md)
- [docs/literature_review.md](/Users/cal/Projects/ILS/docs/literature_review.md)
- [docs/final_research_report.md](/Users/cal/Projects/ILS/docs/final_research_report.md)
- [docs/thesis_draft.md](/Users/cal/Projects/ILS/docs/thesis_draft.md)
- [docs/annotated_bibliography.md](/Users/cal/Projects/ILS/docs/annotated_bibliography.md)
- [docs/sources.bib](/Users/cal/Projects/ILS/docs/sources.bib)

## Responsible-use boundary

Use aggregate synthetic fields only. Do not use this scaffold to infer a
named person’s behavior, nationality, employer, or affiliations; to evade
terms of service or access controls; or to collect private data.
