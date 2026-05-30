# Semantic Retrieval for arXiv Papers

Dense retrieval system for scientific-paper search over arXiv metadata. The goal is to retrieve the correct paper for natural-language research questions using semantic embeddings instead of exact keyword matching.

## Objective

Build a reproducible semantic-search pipeline for scientific-paper retrieval and evaluate whether dense embeddings recover the target paper in the top five results.

## Architecture

- Text encoder: `BAAI/bge-large-en-v1.5`.
- Document representation: title and abstract combined into a dense embedding.
- Index: FAISS inner-product index over normalized vectors.
- Cache: optional on-disk document embedding cache to avoid recomputing the corpus representation.

## Data

The experiment uses an arXiv metadata subset with `id`, `title`, and `abstract` fields plus a 1,000-query evaluation file. Source metadata and embedding caches are excluded from version control.

## Method

- Validated a 98k-document arXiv metadata corpus and 1,000 query evaluation set.
- Cleaned titles, abstracts, and queries.
- Embedded documents and queries with the same sentence-transformer model.
- Used normalized embeddings so FAISS inner product corresponds to cosine similarity.
- Measured both retrieval quality and search latency.

## Evaluation

Metrics are computed on the held-out query set with one known relevant paper per query. The notebook reports MRR@5, HitRate@5, hit/miss counts, and basic latency profiling.

## Results

| Metric | Value |
|:--|--:|
| Documents | 98,213 |
| Evaluation queries | 1,000 |
| Embedding dimension | 1,024 |
| MRR@5 | 0.9164 |
| HitRate@5 | 0.9650 |
| Hits@5 | 965 |

## Limitations

- Evaluation assumes one target paper per query even when several papers may be semantically relevant.
- Dense retrieval can miss exact identifier-like matches or very narrow technical wording.
- No cross-encoder reranking is included.
- The full metadata file and embedding cache are not committed.

## How to Reproduce

Place `arxiv-metadata-s.json` and `test_sample.csv` next to the notebook or in `nlp_s3_project/`, install the root requirements, and run `project.ipynb`. The notebook will rebuild or reuse the local embedding cache.

## Repository Contents

- `project.ipynb` - cleaned notebook with EDA, retrieval implementation, evaluation, profiling, and error inspection.

The source metadata file and embedding cache are intentionally excluded from version control.
