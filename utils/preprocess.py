import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

stop_word = set(stopwords.words('english'))

def split_sentences(text):
    return sent_tokenize(text)

def clean_text(text):
    text = text.lower()
    words = word_tokenize(text)    
    expanded_words = []

    for word in words:
        if word == "ai":
            expanded_words.extend(["artificial", "intelligence"])
        elif word == "ml":
            expanded_words.extend(["machine", "learning"])
        else:
            expanded_words.append(word)

    cleaned_words = []

    for word in expanded_words:
        if word not in string.punctuation and word not in stop_word:
            cleaned_words.append(word)

    return " ".join(cleaned_words)

def create_chunks(sentences, chunk_size=3):
    chunks = []

    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i:i + chunk_size])
        chunks.append(chunk)

    return chunks