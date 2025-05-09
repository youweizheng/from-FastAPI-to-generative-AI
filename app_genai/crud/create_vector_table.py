# app_genai/crud/create_vector_table.py
import psycopg
import os
from app_genai.database import DATABASE_VECTOR_URL
from dotenv import load_dotenv

load_dotenv()

def create_vector_table(conn: psycopg.Connection):
    with conn.cursor() as cur:    
        cur.execute("""
            SELECT ai.create_vectorizer(
                'cuisines_content'::regclass,
                if_not_exists => true,
                loading => ai.loading_column(column_name=>'contents'),
                embedding => ai.embedding_openai(model=>'text-embedding-ada-002', dimensions=>'1536', api_key=>%s),
                destination => ai.destination_table(view_name=>'cuisines_content_embedding')
            )
        """, (os.getenv('OPENAI_API_KEY'),))   
    conn.commit()
    
if __name__ == "__main__":
    import pgai
    pgai.install(DATABASE_VECTOR_URL)

    conn = psycopg.connect(DATABASE_VECTOR_URL)
    create_vector_table(conn)