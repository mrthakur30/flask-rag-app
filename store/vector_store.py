
import math
from typing import Dict, List


class VectorStore:
    def __init__(self):
        self.vectors: List[Dict] = []

    def add(self, text: str, embedding: List[float]):
        self.vectors.append({
            "text" : text,
            "embedding" : embedding
        })
    
    def cosine_similarity(self, a: List[float], b: List[float]) -> float :
        dot_product = sum(x*y for x,y in zip(a,b))
        norm_a = math.sqrt(sum(x*x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        
        if norm_a == 0 or norm_b == 0:
           return 0.0
        
        return dot_product / (norm_a * norm_b)

    def search(self, query_embedding : List[float], top_k: int = 3) -> List[str] :
        scored = []

        for item in self.vectors:
            score = self.cosine_similarity(
                query_embedding,
                item["embedding"]
                )
            scored.append((score,item["text"]))
        scored.sort(key=lambda x: x[0], reverse=True) 

        return [text for _, text in scored[:top_k]]  

    
      
    
