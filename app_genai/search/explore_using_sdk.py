# app_genai/search_using_sdk.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from timescale_vector import client as timescale_client
from app_genai.database import DATABASE_VECTOR_URL

load_dotenv()

# Step 01: Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
embedding_model = "text-embedding-3-small"

# Step 02: Initialize Timescale Vector client
timescale_vector_client = timescale_client.Sync(
    service_url=DATABASE_VECTOR_URL,
    table_name="cuisines_vector",
    num_dimensions=1536,  # OpenAI text-embedding-3-small dimension
    time_partition_interval=None  # No time partitioning needed
)

# Step 03: Create embedding for query
query = "What is Mapo Tofu?"

embedding_response = openai_client.embeddings.create(
    model=embedding_model,
    input=query
)

print(embedding_response.data[0].embedding)

# Step 04: Search for similar content using Timescale Vector SDK
results = timescale_vector_client.search(
    query_embedding=embedding_response.data[0].embedding,
    limit=2
)

# Step 05: Format results into tuples of (content, similarity_score)
formatted_results = [
    (result[2], result[4])  # contents is at index 2, similarity at index 4
    for result in results
]

for content, similarity in formatted_results:
    print(f"Content: {content}, Similarity Score: {similarity}")