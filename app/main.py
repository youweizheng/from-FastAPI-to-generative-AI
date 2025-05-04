# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the tutorial Part 01: From FastAPI to OpenAI"}