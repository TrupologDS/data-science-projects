# Multi-Task Information Extraction on NEREL

End-to-end NLP experiment for extracting structured information from news texts. The notebook trains a shared transformer encoder with two task-specific heads: token-level named entity recognition and multi-label document/event classification.

## Objective

Show how a single transformer encoder can support two related information-extraction tasks: BIO-tagged named entity recognition and document-level event/relation classification.

## Architecture

- Shared encoder: transformer model from Hugging Face.
- NER head: token classification over BIO labels.
- Document head: multi-label classifier over 30 document/event labels.
- Loss: token cross-entropy plus binary cross-entropy for document labels.

## Data

The experiment uses `danasone/nerel`. The notebook creates a reproducible train/validation/test split from the source dataset. No checkpoints or intermediate datasets are committed.

## Method

- Built a reproducible train/validation/test split for the `danasone/nerel` dataset.
- Implemented word-to-subword BIO label alignment for transformer tokenization.
- Trained a joint PyTorch model with token classification and document-level classification heads.
- Tuned the multi-label classification threshold on validation predictions.
- Added final test evaluation and error analysis for NER confusion patterns and document labels.

## Evaluation

The notebook reports token-level macro-F1, token macro-F1 across all labels, multi-label micro-F1, the selected validation threshold, and qualitative error analysis.

## Results

| Metric | Value |
|:--|--:|
| Documents | 746 |
| Test token macro-F1 | 0.7318 |
| Test token macro-F1, all labels | 0.7485 |
| Test multi-label micro-F1 | 0.8035 |
| Validation-selected threshold | 0.56 |

## Limitations

- The dataset is small, so rare entity and relation types remain difficult.
- Long documents can exceed the encoder context window.
- The project does not include deployment code or saved checkpoints.

## How to Reproduce

Install the root requirements and run `project.ipynb`. The notebook downloads `danasone/nerel` through Hugging Face Datasets and recreates the split, training loop, evaluation, and error analysis.

## Repository Contents

- `project.ipynb` - cleaned notebook with the full modeling workflow.

Large checkpoints and intermediate datasets are intentionally excluded from version control.
