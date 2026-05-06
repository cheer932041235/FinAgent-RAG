"""
Financial Query Decomposer

Breaks complex financial questions into ordered sub-questions,
each targeting a specific evidence retrieval or computation step.

Five decomposition patterns for financial QA:
1. Temporal comparison: split by time period
2. Multi-metric aggregation: split by financial metric
3. Ratio computation: split into numerator and denominator
4. Cross-document: split by source document/table
5. Conditional filtering: split filter condition from computation
"""

from typing import List


class QueryDecomposer:
    """
    Decomposes complex financial questions into sub-questions.
    
    Uses an LLM with a structured prompt template that handles
    financial-specific decomposition patterns (temporal comparison,
    multi-metric aggregation, ratio computation, etc.).
    
    Args:
        llm_client: LLM API client for decomposition.
    """
    
    def __init__(self, llm_client):
        self.llm = llm_client
        raise NotImplementedError(
            "Decomposition prompt templates will be released upon paper acceptance."
        )
    
    def decompose(self, question: str) -> List[str]:
        """
        Decompose a financial question into ordered sub-questions.
        
        Args:
            question: Complex financial question string.
            
        Returns:
            Ordered list of sub-questions [s_1, s_2, ..., s_m].
        """
        raise NotImplementedError
