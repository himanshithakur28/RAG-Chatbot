# Intelligent PDF Question Answering Chatbot (RAG)

An AI-powered PDF Question Answering chatbot that allows users to upload any PDF and ask questions about its content. The application uses **Sentence Transformers** for semantic search and **Groq Llama 3.1** to generate context-aware responses using a **Retrieval-Augmented Generation (RAG)** pipeline.

---

## Features

-  Upload any PDF document
-  Ask questions based on the uploaded document
-  Semantic search using Sentence Transformers
-  Context-aware responses using Groq Llama 3.1
-  Cosine Similarity for document retrieval
-  Chat history
-  Interactive Streamlit interface

---
## Technologies Used

- Python
- Streamlit
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Groq API (Llama 3.1)
- Scikit-learn
- PyPDF
- NLTK
- Git & GitHub

---

## Screenshots

### Home Page

![Home Page](screenshots/Home.png)

---

### PDF Uploaded

![Upload](screenshots/upload.png)

---

### Chat History

![Chat](screenshots/chat.png)

---

### Question

![Question](screenshots/question.png)

---

##  Project Structure

```
RAG-Chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── utils/
│   ├── preprocess.py
│   ├── search.py
│   └── llm.py
│
└── README.md
```

---
##  How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the document into chunks.
4. Generate embeddings using Sentence Transformers.
5. Compare the user's question with document chunks using Cosine Similarity.
6. Retrieve the most relevant chunk.
7. Send the retrieved context and user question to the Groq LLM.
8. Display a natural language answer.

---
##  RAG Pipeline

```
User Question
       │
       ▼
Upload PDF
       │
       ▼
Extract Text
       │
       ▼
Chunk Document
       │
       ▼
Sentence Transformer Embeddings
       │
       ▼
Cosine Similarity
       │
       ▼
Retrieve Relevant Context
       │
       ▼
Groq Llama 3.1
       │
       ▼
Generated Answer
```
---
##  Installation

Clone the repository

```bash
git clone https://github.com/himanshithakur28/RAG-Chatbot.git
```

Move into the project folder

```bash
cd RAG-Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```
Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key

```text
GROQ_API_KEY=your_api_key_here
```

Run the application

```bash
streamlit run app.py
```

---
## Future Improvements

- FAISS / ChromaDB vector database
- Retrieve Top-K document chunks
- Conversation memory
- Support for multiple PDFs
- Source citations
- Hybrid search (Keyword + Semantic Search)

---

LinkedIn: *(linkedin.com/in/himanshithakur2811)*
---

##  If you found this project useful, consider giving it a star!
