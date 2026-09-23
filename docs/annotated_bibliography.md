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

## 5. Li, S., et al. (2024). "On Effects of Steering Latent Representation for Large Language Model Unlearning."

- Type: arXiv preprint
- Relevance: Direct support for the PDF's discussion of representational erasure being incomplete.
- Note: This work analyzes RMU-style representation steering in LLMs and shows that steering latent representations can suppress behavior without fully removing the underlying representation. It supports the project's caution that erasure does not imply conceptual disappearance.

## 6. Farrell, Eoin, et al. (2024). "Applying sparse autoencoders to unlearn knowledge in language models."

- Type: arXiv preprint
- Relevance: Alternative approach to representational steering and concept suppression.
- Note: This paper examines whether sparse autoencoders can remove knowledge while minimizing side effects. It strengthens the broader point that unlearning is partial, not exact, and that the underlying semantic direction can survive superficial deletion.

## 7. Yang, J.; Boyden, E. S.; So, P. T. (MIT-related photonic computing research)

- Type: Research article / technical report context
- Relevance: Physical analogue used in the PDF for sculpted attractor landscapes.
- Note: The physical concept is the creation of a refractive-index landscape with nanoscale precision such that light propagates through a sculpted field to a stable focus. It is a useful analogy for the idea of basins and attractors, even though it does not prove recommender extraction works.

## 8. Huh, A., and colleagues (on related representation geometry and token dynamics)

- Type: Literature context, not a single canonical paper
- Relevance: General support for distributed, low-rank route structure in language models.
- Note: This literature is relevant to the PDF's insistence that concepts are often distributed across layers and residual streams rather than localized in one clean dimension. It supports the caution that “removing a single feature” is often insufficient to erase a concept.

## 9. Real-world platform auditing and privacy literature

- Type: Contextual literature in privacy, platform measurement, and auditing
- Relevance: Underpins the ethical and policy sections of the project.
- Note: Research on personalized recommendation, inference risk, and privacy shows why aggregate field reconstruction must remain distinct from identifiable individual targeting. This is a key boundary in the project and in the PDF.

## Overall assessment

The bibliography supports the main conceptual logic of the project: retrieval systems are latent-geometry systems, attractor basins are a plausible mechanism, representational erasure is incomplete, and physical analogies show that sculpted landscapes can yield stable low-entropy outputs. What remains unsupported is the stronger operational claim that a black-box recommender can be probed to recover a field frontier better than lexical search in the wild.

That is why the research project is careful to maintain a synthetic, falsifiable framing. The literature supports the structure, not the operational leap.
