# 🎙️ AI Customer Support Voice Assistant

An AI-powered customer support assistant that lets users **speak** their questions and receive **spoken, context-aware answers** — combining speech recognition, retrieval-augmented generation (RAG), and intent classification into a full voice-in, voice-out conversational pipeline.

---

## How It Works

1. User opens the assistant in the browser.
2. Assistant greets the user by voice and text ("Hello! How can I help you today?").
3. User clicks the mic and speaks a question.
4. Speech is converted to text using the Web Speech API.
5. Backend classifies the query's intent using a trained ML model.
6. Backend retrieves relevant knowledge base content using FAISS.
7. Gemini LLM generates a grounded answer using the retrieved context.
8. Answer is displayed as text and spoken aloud to the user.

---

## Processing Mapping

| Input | Action |
|---|---|
| Spoken Question | Converted to text via Web Speech API (Speech-to-Text) |
| User Query Text | Classified into an intent (e.g. Order Tracking, Returns, Billing) |
| User Query Text | Embedded and matched against FAISS knowledge base |
| Retrieved Context + Query | Sent to Gemini LLM as a grounded prompt |
| Gemini Response | Displayed in chat and spoken aloud via Text-to-Speech |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Web Speech API |
| Backend | Python, FastAPI |
| ML (Intent Classification) | scikit-learn (Logistic Regression + TF-IDF) |
| RAG | LangChain, FAISS, HuggingFace Embeddings (`all-MiniLM-L6-v2`) |
| LLM | Google Gemini API (`google-genai` SDK) |

---

## Features

- **Voice Input** — Real-time speech-to-text with automatic message sending once speech ends.
- **Voice Output** — Responses are spoken aloud automatically; assistant greets the user on load.
- **Intent Classification** — Custom-trained scikit-learn model detects the category of each query.
- **Retrieval-Augmented Generation** — Answers are grounded in a real company knowledge base via FAISS, not just the model's general knowledge.
- **Streaming Responses** — `/chat/stream` endpoint streams tokens as they're generated for a ChatGPT-style typing effect.
- **Latency-Optimized** — Response time profiled and tuned across each pipeline stage (intent, retrieval, generation).

---

## Installation

```
pip install fastapi uvicorn python-dotenv google-genai langchain-huggingface langchain-community faiss-cpu scikit-learn
```

---

## Run the Project

### Start the Backend

```
uvicorn backend.app:app --reload --port 8000
```

### Start the Frontend

Open `frontend/index.html` using **Live Server** (VS Code extension) or any static file server.

> ⚠️ Must be served (not opened directly as a file) for the Web Speech API to work correctly.

---

## Environment Setup

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## Project Structure

```
Ai-Customer-Support-Bot/
├── backend/        → FastAPI app, API routes
├── rag/            → RAG pipeline, Gemini calls, vector store
├── ml/             → Intent classification model
├── models/         → Saved ML models
├── dataset/        → Training data
├── database/       → Knowledge base source documents
├── voice/          → Voice-related utilities
└── frontend/       → HTML, CSS, JS (UI + Web Speech API)
```

---

## Roadmap

- [ ] Multi-turn conversation memory
- [ ] Human escalation flow for unanswered queries
- [ ] Frontend integration of streaming responses
- [ ] Sentiment/priority-based response handling
- [ ] Cloud deployment




