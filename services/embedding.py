from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once (global singleton)
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    if not text:
        return None

    vector = model.encode(text)

    # Convert numpy array to Python list (required for pgvector)
    return vector.tolist()