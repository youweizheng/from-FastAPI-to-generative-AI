# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app_fastapi.routers import chatgpt

import os
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

# Include routers
app.include_router(chatgpt.router)

# Default home page
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>From FastAPI to GenAI Part 04</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                h1 {
                    color: #2c3e50;
                    margin-bottom: 10px;
                }
                h2 {
                    color: #7f8c8d;
                    font-weight: normal;
                }
            </style>
        </head>
        <body>
            <h1>From FastAPI to GenAI Part 04: ChatGPT API</h1>
            <h2>www.youtube.com/@youweizheng</h2>
        </body>
    </html>
    """