# Information Landscape Sculpting: Research Proposal

## Working title

Information Landscape Sculpting: Reconstructing Latent Epistemic Fields with Ensemble Associative Probing

## Motivation

The source PDF argues that modern retrieval systems behave like continuous associative memories: users and items are embedded into a shared geometry, and low-entropy probing can push a synthetic agent toward a local attractor associated with a cohort. The central empirical question is not whether such retrieval systems literally reveal hidden secrets, but whether they can recover the adjacency structure and read-front of a specialized field more effectively than lexical search alone.

This is an interesting and important project because it sits at the boundary between:

- representation learning and modern retrieval,
- associative memory and attention,
- unlearning and representational erasure,
- platform auditing and privacy risk,
- and the ethics of automated probing in commercial recommendation pipelines.

## Research question

Primary question:

Does a heterogeneous ensemble of synthetic personas, when driven by adjacent low-entropy terms, recover more of a specialized field's frontier concepts than a lexical baseline?

Secondary questions:

1. How much of the signal comes from the platform's lookalike geometry versus the starting vocabulary?
2. How sensitive is the recovery to popularity bias and cohort drift?
3. Does the method outperform lexical search primarily on hidden or out-of-index frontier terms?
4. How should the project be framed ethically and operationally to avoid individual targeting or policy violations?

## Hypothesis

If a recommender is effectively organizing users and documents into a smooth but basin-structured latent field, then low-entropy, semantically adjacent probe trajectories from multiple heterogeneous personas should recover more of the field adjacency graph than a comparable lexical approach. The effect should be strongest for near-frontier terms that are not yet widely indexed or surfaced by generic search.

## Falsifiable design

The project adopts the PDF's strongest version of the claim as a falsifiable thesis:

- Construct a synthetic field graph with known frontier concepts.
- Seed personas with adjacent but non-explicit terms.
- Run a popularity-biased recommender and ensemble probing simulation.
- Compare recovered frontier concept set against a lexical baseline.
- Evaluate precision, recall, and recovery of held-out concept terms.
- Treat a null result as valid evidence.

This reframing is essential: the method is only useful if it improves frontier recovery beyond lexical retrieval, and only on domains where links exist in the recommender's observational surface.

## Methodology

### 1. Data generation

Build a synthetic concept graph with:

- core concepts,
- adjacent technical terms,
- popularity weights,
- a hidden frontier set intentionally not captured by the seed vocabulary.

This simulates a niche research field with a latent frontier whose terms are not directly present in the initialization.

### 2. Persona design

Create several personas with distinct anchor vocabularies but shared domain adjacency. Each persona is intentionally semantically narrow and non-explicit. The ensemble is used to suppress idiosyncratic noise and recover the shared cohort shape.

### 3. Retrieval model

Use a biased recommender that:

- increases scores for strong local adjacency,
- biases toward popular concepts,
- adds noise and instability.

This captures the popularity bias described in the PDF and allows a direct test of whether the ensemble can still recover hidden structures.

### 4. Evaluation

The project measures:

- precision among recovered frontier concepts,
- recall across the true frontier set,
- delta relative to lexical search baseline,
- robustness over repeated trials with different seeds.

A meaningful result requires the ensemble to beat a lexical baseline on out-of-index frontier terms.

## Expected contributions

1. A reproducible, open research scaffold for studying latent field reconstruction.
2. A synthetic evaluation environment that exposes the assumptions behind the claim.
3. A clear separation between a narrow and defensible claim (field reconstruction) and a much stronger but unsupported one (individual targeting or exfiltration).
4. A research artifact that can be used for safe critical analysis rather than direct operational deployment.

## Risks and limitations

This is a simulation project. It does not claim to demonstrate real-world extraction from a commercial platform. The main uncertainties are:

- output signal-to-noise in recommendation feeds,
- popularity bias flattening the landscape,
- simulator bias from synthetic personas,
- the gap between a cohort-level field and a named individual or institution,
- policy and consent boundaries in real-world platform studies.

## Ethics and compliance

The project stays within a synthetic and aggregate setting. It intentionally avoids:

- live scraping,
- personal targeting,
- biometric or demographic inference,
- bypassing terms of service,
- or experimentation on identifiable people.

Any future platform study would require explicit review, consent, and authorization, and would need to address legal and privacy implications as a first-class requirement.

## Deliverables

- research proposal,
- literature review,
- annotated bibliography,
- reproducible simulator,
- evaluation harness,
- final report and discussion of claims and failure modes.
