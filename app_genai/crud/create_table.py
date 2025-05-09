# create_table.py
import app_genai.models_vector as models_vector
from app_genai.database import vector_engine

models_vector.Base.metadata.create_all(bind=vector_engine)
print("Table created successfully")