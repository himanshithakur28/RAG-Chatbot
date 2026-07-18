import streamlit as st
from pypdf import PdfReader
from utils.llm import generate_answer
from utils.preprocess import split_paragraphs, expand_abbreviations
from utils.search import create_embeddings, find_best_answer

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("📄 AI-Powered PDF Question Answering Chatbot")
st.write("Upload a PDF and ask questions based on its content.")

st.header("Upload your PDF file")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    total_pages = len(reader.pages)

    st.success(
        f"PDF uploaded successfully! ({total_pages} pages)"
    )

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    chunks = split_paragraphs(text)
   

    # Create embeddings only once
    chunk_embeddings = create_embeddings(chunks)

st.header("Ask your question")

question = st.text_input("Ask anything")

if st.button("Ask"):

    if uploaded_file is None:
        st.warning("Please upload a PDF file first.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:
        expanded_question = expand_abbreviations(question)

        context = find_best_answer(
            expanded_question,
            chunk_embeddings,
            chunks
        )

        if context is None:
            answer = "Sorry, I couldn't find an answer in the uploaded PDF."
        else:
            answer = generate_answer(question, context)

        st.header("Answer")
        st.success(answer)

        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )
if st.session_state.chat_history:

    st.header("Chat History")

    for chat in st.session_state.chat_history:

        st.markdown(f"**🧑 You:** {chat['question']}")

        st.markdown(f"**🤖 Bot:** {chat['answer']}")

        st.write("---")