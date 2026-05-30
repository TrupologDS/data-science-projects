# Evaluation Report

## Scope

This report summarizes the evaluation surface available in the committed Russian LLM pretraining and SFT experiment. It is intentionally conservative: only observed notebook outputs are reported.

## Quantitative Signals

| Signal | Value |
|:--|--:|
| Pretraining train blocks | 44,432 |
| Pretraining validation blocks | 917 |
| Pretraining context length | 512 |
| Effective pretraining batch size | 64 |
| SFT train examples | 7,840 |
| SFT validation examples | 160 |
| SFT training loss | 1.6505 |

## Qualitative Checks

The notebook samples generations before and after SFT on fixed Russian prompts. The intended review criteria are:

- response language matches the prompt;
- answer follows the requested instruction;
- formatting is coherent for list-like requests;
- output does not collapse into repetition.

## Error Taxonomy

- `language_mismatch`: answer switches away from the requested language.
- `instruction_miss`: answer does not address the instruction.
- `format_miss`: answer ignores the requested answer structure.
- `unsupported_claim`: answer introduces unsupported factual claims.
- `degeneration`: answer repeats, collapses, or becomes incoherent.

## Limitations

No external LLM benchmark, preference model evaluation, or human rating study is included. The report should be read as an experiment audit trail rather than a model quality claim.
