from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def find_best_answer(question, cleaned_chunks, original_chunks):
    vectorizer = TfidfVectorizer()
    chunk_vectors = vectorizer.fit_transform(cleaned_chunks)
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, chunk_vectors)
    best_score = similarities.max()
    best_index = similarities.argmax()

    if best_score < 0.30:
     return None

    return original_chunks[best_index]