from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    return model.encode(chunks)


def find_best_answer(question, chunk_embeddings, chunks):

    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )

    best_score = similarities.max()
    best_index = similarities.argmax()

    if best_score < 0.30:
        return None

    return chunks[best_index]