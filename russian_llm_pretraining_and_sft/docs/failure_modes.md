# Failure Modes and Next Evaluation Steps

## Scope

This project validates a compact LLM training and SFT pipeline.

It should not be read as a claim that the resulting model is production-ready.

## Observed / expected failure modes

Realistic failure modes for this scale of experiment include:

- repetitive generations
- weak long-context coherence
- factual hallucinations
- sensitivity to prompt formatting
- inconsistent instruction following
- style drift after SFT
- limited safety/refusal behavior coverage
- domain mismatch between pretraining and instruction data

## Before/after SFT examples

The committed notebook defines before/after SFT generation steps, but the repository does not include generated outputs or checkpoints.

Do not invent examples when reviewing this project.

- TODO: add observed prompts from a rerun.
- TODO: paste actual base-model outputs from the rerun.
- TODO: paste actual SFT outputs from the rerun.
- TODO: label observed failure modes or improvements.

## Next evaluation steps

- instruction-following gold set
- held-out prompts
- toxicity/safety prompts
- preference-pair review
- simple human evaluation rubric
- multilingual/Russian-specific eval prompts
- comparison against base Qwen2.5-0.5B behavior
- latency/memory notes if measured
