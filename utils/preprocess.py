import re

def split_paragraphs(text):

    text = text.replace("\r", "")

    pattern = r'(?=\n?[A-Z][A-Za-z\s()\-]{2,40}\n)'

    chunks = re.split(pattern, text)

    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    return chunks


def expand_abbreviations(text):

    abbreviations = {
        "AI": "Artificial Intelligence",
        "ML": "Machine Learning",
        "NLP": "Natural Language Processing",
        "DL": "Deep Learning",
        "RAG": "Retrieval Augmented Generation",
    }

    words = text.split()

    expanded = []

    for word in words:
        clean_word = word.upper().strip("?,.!")

        if clean_word in abbreviations:
            expanded.append(abbreviations[clean_word])
        else:
            expanded.append(word)

    return " ".join(expanded)