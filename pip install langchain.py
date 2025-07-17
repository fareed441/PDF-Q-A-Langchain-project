import PyPDF2
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

st.title("PDF Q&A with Local LLM (Ollama)")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")
if pdf_file:
    raw_text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            raw_text += text

    if not raw_text.strip():
        st.error("No text could be extracted from the PDF.")
    else:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)
        if not texts:
            st.error("Text splitting produced no chunks.")
        else:
            embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")
            docsearch = FAISS.from_texts(texts, embeddings)
            llm = OllamaLLM(model="deepseek-r1:1.5b")
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

            question = st.text_input("Ask a question about the PDF:")
            if question:
                answer = qa.invoke(question)
                st.success(answer.get("result", answer))
