# app_genai/crud/create_vector_table.py
import psycopg
from app_genai.database import DATABASE_VECTOR_URL
from dotenv import load_dotenv

load_dotenv()

def create_vector_table(conn: psycopg.Connection):
    with conn.cursor() as cur:
        # First, ensure the required extensions are installed
        cur.execute("CREATE EXTENSION IF NOT EXISTS plpython3u;")
        cur.execute("CREATE EXTENSION IF NOT EXISTS ai;")
        conn.commit()
        
        # Then create the vector table
        cur.execute("""
            SELECT ai.create_vectorizer(
                'cuisines_content'::regclass,
                if_not_exists => true,
                loading => ai.loading_column(column_name=>'contents'),
                embedding => ai.embedding_openai(
                    model => 'text-embedding-ada-002',
                    dimensions => 1536,
                    api_key_name => 'OPENAI_API_KEY'
                ),
                destination => ai.destination_table(view_name=>'cuisines_vector')
            )
        """)   
    conn.commit()
    
if __name__ == "__main__":
    import pgai
    pgai.install(DATABASE_VECTOR_URL)

    conn = psycopg.connect(DATABASE_VECTOR_URL)
    create_vector_table(conn)