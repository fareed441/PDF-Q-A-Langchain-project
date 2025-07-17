# PDF Q&A with Local LLM (Ollama)

This project is a **Streamlit web app** that lets you upload a PDF and ask questions about its content using a **locally running Large Language Model (LLM)** via [Ollama](https://ollama.com/).  
No OpenAI API key or cloud service is required—everything runs on your own machine!

---

## Features

- 📄 **Upload any PDF** and extract its text
- 🤖 **Ask questions** about the PDF using a local LLM (e.g., `deepseek-r1:1.5b`)
- 🧠 **Embeddings and retrieval** are performed locally for privacy and speed
- 🖥️ **No internet or API key required** (after initial model download)

---

## How It Works

1. **PDF Upload:**  
   The app extracts text from your uploaded PDF using `PyPDF2`.

2. **Text Splitting:**  
   The text is split into manageable chunks for retrieval.

3. **Embeddings:**  
   Each chunk is embedded using `OllamaEmbeddings` (runs locally via Ollama).

4. **Vector Store:**  
   Chunks and embeddings are stored in a FAISS vector database for fast retrieval.

5. **Question Answering:**  
   When you ask a question, the most relevant chunks are retrieved and passed to the local LLM (`OllamaLLM`) for answer generation.

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- The model you want to use downloaded via Ollama (e.g., `deepseek-r1:1.5b`)
- Python packages:  
  ```
  pip install streamlit langchain langchain-ollama langchain-community PyPDF2
  ```

---

## Usage

1. **Start Ollama** and download your model (e.g.):
   ```sh
   ollama pull deepseek-r1:1.5b
   ollama serve
   ```

2. **Run the Streamlit app:**
   ```sh
   streamlit run "pip install langchain.py"
   ```

3. **Open the app in your browser.**
   - Upload a PDF.
   - Ask questions about its content!

---

## About the Model

- **Model Used:** `deepseek-r1:1.5b` (or any other model available in Ollama)
- **Runs Locally:** All inference and embedding generation is performed on your machine via Ollama.
- **No API Key Needed:** You do not need an OpenAI or other cloud API key.

---

## Sample PDF

A sample PDF (`sample.pdf`) is included for testing.

---

## Credits

- [Ollama](https://ollama.com/)
- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [PyPDF2](https://pypdf2.readthedocs.io/)

---

**Enjoy private, local PDF Q&A with
