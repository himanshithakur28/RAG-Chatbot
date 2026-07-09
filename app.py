import streamlit as st
from pypdf import PdfReader

from utils.preprocess import split_sentences, clean_text, create_chunks
from utils.search import find_best_answer

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("📄 PDF Question Answering Chatbot (TF-IDF RAG)")
st.write("Upload a PDF and ask questions based on its content.")
st.header("Upload your PDF file")

uploaded_file = st.file_uploader(
   "choose a PDF file", 
  type=["pdf"]
  )
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    st.success(f"PDF uploaded successfully! ({total_pages} pages)")
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
           text += page_text
   
    sentences = split_sentences(text)
    chunks = create_chunks(sentences)
    cleaned_chunks = [clean_text(chunk) for chunk in chunks]
   
st.header("Ask your question")
question = st.text_input("Ask anything")

if st.button("Ask"):
  if uploaded_file is None:
    st.warning("Please upload a PDF file first.")

  elif question.strip() == "":
        st.warning("Please enter a question.")
  else:
     cleaned_question = clean_text(question)
     answer = find_best_answer(cleaned_question, cleaned_chunks, chunks)   
     st.header("Answer")  
     if answer is None:
      answer = "Sorry, I couldn't find an answer in the uploaded PDF."
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

    