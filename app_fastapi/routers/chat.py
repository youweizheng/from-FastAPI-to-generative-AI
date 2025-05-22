# app_fastapi/routers/chat.py
from fastapi import APIRouter
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app_genai.chatbot import chat

router = APIRouter()

@router.get("/chat")
async def chat_endpoint(query: str):
    return chat(query)

