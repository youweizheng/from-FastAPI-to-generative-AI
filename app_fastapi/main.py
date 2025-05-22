# main.py
from fastapi import FastAPI
from routers import chat

import os
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()
# Include routers
app.include_router(chat.router)

@app.get("/")
async def home():
    return {"message": "From FastAPI to GenAI Part 04: Chatbot API"}