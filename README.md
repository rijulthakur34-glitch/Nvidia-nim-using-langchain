# NVIDIA NIM using LangChain

This repository demonstrates how to integrate and use **NVIDIA NIM (NVIDIA Inference Microservice)** endpoints with LangChain and Streamlit to build interactive, retrieval-augmented generation (RAG) applications.

## Project Structure

*   `app.py`: A simple standalone test script to query an LLM on the NVIDIA NIM catalog using the OpenAI Python SDK.
*   `app1.py`: A Streamlit web application that runs a RAG pipeline utilizing NVIDIA Embeddings (`NVIDIAEmbeddings`), NVIDIA Chat Endpoints (`ChatNVIDIA`), and FAISS vector stores to perform similarity searches over document collections.
*   `us_census/`: Directory containing source PDF documents (US Census data) used for RAG ingestion.
*   `requirements.txt`: Python package requirements.
*   `.env`: Local environment variable storage (e.g., API keys).

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rijulthakur34-glitch/Nvidia-nim-using-langchain.git
cd Nvidia-nim-using-langchain
```

### 2. Set Up Virtual Environment
Initialize a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
Install all required libraries:
```bash
pip install -r requirements.txt
```

### 4. Configure Your NVIDIA API Key
Create a `.env` file in the root directory (this is already ignored by `.gitignore` so your keys won't be pushed online):
```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```
> Obtain your API key from the [NVIDIA API Catalog](https://build.nvidia.com/).

---

## How to Run

### Run the Standalone Script (`app.py`)
This script uses the OpenAI SDK to send a direct prompt to the Llama 3.1-70B model:
```bash
python app.py
```

### Run the Streamlit RAG Web App (`app1.py`)
This launches a user interface that loads PDFs from the `us_census/` folder, splits and vectorizes them using NVIDIA Embeddings, and lets you ask questions about the documents:
```bash
streamlit run app1.py
```

1. Click the **"Documents Embedding"** button first to ingest the PDFs and build the vector database.
2. Enter your question in the text input box (e.g., *"What is the main topic of the census reports?"*).
3. View the response along with the relevant chunks sourced during document similarity search.