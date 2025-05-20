# app_genai/search_using_sdk.py

from typing import List, Tuple
import os
from openai import OpenAI
from dotenv import load_dotenv
from timescale_vector import client as timescale_client
from app_genai.database import DATABASE_VECTOR_URL

load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"

# Initialize Timescale Vector client
timescale_vector_client = timescale_client.Sync(
    service_url=DATABASE_VECTOR_URL,
    table_name="cuisines_vector",
    num_dimensions=1536,  # OpenAI text-embedding-3-small dimension
    time_partition_interval=None  # No time partitioning needed
)

def simiarity_search_sdk(
    query: str,
    limit: int = 1,
) -> List[Tuple[str, float]]:
    """
    Search for similar content using Timescale Vector SDK.

    Args:
        query: The search query
        limit: Number of results to return
        
    Returns:
        List of tuples containing (content, similarity_score)
    """
    print(f"\nStep 1: Searching for similar content using Timescale Vector SDK (limit={limit})")
    
    try:
        # Get the embedding for the query
        response = openai_client.embeddings.create(    
            model="text-embedding-3-small",
            input=query
        )
        query_embedding = response.data[0].embedding
        
        # Search using Timescale Vector SDK
        results = timescale_vector_client.search(
            query_embedding=query_embedding,
            limit=limit
        )
        
        # Format results into tuples of (content, similarity_score)
        # results format: [(id, metadata, contents, embedding, similarity), ...]
        formatted_results = [
            (result[2], result[4])  # contents is at index 2, similarity at index 4
            for result in results
        ]
        
        print(f"Found {len(formatted_results)} similar results")
        for idx, (content, similarity) in enumerate(formatted_results, 1):
            print(f"\nResult {idx}: (similarity: {similarity:.4f}):")
            print(f"Content: {content[:100]}...")  # Print first 100 chars
        
        return formatted_results
        
    except Exception as e:
        raise RuntimeError(f"Failed to execute similarity search: {str(e)}") from e


# Test the semantic search function
if __name__ == "__main__":
    query = "I want to eat Kung Pao Chicken"
    limit_results = 2
    results = simiarity_search_sdk(query, limit_results)
