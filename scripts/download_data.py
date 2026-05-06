"""
Download benchmark datasets for FinAgent-RAG evaluation.

Datasets:
    - FinQA: https://github.com/czyssrs/FinQA
    - ConvFinQA: https://github.com/czyssrs/ConvFinQA
    - TAT-QA: https://github.com/NExTplusplus/TAT-QA
"""

import os
import subprocess
import sys


DATASETS = {
    "finqa": {
        "repo": "https://github.com/czyssrs/FinQA.git",
        "description": "8,281 QA pairs from S&P 500 earnings reports"
    },
    "convfinqa": {
        "repo": "https://github.com/czyssrs/ConvFinQA.git",
        "description": "3,892 multi-turn financial conversations"
    },
    "tatqa": {
        "repo": "https://github.com/NExTplusplus/TAT-QA.git",
        "description": "16,552 hybrid tabular-textual questions"
    }
}


def download_dataset(name: str, target_dir: str = "data"):
    """Download a benchmark dataset."""
    if name not in DATASETS:
        print(f"Unknown dataset: {name}. Available: {list(DATASETS.keys())}")
        return
    
    info = DATASETS[name]
    dest = os.path.join(target_dir, name)
    
    if os.path.exists(dest):
        print(f"[skip] {name} already exists at {dest}")
        return
    
    print(f"[download] {name}: {info['description']}")
    print(f"  Source: {info['repo']}")
    os.makedirs(target_dir, exist_ok=True)
    subprocess.run(["git", "clone", info["repo"], dest], check=True)
    print(f"[done] {name} saved to {dest}")


if __name__ == "__main__":
    datasets = sys.argv[1:] if len(sys.argv) > 1 else list(DATASETS.keys())
    for ds in datasets:
        download_dataset(ds)
