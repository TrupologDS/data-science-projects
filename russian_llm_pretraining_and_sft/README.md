# Russian LLM Pretraining and Instruction Tuning

Experiment report and reproducible scaffold for two related LLM post-training workflows: compact causal LM pretraining on Russian literature and LoRA supervised fine-tuning of an existing instruction model.

## Objective

Demonstrate the mechanics of a language-model training workflow end to end: corpus preparation, tokenizer training, causal LM packing, trainer configuration, qualitative generation review, instruction-tuning data formatting, and lightweight evaluation reporting.

## Architecture

- Pretraining model: Llama-style decoder-only causal LM configured in `transformers`.
- Tokenizer: ByteLevel BPE with a compact 3k-token vocabulary.
- SFT base model: `Qwen/Qwen2.5-0.5B`.
- Adaptation method: LoRA with TRL `SFTTrainer`.
- Supporting code: small `src/` package for configs, preprocessing, chat formatting, evaluation summaries, and reproducibility checks.

## Data

- Pretraining corpus: Russian literature text files prepared into cleaned sentence-level examples.
- SFT corpus: Russian Alpaca-style instruction examples converted into a chat/message format.
- The repository does not include raw corpora, model weights, checkpoints, Hugging Face caches, or generated artifacts.

## Method

- Normalize and clean text before tokenizer/model training.
- Pack tokenized examples into fixed 512-token causal LM blocks.
- Use an effective pretraining batch size of 64 with gradient accumulation.
- Record fixed-prompt generations during evaluation for qualitative inspection.
- Preserve assistant-only loss during SFT so system/user tokens are not optimized as target responses.

## Evaluation

The notebook is kept as the experiment report. It records training configuration, dataset sizes, SFT training loss, and qualitative generation checks before and after instruction tuning. Additional evaluation notes live in [eval_report.md](eval_report.md).

Failure modes and next evaluation steps are documented in [docs/failure_modes.md](docs/failure_modes.md).

## Run Snapshot

| Component | Value |
|:--|--:|
| Pretraining train blocks | 44,432 |
| Pretraining validation blocks | 917 |
| Pretraining context length | 512 |
| Effective pretraining batch size | 64 |
| SFT train examples | 7,840 |
| SFT validation examples | 160 |
| SFT training loss | 1.6505 |

## Results

The run validates the training pipeline rather than claiming a production-ready language model. The main quantitative value available from the committed experiment is the SFT training loss shown above. Qualitative generations are inspected in the notebook and summarized in the evaluation report.

## Limitations

- The pretraining run is intentionally small and should not be interpreted as a competitive foundation model.
- No external benchmark scores are reported because they were not run for this project.
- Final weights and adapters are excluded from the repository.
- Some reproduction steps require GPU resources and access to the source datasets.

## How to Reproduce

```bash
cd russian_llm_pretraining_and_sft
make install
make test
make lint
```

To rerun the full notebook, provide the source corpora locally and execute `project.ipynb`. Generated files should remain under ignored artifact directories such as `outputs/`, `checkpoints/`, or local caches.

## Repository Contents

- `project.ipynb` - cleaned notebook covering corpus preparation, tokenizer training, model pretraining, LoRA SFT, and sample generations.
- `src/` - reusable utilities extracted from the notebook workflow.
- `configs/` - small YAML configs for pretraining and SFT runs.
- `tests/` - fast unit tests for deterministic preprocessing/evaluation logic.
- `model_card.md` - model-card style summary for the experiment.
- `eval_report.md` - concise evaluation and limitation report.
- `docs/failure_modes.md` - failure-mode notes and next evaluation steps.

Model weights, Hugging Face caches, and generated artifacts are intentionally excluded from version control.
