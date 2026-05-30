# Model Card: Russian LLM Training Experiment

## Model Details

This project contains an experiment report, not a released production model. It covers:

- a compact Llama-style causal LM trained on a Russian literature corpus;
- a LoRA SFT adapter workflow for `Qwen/Qwen2.5-0.5B` on Russian instruction data.

Weights, adapters, tokenizer artifacts, and generated samples are not included in the repository.

## Intended Use

The project is intended for reviewing the training and evaluation workflow: data preparation, tokenizer setup, trainer configuration, assistant-only SFT formatting, and experiment reporting.

## Out-of-Scope Use

The experiment should not be used as a deployed assistant, factual QA system, or safety-critical model. No claim is made that the resulting model is robust, aligned, or benchmark-competitive.

## Training Data

The notebook uses a Russian literature corpus for causal LM pretraining and Russian Alpaca-style examples for supervised fine-tuning. The source datasets are referenced in the notebook but are not committed.

## Evaluation

The committed experiment reports dataset sizes, configuration choices, SFT training loss, and qualitative generation checks. No external benchmark score is reported.

## Limitations

- Small-scale pretraining run.
- Limited evaluation surface.
- No released weights.
- Reproduction requires local data access and suitable compute.
