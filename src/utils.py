"""
Utility functions for FinAgent-RAG evaluation and data processing.
"""

from typing import List, Dict, Tuple
import re


def execution_accuracy(predicted: str, gold: str, tolerance: float = 0.01) -> bool:
    """
    Compute execution accuracy: whether the predicted numerical answer
    matches the gold answer within a tolerance of 1%.
    
    Args:
        predicted: Predicted answer string.
        gold: Gold answer string.
        tolerance: Relative tolerance (default: 1%).
        
    Returns:
        True if answers match within tolerance.
    """
    try:
        pred_val = float(re.sub(r'[,$%]', '', str(predicted).strip()))
        gold_val = float(re.sub(r'[,$%]', '', str(gold).strip()))
        if gold_val == 0:
            return abs(pred_val) < 1e-6
        return abs(pred_val - gold_val) / abs(gold_val) <= tolerance
    except (ValueError, TypeError):
        return str(predicted).strip().lower() == str(gold).strip().lower()


def program_accuracy(predicted_program: str, gold_program: str) -> bool:
    """
    Compute program accuracy: whether the predicted reasoning program
    matches the gold program structure.
    """
    raise NotImplementedError


def linearize_table(table: List[List[str]], headers: List[str]) -> str:
    """
    Linearize a financial table using header-prepended row format.
    
    For each row r in a table with headers [h1, h2, ..., hc],
    generates: "h1: r1 | h2: r2 | ... | hc: rc"
    
    Args:
        table: 2D list of cell values.
        headers: List of column header strings.
        
    Returns:
        Linearized string representation.
    """
    rows = []
    for row in table:
        pairs = [f"{h}: {v}" for h, v in zip(headers, row)]
        rows.append(" | ".join(pairs))
    return "\n".join(rows)


def chunk_document(
    text: str,
    chunk_size: int = 512,
    overlap: int = 64,
    tokenizer=None
) -> List[Dict]:
    """
    Chunk a document into overlapping passages at paragraph level.
    
    Args:
        text: Document text.
        chunk_size: Maximum chunk size in tokens.
        overlap: Overlap between consecutive chunks.
        tokenizer: Tokenizer for token counting (default: tiktoken cl100k).
        
    Returns:
        List of chunk dicts with 'text', 'start_idx', 'end_idx'.
    """
    raise NotImplementedError
