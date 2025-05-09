from openai import OpenAI
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os
from pathlib import Path
import sys
from database import BusinessSessionMaker
from query_table import query_all_cuisines

load_dotenv()

# Add app_business to Python path
project_root = Path(__file__).parent.parent
app_business_path = str(project_root / "app_business")
sys.path.append(app_business_path)

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"


def generate_answer(query: str, db_session: Session) -> str:
    """
    Generate an answer using OpenAI based on the query and search results.

    Args:
        query: The original question
        results: List of tuples containing (content, similarity_score)

    Returns:
        Generated answer from OpenAI
    """

    # Prepare context from search results
    context = query_all_cuisines(db_session)

    print(f"Generating answer using {MODEL}")
    messages = [
        {
            "role": "developer",
            "content": "You are a helpful assistant that answers questions based on the provided context.",
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}\n\nPlease provide a concise answer based on the context.",
        },
    ]

    response = openai_client.responses.create(
        model=MODEL, input=messages, temperature=0.7, max_output_tokens=1000
    )

    answer = response.output_text
    print("\nGenerated Answer:")
    print(answer)
    return answer


if __name__ == "__main__":
    # Create a new database session
    db_session = BusinessSessionMaker()

    # Get user input for query and limit
    query = input("Enter your question: ")

    try:
        generate_answer(query, db_session)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise
