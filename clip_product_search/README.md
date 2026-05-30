# Text-to-Image Product Search with Fine-Tuned CLIP

Product retrieval project for an online fashion catalog. The system fine-tunes CLIP on image-description pairs, builds image embeddings, and retrieves product photos from text queries.

## Objective

Adapt a pretrained CLIP model to product-catalog descriptions and build a text-to-image retrieval workflow suitable for interactive catalog search.

## Architecture

- Base model: Hugging Face `CLIPModel`.
- Processor: CLIP image/text processor for paired batches.
- Training objective: symmetric contrastive image-text loss from CLIP.
- Search index: full-catalog image embedding matrix ranked by cosine similarity.

## Data

The project expects a fashion product CSV and image archive. Images, catalog CSV files, embeddings, and checkpoints are intentionally excluded from version control.

## Method

- Loaded and validated a product catalog with image paths and text descriptions.
- Built PyTorch datasets and CLIP processor-based batching for image-text pairs.
- Measured pretrained CLIP baseline matching quality.
- Fine-tuned CLIP with contrastive image-text loss.
- Built a reusable image embedding index for search.
- Implemented query-time text-to-image retrieval with top-k product previews.

## Evaluation

The notebook tracks average CLIP loss and image-text matching score on the validation subset. Search examples are inspected qualitatively with product previews.

## Results

| Metric | Value |
|:--|--:|
| Full train split | 39,742 |
| Full test split | 4,416 |
| Training subset used | 4,096 |
| Validation subset used | 768 |
| Baseline CLIP score | 29.67 |
| Final validation CLIP score | 30.51 |

## Limitations

- Validation uses CLIP matching score rather than a human-judged retrieval benchmark.
- The committed repository does not include product images or trained model weights.
- Product descriptions can contain noisy catalog text, which affects retrieval quality.

## How to Reproduce

Place the Kaggle-style image archive and catalog CSV in the project directory, install the root requirements, and run `project.ipynb`. Generated checkpoints, embeddings, and metrics should remain in ignored artifact directories.

## Repository Contents

- `project.ipynb` - cleaned notebook with data checks, baseline evaluation, CLIP fine-tuning, embedding index creation, and search examples.

Images, model checkpoints, embeddings, and catalog CSV files are intentionally excluded from version control.
