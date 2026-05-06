"""
Adaptive Strategy Router

Lightweight LightGBM classifier that predicts question complexity
and routes questions to cost-efficient processing paths:
- simple → single-pass retrieval + direct PoT reasoning
- complex → full agentic loop with up to K iterations

Trained on FinQA validation set (883 examples) with 5-fold cross-validation.
Achieves 87.34% routing accuracy (91.2% precision for complex, 84.1% for simple).
"""

from typing import Dict, Tuple
import numpy as np


class AdaptiveStrategyRouter:
    """
    Routes financial questions to simple or complex processing paths
    based on predicted complexity.
    
    Feature groups (14 dimensions total):
        1. Syntactic features (5 dims): question length, token count,
           sub-clause count, question type, entity count
        2. Semantic features (3 dims): embedding similarity to table vs text,
           query decomposition tree depth
        3. Temporal features (3 dims): distinct time periods referenced,
           year-over-year comparison patterns, temporal span
        4. Computation features (3 dims): one-hot encoding of implied
           computation type (lookup, single-step, multi-step, metric)
    
    Args:
        model_path: Path to trained LightGBM model.
        threshold: Classification threshold (default: 0.5).
    """
    
    def __init__(self, model_path: str, threshold: float = 0.5):
        self.threshold = threshold
        raise NotImplementedError(
            "Router model and feature extraction code will be released "
            "upon paper acceptance."
        )
    
    def predict(self, question: str, metadata: Dict = None) -> Tuple[str, float]:
        """
        Predict question complexity.
        
        Returns:
            Tuple of (route: 'simple'|'complex', confidence: float).
        """
        raise NotImplementedError
    
    def extract_features(self, question: str) -> np.ndarray:
        """Extract 14-dimensional feature vector from a question."""
        raise NotImplementedError
