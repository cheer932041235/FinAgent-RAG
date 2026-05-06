"""
Contrastive Financial Retriever

Dense retriever fine-tuned with four types of domain-specific hard negatives:
- Temporal negatives: same metric, different time period
- Metric-swap negatives: same entity, different financial metric
- Granularity negatives: same metric, different aggregation level
- Entity-swap negatives: same metric, different company/segment
"""

from typing import List, Dict, Optional, Tuple
import numpy as np


class ContrastiveFinancialRetriever:
    """
    Domain-adapted dense retriever for financial document QA.
    
    Fine-tuned from bge-base-en-v1.5 using contrastive learning with
    InfoNCE loss and four types of financial hard negatives.
    
    Args:
        model_path: Path to the fine-tuned encoder weights.
        index_path: Path to the FAISS index.
        embedding_dim: Embedding dimension (default: 768).
    """
    
    def __init__(self, model_path: str, index_path: str, embedding_dim: int = 768):
        self.embedding_dim = embedding_dim
        # Full implementation will be released upon acceptance.
        raise NotImplementedError(
            "Contrastive Financial Retriever weights and training code "
            "will be released upon paper acceptance."
        )
    
    def encode(self, texts: List[str]) -> np.ndarray:
        """Encode texts into dense embeddings."""
        raise NotImplementedError
    
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        exclude_ids: Optional[List[str]] = None
    ) -> List[Dict]:
        """
        Retrieve top-k passages with exclusion-based exploration.
        
        Args:
            query: Query string.
            top_k: Number of passages to retrieve.
            exclude_ids: IDs of previously retrieved passages to exclude.
            
        Returns:
            List of dicts with 'passage_id', 'text', 'score'.
        """
        raise NotImplementedError
    
    def build_index(self, passages: List[Dict]) -> None:
        """Build FAISS index from a corpus of passages."""
        raise NotImplementedError

    @staticmethod
    def generate_hard_negatives(
        anchor: Dict,
        corpus: List[Dict],
        negative_type: str
    ) -> List[Dict]:
        """
        Generate hard negatives for contrastive training.
        
        Args:
            anchor: The anchor passage.
            corpus: Full document corpus.
            negative_type: One of 'temporal', 'metric_swap', 
                          'granularity', 'entity_swap'.
        
        Returns:
            List of hard negative passages.
        """
        raise NotImplementedError
