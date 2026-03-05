from sentence_transformers import SentenceTransformer

# Load model once (global singleton)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def generate_embedding(text: str):
    if not text:
        return None

    vector = model.encode(text, normalize_embeddings=True)

    # Convert numpy array → list for pgvector
    return vector.tolist()