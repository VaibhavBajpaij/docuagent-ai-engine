import numpy as np
import time
from typing import Optional, Tuple, Dict, Any

class SemanticCache:
    """
    In-memory vector similarity cache mimicking Redis Vector Store for sub-50ms cache hits.
    Computes cosine similarity against cached query embeddings.
    """
    def __init__(self, similarity_threshold: float = 0.90):
        self.similarity_threshold = similarity_threshold
        # Stores: query -> { embedding, answer, metadata, timestamp }
        self._cache: Dict[str, Dict[str, Any]] = {}

    def _mock_embed(self, text: str) -> np.ndarray:
        """Deterministic pseudo-embedding for testing & offline execution."""
        vec = np.zeros(64, dtype=np.float32)
        for i, char in enumerate(text.lower()):
            vec[i % 64] += ord(char)
        norm = np.linalg.norm(vec)
        return vec / (norm + 1e-8)

    def get(self, query: str) -> Optional[Tuple[str, float, str]]:
        if not self._cache:
            return None
        target_vec = self._mock_embed(query)
        best_sim = -1.0
        best_hit = None
        best_agent = "doc_agent"

        for cached_query, data in self._cache.items():
            sim = float(np.dot(target_vec, data['embedding']))
            if sim > best_sim:
                best_sim = sim
                best_hit = data['answer']
                best_agent = data.get('routed_agent', 'doc_agent')

        if best_sim >= self.similarity_threshold and best_hit:
            return best_hit, best_sim, best_agent
        return None

    def set(self, query: str, answer: str, routed_agent: str = "doc_agent") -> None:
        self._cache[query] = {
            'embedding': self._mock_embed(query),
            'answer': answer,
            'routed_agent': routed_agent,
            'timestamp': time.time()
        }

    def clear(self) -> None:
        self._cache.clear()
