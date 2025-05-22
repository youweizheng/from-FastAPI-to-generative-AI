# app_genai/chatbot.py
from app_genai.search.search_using_sdk import simiarity_search_sdk

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"

def chatapi(query: str) -> str:
    """
    Chat function that uses similarity search to find the most relevant content.
    """

    # Prepare context from search results
    context = simiarity_search_sdk(query)

    # Generate response
    response = openai_client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "developer",
                "content": "You are a helpful assistant that answers user's questions based ONLY on the provided context."
            },
            {
                "role": "user",
                "content": f"""
                    Question: {query}
                    Context: {context}
                    """
            }
        ]
    )

    return response.output_text


if __name__ == "__main__":
    print(chatapi("What is the price of Mapo Tofu?"))