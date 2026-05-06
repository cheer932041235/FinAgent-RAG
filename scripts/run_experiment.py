"""
FinAgent-RAG Experiment Runner

Usage:
    python scripts/run_experiment.py --dataset finqa --config configs/default.yaml
    python scripts/run_experiment.py --dataset convfinqa --use-router
    python scripts/run_experiment.py --dataset tatqa --backbone gpt-4o
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def parse_args():
    parser = argparse.ArgumentParser(description="Run FinAgent-RAG experiments")
    parser.add_argument("--dataset", type=str, required=True,
                        choices=["finqa", "convfinqa", "tatqa"],
                        help="Benchmark dataset to evaluate on")
    parser.add_argument("--config", type=str, default="configs/default.yaml",
                        help="Path to configuration file")
    parser.add_argument("--backbone", type=str, default="deepseek-v3",
                        help="LLM backbone (deepseek-v3, gpt-4o, qwen-2.5-72b, llama-3.1-70b)")
    parser.add_argument("--use-router", action="store_true",
                        help="Enable Adaptive Strategy Router")
    parser.add_argument("--max-iterations", type=int, default=None,
                        help="Override max iterations K")
    parser.add_argument("--output-dir", type=str, default="results/",
                        help="Directory to save results")
    parser.add_argument("--split", type=str, default="test",
                        choices=["validation", "test"],
                        help="Dataset split to evaluate")
    return parser.parse_args()


def main():
    args = parse_args()
    
    print(f"=" * 60)
    print(f"FinAgent-RAG Experiment")
    print(f"  Dataset:    {args.dataset}")
    print(f"  Backbone:   {args.backbone}")
    print(f"  Router:     {'enabled' if args.use_router else 'disabled'}")
    print(f"  Config:     {args.config}")
    print(f"=" * 60)
    
    # Full experiment pipeline will be released upon paper acceptance.
    raise NotImplementedError(
        "Complete experiment reproduction scripts will be released "
        "upon paper acceptance. Please refer to Section 4 of the paper "
        "for experimental setup details."
    )


if __name__ == "__main__":
    main()
