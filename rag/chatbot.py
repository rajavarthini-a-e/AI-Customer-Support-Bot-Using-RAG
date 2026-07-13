import sys
import os
import time

# Allow Python to access project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
from google import genai
from google.genai import types

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from ml.predict import predict_intent

# ==========================
# Load API Key
# ==========================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

# ==========================
# Load Embedding Model
# ==========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================
# Load FAISS Database
# ==========================

db = FAISS.load_local(
    "rag/vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# ==========================
# Chat Function
# ==========================

def _build_prompt(question):
    intent = predict_intent(question)

    docs = db.similarity_search(question, k=2)

    context = ""
    for doc in docs:
        context += doc.page_content + "\n\n"

    prompt = f"""
You are an AI Customer Support Assistant.

Detected Intent:
{intent}

Company Information:
{context}

Customer Question:
{question}

Instructions:

- Answer ONLY using the company information.
- Be professional and polite.
- If the answer is unavailable, reply:
"I couldn't find that information in our knowledge base."
"""
    return intent, prompt


THINKING_CONFIG = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="minimal")
)


def ask_chatbot(question):
    start = time.time()

    intent, prompt = _build_prompt(question)
    t1 = time.time()
    print(f"[TIMING] Intent + retrieval:     {t1 - start:.2f}s")

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config=THINKING_CONFIG
    )
    t2 = time.time()
    print(f"[TIMING] Gemini API call:       {t2 - t1:.2f}s")
    print(f"Response Time: {t2 - start:.2f} seconds")

    return response.text


def ask_chatbot_stream(question):
    start = time.time()

    intent, prompt = _build_prompt(question)
    t1 = time.time()
    print(f"[TIMING] Intent + retrieval:     {t1 - start:.2f}s")

    first_chunk_time = None

    for chunk in client.models.generate_content_stream(
        model="gemini-flash-latest",
        contents=prompt,
        config=THINKING_CONFIG
    ):
        if chunk.text:
            if first_chunk_time is None:
                first_chunk_time = time.time()
                print(f"[TIMING] Time to first chunk:   {first_chunk_time - t1:.2f}s")
            yield chunk.text

    end = time.time()
    print(f"[TIMING] Total stream time:      {end - start:.2f}s")


# ==========================
# Test from Terminal
# ==========================

if __name__ == "__main__":
    print("=" * 60)
    print("AI CUSTOMER SUPPORT CHATBOT")
    print("=" * 60)

    while True:
        question = input("\nAsk your question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        print("\nDetected Intent:", predict_intent(question))
        print("\nAI Response:\n")
        print(ask_chatbot(question))