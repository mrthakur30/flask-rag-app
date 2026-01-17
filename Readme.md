# 🧠 RAG Flask – GenAI & Agentic AI From Scratch

A **from-scratch Retrieval-Augmented Generation (RAG) system** built using **Flask**, **Groq LLMs**, and a **custom in-memory vector store**, without LangChain or heavy abstractions.

This project is intentionally designed for **deep understanding**, **debuggability**, and **job readiness** in GenAI / Agentic AI roles.

---

## 🚀 What This Project Teaches

* How RAG actually works under the hood
* How embeddings, chunking, and vector search fit together
* How LLMs are grounded using retrieved context
* How Agentic AI differs from simple chatbots
* How to structure GenAI backends like real systems

No magic. No black boxes.

---

## 🏗️ High-Level Architecture

```
User
 ├── POST /ingest ──▶ Chunker ─▶ Embedder ─▶ Vector Store
 └── POST /query  ──▶ Retriever ─▶ Prompt Builder ─▶ Groq LLM ─▶ Answer
                         ▲
                         └──── Agent (decision logic)
```

Key principles:

* Clear **write path** (ingestion)
* Clear **read path** (retrieval + generation)
* Shared vector store state
* Agent controls *when* tools are used

---

## 📁 Project Structure (Explained)

```
rag-flask/
├── app.py                    # Flask entry point (API)
├── config.py                 # App & model configuration
├── ingest/                   # Write path (indexing)
│   ├── chunker.py            # Text chunking with overlap
│   ├── embedder.py           # Embedding generation
│   └── ingest_service.py     # Ingestion orchestration
├── store/                    # Memory & similarity layer
│   ├── vector_store.py       # Custom vector DB + cosine similarity
│   └── store.py              # Singleton vector store instance
├── query/                    # Read path (RAG pipeline)
│   ├── retriever.py          # Semantic search
│   ├── prompt.py             # Prompt construction
│   ├── groq_client.py        # Groq API wrapper
│   └── generate_answer.py    # RAG answer generation
├── agent/                    # Agentic AI logic
│   └── simple_agent.py       # Tool-using decision loop
├── requirements.txt
├── .env
└── README.md
```

Each folder maps to a **real production concern**, not a framework abstraction.

---

## 🧠 RAG Flow (Step-by-Step)

### 1️⃣ Ingestion

* Raw text is chunked with overlap
* Each chunk is embedded into a vector
* Vectors are stored in the vector store

Why overlap?

* Prevents semantic loss at chunk boundaries
* Improves retrieval accuracy

---

### 2️⃣ Retrieval

* User question is embedded
* Cosine similarity finds top-K relevant chunks
* Retrieved chunks form the **grounded context**

---

### 3️⃣ Generation

* Context + question are injected into a strict prompt
* Groq LLM generates an answer
* If context is missing → model must say **"I don’t know"**

This is hallucination control.

---

## 🤖 Agentic AI (Important)

This project does **not** treat agents as libraries.

An agent here is:

* A control loop
* With access to tools (retriever, LLM)
* Making decisions based on state

Example reasoning:

```
If context is empty → don’t answer
If question is vague → retrieve first
If answer already known → skip retrieval
```

This mirrors real agent systems.

---

## ❌ Why No LangChain?

LangChain is intentionally avoided to:

* Understand fundamentals deeply
* Avoid hidden abstractions
* Make debugging obvious
* Explain systems clearly in interviews
* Maintain full architectural control

Frameworks can be added **after mastery**, not before.

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the App

```
python app.py
```

---

## 🧪 Example Usage

### Ingest

```
POST /ingest
{
  "text": "JWT tokens are stateless authentication tokens..."
}
```

### Query

```
POST /query
{
  "question": "How do JWT tokens expire?"
}
```

---

## 🧑‍💻 Skills Demonstrated

* GenAI system design
* RAG from scratch
* Vector similarity search
* Prompt engineering
* Agentic AI fundamentals
* Flask backend development
* Real-world debugging

---

## 📄 Resume-Ready Line

> Built a custom Retrieval-Augmented Generation (RAG) backend using Flask and Groq LLMs with semantic search, grounded generation, and agentic decision logic — without LangChain.

---

## 🚀 Future Extensions

* Persistent vector DB (FAISS / Qdrant)
* Streaming responses
* MCP-style tool servers
* Multi-agent collaboration
* Evaluation & observability

---

**Author:** Mukul Thakur
**Focus:** Learning-first, production-aligned GenAI engineering
