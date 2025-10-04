import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

def add_document(text:str):
    vector = embedding_model.encode([text])
    index.add(np.array(vector, dtype='float32'))
    documents.append(text)

def search(query: str, top_k: int = 3):
    vector = embedding_model.encode([query])
    distances, indices = index.search(np.array(vector, dtype='float32'), top_k)
    results = []
    for idx, dist in zip(indices[0], distances[0]):
        if idx < len(documents):
            if idx < len(documents):
                results.append({"text": documents[idx], "score": float(dist)})
    return results            