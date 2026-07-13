from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ml.predict import predict_intent
from rag.chatbot import ask_chatbot, ask_chatbot_stream

app = FastAPI(title="AI Customer Support API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Customer Support API Running"}


@app.post("/chat")
def chat(request: ChatRequest):
    intent = predict_intent(request.message)
    response = ask_chatbot(request.message)
    return {
        "intent": intent,
        "response": response
    }


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    return StreamingResponse(
        ask_chatbot_stream(request.message),
        media_type="text/plain"
    )