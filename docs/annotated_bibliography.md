# Annotated Bibliography

## 1. Ramsauer, Hubert, et al. (2020). "Hopfield Networks is All You Need."

- Type: arXiv preprint
- Relevance: Core mathematical foundation for the PDF's associative-memory interpretation of retrieval and attention.
- Note: This paper establishes a modern Hopfield network with continuous states and shows its equivalence to scaled dot-product attention. It is the most direct paper supporting the claim that transformer-like retrieval behaves like associative memory with attractor basins.

## 2. Koulischer, Felix, et al. (2023). "Exploring the Temperature-Dependent Phase Transition in Modern Hopfield Networks."

- Type: arXiv preprint
- Relevance: Supports the inverse-temperature logic in the PDF.
- Note: This work shows how the energy landscape changes with temperature or inverse temperature, producing a transition from broad averaging basins to sharper pattern-specific minima. This is central to the PDF's explanation of why probing can navigate a field at all.

## 3. Covington, Paul, Jay Adams, and Emre Sargin (2016). "Deep Neural Networks for YouTube Recommendations."

- Type: ACM conference paper
- Relevance: Illustrates real-world recommendation systems as latent embedding systems rather than catalog lookup systems.
- Note: The paper provides a concrete example of candidate generation and ranking via latent embeddings. It supports the conceptual framing that recommender systems organize behavior in geometry, not just in discrete item tables.

## 4. Huang, Po-Sen, et al. (2013). "Learning Deep Structured Semantic Models for Web Search Using Clickthrough Data."

- Type: ACM conference paper
- Relevance: Shows the use of latent semantic matching in search and retrieval.
- Note: DSSM-style models embed queries and documents into a shared semantic space. They are important background to the claim that retrieval systems can cluster or move users and items along a shared latent landscape.

## 5. van den Oord, Aaron, Yazhe Li, and Oriol Vinyals (2018). "Representation Learning with Contrastive Predictive Coding."

- Type: arXiv preprint
- Relevance: The canonical reference for InfoNCE and contrastive representation learning.
- Note: InfoNCE trains a model to assign high similarity to matched pairs while pushing non-matching distractors apart. In retrieval systems, this objective is exactly the mechanism that forms structured embedding geometry: nearby points correspond to semantically similar items, while unrelated items remain separated. It provides a direct mathematical basis for the thesis that a latent field can be navigated through semantically adjacent probes.

## 6. Li, S., et al. (2024). "On Effects of Steering Latent Representation for Large Language Model Unlearning."

- Type: arXiv preprint
- Relevance: Direct support for the PDF's discussion of representation steering and concept persistence.
- Note: This work analyzes RMU-style representation steering in LLMs and shows that steering latent representations can substantially reshape behavior while leaving latent structure recoverable. It supports the idea that semantic structure persists in a learned field and can be navigated through controlled interventions.

## 7. Farrell, Eoin, et al. (2024). "Applying sparse autoencoders to unlearn knowledge in language models."

- Type: arXiv preprint
- Relevance: Alternative approach to representational steering and concept shaping.
- Note: This paper examines whether sparse autoencoders can remove knowledge while minimizing side effects. It strengthens the broader point that semantic content is organized across distributed latent structure rather than localized in a single feature or state.

## 8. Yang, J.; Boyden, E. S.; So, P. T. (MIT-related photonic computing research)

- Type: Research article / technical report context
- Relevance: Physical analogue used in the PDF for sculpted attractor landscapes.
- Note: The physical concept is the creation of a refractive-index landscape with nanoscale precision such that light propagates through a sculpted field to a stable focus. It is a useful analogy for the idea of basins and attractors and helps frame the landscape metaphor in concrete physical terms.

## 8. Real-world platform and retrieval literature

- Type: Contextual literature in recommendation, ranking, and information retrieval
- Relevance: Underpins the project's treatment of retrieval as a latent geometry problem.
- Note: Across retrieval and recommendation research, the dominant picture is that users, queries, and documents are embedded in a shared semantic space and ranked by similarity. This is the core conceptual support for the idea that information landscapes are navigable by semantically adjacent probes.

## Overall assessment

The bibliography strongly supports the main conceptual logic of the project: retrieval systems are latent-geometry systems, attractor basins are a plausible mechanism, semantic structure is distributed rather than isolated, and physical analogies show that sculpted landscapes can yield stable navigation paths. Taken together, these sources provide a compelling foundation for the original concept and help situate it within a broader research tradition.
