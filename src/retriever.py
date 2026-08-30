import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def retrieve_chunks(query, chunks, chunk_embeddings, top_k=3):
    query_embedding = model.encode(query)

    similarities = []

    for embedding in chunk_embeddings:
        score = cosine_similarity(
            embedding,
            query_embedding
        )

        similarities.append(score)

    similarities = np.array(similarities)

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "chunk": chunks[index],
            "score": similarities[index]
        })

    return results