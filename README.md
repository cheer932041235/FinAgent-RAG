# FinAgent-RAG: Agentic Retrieval-Augmented Generation for Financial Document Question Answering

[![Paper](https://img.shields.io/badge/Paper-Preprint-blue)](paper/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)](https://python.org)

## Overview

**FinAgent-RAG** is an agentic RAG framework specifically designed for financial document question answering. It orchestrates iterative retrieval-reasoning loops with self-verification, integrating three domain-specific innovations:

1. **Contrastive Financial Retriever** — trained with hard negative mining (temporal, metric-swap, granularity, entity-swap) to distinguish semantically similar but numerically distinct financial passages
2. **Program-of-Thought (PoT) Reasoning** — generates executable Python code for precise arithmetic instead of relying on error-prone LLM mental computation
3. **Adaptive Strategy Router** — dynamically allocates computational resources based on question complexity, reducing API costs by 41.3% while preserving accuracy

<p align="center">
  <img src="figures/framework.png" width="85%" alt="FinAgent-RAG Framework"/>
</p>

## Key Results

| Benchmark | Exe Acc (%) | vs. Best Baseline |
|-----------|-------------|-------------------|
| FinQA     | **76.81**   | +8.98 pp          |
| ConvFinQA | **78.46**   | +9.32 pp          |
| TAT-QA    | **74.96**   | +5.62 pp          |

- Cross-backbone evaluation: consistent +20–24% improvement across GPT-4o, DeepSeek-V3, Qwen-2.5-72B, and Llama-3.1-70B
- PoT reasoning eliminates 88.0% of arithmetic errors
- Adaptive Router reduces API costs by 41.3% with only 1.34% accuracy trade-off

## Architecture

```
Financial Question q
        │
        ▼
┌─────────────────┐
│ Query Decomposer│ → Sub-questions [s₁, s₂, ..., sₘ]
└────────┬────────┘
         │
    ┌────▼────┐
    │ for k=1 │──────────────────────────────────┐
    │  to K   │                                  │
    └────┬────┘                                  │
         │                                       │
┌────────▼─────────┐   ┌──────────────────────┐  │
│ Adaptive Retriever│──▶│ Contrastive Financial │  │
│ (with exclusion)  │   │ Retriever (fine-tuned)│  │
└────────┬─────────┘   └──────────────────────┘  │
         │                                       │
┌────────▼─────────┐                             │
│ Strategy Router   │ → simple / complex         │
└──┬───────────┬───┘                             │
   │           │                                 │
┌──▼──┐    ┌──▼──┐                               │
│ CoT │    │ PoT │ (sandboxed execution)         │
└──┬──┘    └──┬──┘                               │
   └────┬─────┘                                  │
        │                                        │
┌───────▼────────┐                               │
│ Self-Verifier  │ → ACCEPT / REJECT             │
│ (3 checks)     │                               │
└───────┬────────┘                               │
    ACCEPT│    REJECT│                            │
        │    ┌──────▼───────┐                    │
        │    │ Query Refiner │────────────────────┘
        │    └──────────────┘
        ▼
   Final Answer a
```

## Installation

```bash
git clone https://github.com/cheer932041235/FinAgent-RAG.git
cd FinAgent-RAG
pip install -r requirements.txt
```

## Project Structure

```
FinAgent-RAG/
├── src/
│   ├── pipeline.py              # Main agentic RAG pipeline
│   ├── query_decomposer.py      # Financial query decomposition
│   ├── retriever.py             # Contrastive financial retriever
│   ├── reasoner.py              # CoT and PoT reasoning modules
│   ├── router.py                # Adaptive strategy router
│   ├── verifier.py              # Self-verification with query refinement
│   └── utils.py                 # Evaluation and utility functions
├── configs/
│   └── default.yaml             # Default hyperparameter configuration
├── scripts/
│   └── run_experiment.py        # Experiment runner
├── data/                        # Dataset directory (see below)
├── figures/                     # Paper figures
└── requirements.txt
```

## Datasets

We evaluate on three established financial QA benchmarks:

- **FinQA** ([Chen et al., 2021](https://github.com/czyssrs/FinQA)): 8,281 QA pairs from S&P 500 earnings reports
- **ConvFinQA** ([Chen et al., 2022](https://github.com/czyssrs/ConvFinQA)): 3,892 multi-turn conversations
- **TAT-QA** ([Zhu et al., 2021](https://github.com/NExTplusplus/TAT-QA)): 16,552 hybrid tabular-textual questions

## Usage

```bash
# Download datasets
python scripts/download_data.py

# Run full experiment on FinQA
python scripts/run_experiment.py --dataset finqa --config configs/default.yaml

# Run with Adaptive Router enabled
python scripts/run_experiment.py --dataset finqa --use-router --config configs/default.yaml
```

## Configuration

Key hyperparameters (see `configs/default.yaml`):

| Parameter | Value | Description |
|-----------|-------|-------------|
| Max iterations K | 3 | Maximum agentic loop iterations |
| Confidence threshold θ | 0.8 | Self-verifier acceptance threshold |
| Top-k passages | 5 | Retrieved passages per sub-question |
| Chunk size | 512 tokens | Document chunk size |
| Chunk overlap | 64 tokens | Overlap between chunks |

## Code Release Status

> **Note**: This repository currently provides the framework architecture and module interfaces. The complete implementation, including trained Contrastive Financial Retriever weights, full prompt templates, and experiment reproduction scripts, will be released upon paper acceptance.

## Citation

If you find this work useful, please cite:

```bibtex
@article{shu2026finagentrag,
  title={Agentic Retrieval-Augmented Generation for Financial Document Question Answering},
  author={Shu, Yang},
  journal={Expert Systems with Applications},
  year={2026}
}
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
