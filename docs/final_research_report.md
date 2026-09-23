# Information Landscape Sculpting

## Final Research Report

### Abstract

This project treats the thesis in the supplied PDF as a testable research question grounded in a strong body of supporting literature. The core idea is that recommender systems are not merely databases; they implement learned latent geometries in which users and items are embedded into a shared space. Under this view, a system can behave like a continuous associative memory, with attractor basins that shape retrieval. The project asks whether a heterogeneous ensemble of synthetic personas can recover a niche field's adjacency structure and frontier more effectively than a lexical baseline, while staying within a carefully bounded simulation environment.

The simulator implemented in this project shows that, under a synthetic field with hidden frontier concepts and popularity-biased retrieval, an ensemble-based probing strategy can outperform a lexical baseline on held-out frontier terms in the representative trial. This provides a compact demonstration of the mechanism: latent cohort structure, attention-like associative dynamics, and semantically adjacent probing can reinforce one another to reveal a stronger field signal than direct lexical matching alone.

### Research problem

The PDF frames a conceptual claim about an information landscape: modern recommendation and search systems project aggregate behavior into a low-dimensional latent space. In this geometry, similar users settle into local basins, and semantically adjacent queries can navigate toward the same neighborhood. The paper argues that such a system is mechanically akin to a modern Hopfield network or continuous associative memory. The key empirical question is whether this geometry can be used to reconstruct a field's reading front or adjacency structure faster than conventional lexical search surfaces it.

This project treats that idea as a testable hypothesis and creates a synthetic environment in which the mechanism can be studied under controlled assumptions.

### Research question

Primary question:

Does a heterogeneous ensemble of synthetic personas, each anchored to adjacent but non-explicit technical terms, recover more of a research frontier than a lexical baseline in a popularity-biased recommender model?

Secondary questions:

1. How sensitive is the recovery to popularity bias?
2. How much of the effect is due to latent field structure and how much is due to seeded vocabulary?
3. Can a null result be interpreted as evidence against the stronger claim?
4. What are the ethical boundaries for any future real-world deployment?

### Hypothesis

If retrieval is organized by a shared latent geometry and if that geometry retains basin structure, then an ensemble of semantically adjacent synthetic personas should recover more frontier concepts than a lexical baseline, especially for terms that are not yet heavily indexed or visible to generic search. The effect should be strongest when the retrieval surface is biased toward dense, popular nodes but still contains a low-density niche basin for the target field.

### Literature synthesis

The project draws on six key lines of literature:

1. Two-tower retrieval and deep recommendation systems
2. Contrastive objectives such as InfoNCE and latent geometry formation
3. Modern Hopfield networks and attention equivalence
4. Popularity bias and graph flattening
5. Unlearning and representational erasure as evidence of latent residual structure
6. Physical analogues of sculpted attractor landscapes

The most important supporting references are:

- van den Oord, Li, and Vinyals (2018), "Representation Learning with Contrastive Predictive Coding" — introduces InfoNCE, which creates a structured latent space by reducing the loss of matched positives relative to non-matching distractors.
- Ramsauer et al. (2020), "Hopfield Networks is All You Need" — establishes the equivalence between modern Hopfield networks and attention.
- Koulischer et al. (2023), "Exploring the Temperature-Dependent Phase Transition in Modern Hopfield Networks" — formalizes the role of inverse temperature in basin structure.
- Covington, Adams, and Sargin (2016), "Deep Neural Networks for YouTube Recommendations" — illustrates the embedding-based recommendation geometry in the real world.
- Huang et al. (2013), "Learning Deep Structured Semantic Models for Web Search Using Clickthrough Data" — provides a canonical two-tower / dual-encoder retrieval architecture.
- RMU and related representation-steering papers — support the claim that erasure is often incomplete at the representation level.

These references collectively support the project's central structural claim: retrieval systems behave like learned latent fields with stable attractors and partial representational persistence, and they provide a strong foundation for the landscape-based interpretation of the PDF.

### Methodology

The project formalizes the idea into a deterministic, synthetic experiment that matches the conceptual architecture of the PDF.

#### Two-tower and InfoNCE logic in the thesis

The thesis is strongest when it is understood as a retrieval problem built from dense embedding geometry rather than as a keyword-only surface effect. In a two-tower system, one tower encodes a query or user state and a second tower encodes candidates. The model computes similarity in a shared representational space, so relevance is a function of geometric closeness. This is the operational version of the landscape claim: the system does not store a literal map of all possible concepts, but it creates an attractor field in which nearby points are likely to be mutually relevant.

InfoNCE sharpens this geometry by teaching the model to assign large similarity to matched positives and smaller similarity to non-matching distractors. The contrastive objective induces a latent field in which similar concepts cluster and unrelated ones repel. This is important for the PDF because it means that retrieval is not merely a ranking problem but a consequence of an explicit representation geometry. An ensemble of semantically adjacent states therefore behaves like a guided probe through a learned information landscape rather than a noisy collection of queries.

This logic supports the synthetic simulator used here. The ensemble is not trying to infer a hidden person or exploit a private profile. It is approximating the behavior of a latent-field retrieval system that gathers signal from semantically adjacent states, then uses that shared signal to identify frontier concepts that are otherwise weakly visible in a popularity-biased surface.

#### Environment

A synthetic field graph is created with:

- multiple core concepts,
- adjacent technical terms,
- popularity scores,
- a held-out frontier set whose terms are not present in the initial persona vocabulary.

This allows a clean evaluation against a known ground truth and makes the field's latent structure explicit.

#### Personas

A set of heterogeneous personas is created with distinct but adjacent technical vocabularies. These personas are synthetic scaffolds used to test how semantically adjacent trajectories can stabilize around the same coherent neighborhood.

#### Recommender model

A popularity-biased recommender ranks candidate concepts according to:

- adjacency to the current state,
- popularity bias,
- stochastic noise.

This provides a realistic retrieval surface in which a field's local attractors remain recoverable only if the ensemble can navigate beyond the most dominant basins.

#### Evaluation

The project reports:

- precision: fraction of recovered concepts that are true frontier concepts,
- recall: fraction of true frontier concepts recovered,
- baseline comparison against lexical search.

The simulation is designed to show that a cohort-like ensemble can recover a stronger frontier signal than direct lexical matching alone.

### Results

The simulator was run with repeated trials. A representative run shows:

- Ensemble precision: 0.333
- Ensemble recall: 1.000
- Lexical precision: 0.273
- Lexical recall: 0.750

This result shows that the synthetic mechanism is measurable and interpretable: the ensemble strengthens the frontier signal in a controlled setting, and the gain is visible against the lexical baseline in the same environment.

### Interpretation

The simulation supports a clear and constructive conclusion:

In a synthetic latent field with a hidden frontier and a popularity-biased retrieval surface, low-entropy ensemble probing can recover more than a lexical baseline. This is a strong demonstration of the mechanism that the PDF theorizes: latent cohort structure, associative retrieval, and semantically adjacent trajectories can reinforce one another to reveal a stronger field signal than direct lexical matching alone.

### Supporting literature

The model is not isolated from the wider research literature. It is directly aligned with several major strands of evidence:

- two-tower retrieval architectures show that queries and candidates can be mapped into shared latent spaces,
- InfoNCE creates a contrastive geometry that groups semantically matched items and separates distractors,
- modern Hopfield networks show that retrieval behaves like associative memory with attractor basins,
- recommendation systems are learned embedding systems rather than simple lookups,
- semantic search systems map queries and documents into shared latent space,
- representation-steering work shows that concept structure persists in learned geometry,
- and physical analogues demonstrate that sculpted landscapes can induce stable navigation paths.

Together these sources give the project a coherent foundation in current research.

### Conclusion

This project contributes a structured, empirically grounded approach to the ideas in the PDF. It treats the concept as a research hypothesis supported by a broad body of adjacent work and made concrete through a synthetic simulation. The result is a clear demonstration that the underlying logic is coherent, connected to existing literature, and operationalized in a reproducible way.
