# 🧠 RAG Flask – Custom GenAI & Agentic AI Backend

A **from-scratch Retrieval-Augmented Generation (RAG) system** built with **Flask**, **Groq LLMs**, and a **custom vector store**, without relying on heavy frameworks like LangChain.

This project is designed to deeply understand **GenAI fundamentals**, **RAG architecture**, and **Agentic AI concepts**, making it **interview-ready and production-aligned**.

---

## 🚀 Features

* ✅ Custom RAG pipeline (no LangChain)
* ✅ Text chunking with overlap
* ✅ SentenceTransformer embeddings
* ✅ In-memory vector store with cosine similarity
* ✅ Semantic retrieval (Top-K search)
* ✅ Groq-powered answer generation
* ✅ Flask API (`/ingest`, `/query`)
* ✅ Agentic AI foundations (tool-based reasoning)
* ✅ Clean, modular architecture

---

## 🏗️ Architecture Overview

```
User
 ├── POST /ingest ──▶ Chunker ─▶ Embedder ─▶ Vector Store
 └── POST /query  ──▶ Retriever ─▶ Prompt Builder ─▶ Groq LLM ─▶ Answer
```

### Key Design Principles

* **Separation of concerns** (ingestion, retrieval, generation)
* **Shared singleton vector store** to avoid state bugs
* **Framework-agnostic core logic**
* **Grounded answers (hallucination control)**

---

## 📁 Project Structure

```
rag-flask/
├── app.py                     # Flask entry point
├── ingest/
│   ├── chunker.py              # Text chunking logic
│   ├── embedder.py             # Embedding layer
│   └── ingest_service.py       # Ingestion pipeline
├── retrieval/
│   └── retriever.py            # Semantic search
├── generation/
│   ├── groq_client.py          # Groq LLM wrapper
│   ├── prompt.py               # Prompt construction
│   └── answer_generator.py     # RAG answer generation
├── agent/
│   └── simple_agent.py         # Agentic AI loop
├── store/
│   ├── vector_store.py         # Custom vector DB
│   └── store.py                # Singleton store
└── README.md
```

---

## 🧠 How RAG Works Here

1. **Ingestion**

   * Raw text is chunked with overlap
   * Chunks are embedded into vectors
   * Stored in a custom vector store

2. **Retrieval**

   * User query is embedded
   * Cosine similarity finds relevant chunks

3. **Generation**

   * Retrieved context is injected into prompt
   * Groq LLM generates a grounded answer
   * If context is missing → "I don’t know"

---

## 🧪 API Usage

### 🔹 Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok",
  "vectors": 5
}
```

---

### 🔹 Ingest Data

```
POST /ingest
Content-Type: application/json

{
  "text": "JWT tokens are stateless authentication tokens..."
}
```

---

### 🔹 Query

```
POST /query
Content-Type: application/json

{
  "question": "How do JWT tokens expire?"
}
```

Response:

```json
{
  "question": "How do JWT tokens expire?",
  "answer": "JWT tokens expire after a fixed duration..."
}
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```
pip install flask sentence-transformers groq
```

### 3️⃣ Set Environment Variable

```
setx GROQ_API_KEY "your_groq_api_key"
```

### 4️⃣ Run Server

```
python app.py
```

---

## 🤖 Agentic AI (STEP 9)

This project introduces **Agentic AI concepts** without frameworks:

* Tool-based reasoning
* Conditional execution
* Multi-step decision logic

Agents are implemented as **control-flow loops**, not magic abstractions.

---

## ❌ Why Not LangChain?

* Avoids hidden abstractions
* Easier debugging
* Stable core logic
* Better interview explanations
* Full control over retrieval & generation

LangChain can be added later **once fundamentals are solid**.

---

## 📌 Known Limitations (Intentional)

* In-memory vector store (resets on restart)
* Single-process Flask app
* No authentication
* No streaming responses

These are solvable extensions.

---

## 🧑‍💻 Skills Demonstrated

* GenAI system design
* RAG fundamentals
* Vector similarity search
* Prompt engineering
* Agentic AI concepts
* Flask backend development
* Debugging real-world AI issues

---

## 📄 Resume-Ready Description

> Built a custom Retrieval-Augmented Generation (RAG) backend using Flask and Groq LLMs with semantic search, vector similarity retrieval, and agentic AI foundations — without relying on LangChain.

---

## 🚀 Next Possible Enhancements

* Persistent vector DB (FAISS / Qdrant)
* Streaming responses
* Tool calling via MCP
* Multi-agent collaboration
* Evaluation & metrics
* Authentication & rate limiting

---

**Author:** Mukul Thakur
**Purpose:** Learning-first, job-ready GenAI engineering
