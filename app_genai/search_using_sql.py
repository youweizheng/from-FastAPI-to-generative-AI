# app_genai/search_using_sql.py

import os
import psycopg2
from dotenv import load_dotenv
from app_genai.database import DATABASE_VECTOR_URL

load_dotenv()


def semantic_search_sql(
    query: str,
    limit_results: int, 
    table_name: str,    
    column_name: str = "contents",
    embedding_model: str = "text-embedding-3-small",
    similarity_threshold: float = 0.7):
    """
    Perform a semantic search on a table column using a query.

    Args:
        query (str): The search query.
        limit_results (int): The number of results to return.
        table_name (str): The name of the table to search.
        column_name (str): The name of the column to search.
        similarity_threshold (float): The similarity threshold for the search.
    Returns:
        str: The SQL query to perform the semantic search.
    """

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(DATABASE_VECTOR_URL)
    cursor = connection.cursor()

    # Set up OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # Set the API key in the database
    cursor.execute(f"SELECT set_config('ai.openai_api_key', '{api_key}', false);")
    connection.commit()

    # Construct the SQL query for semantic search
    sql_query = f"""
        SELECT id, {column_name}, 
            (embedding <=> (
                SELECT ai.openai_embed(
                    '{embedding_model}',
                    '{query}'
                )
            )
        ) as similarity
        FROM {table_name}
        WHERE (embedding <=> (
                SELECT ai.openai_embed(
                    '{embedding_model}',
                    '{query}'
                )
            )
        ) > {similarity_threshold}
        ORDER BY similarity DESC
        LIMIT {limit_results};
    """

    # Execute the SQL query
    cursor.execute(sql_query)
    results = cursor.fetchall()

    # Print how many results were returned
    print(f"Found {len(results)} results")

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return results


# Test the semantic search function
if __name__ == "__main__":
    query = "What is Mapo Tofu?"
    limit_results = 2
    table_name = "cuisines_vector"
    results = semantic_search_sql(query, limit_results, table_name)
    
    # Print results in a more readable format
    for result in results:
        id, content, similarity = result
        print(f"\nID: {id}")
        print(f"Content: {content}")
        print(f"Similarity: {similarity:.4f}")