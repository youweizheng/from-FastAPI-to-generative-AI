# app_genai/database.py
from typing import Annotated

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi import Depends

# vector database
DATABASE_VECTOR_URL = "postgresql://youwei:fromfastapi2genai@localhost:5119/vector"
vector_engine = create_engine(DATABASE_VECTOR_URL)
VectorSessionMaker = sessionmaker(
    autocommit=False, autoflush=False, bind=vector_engine
)


def get_vector_db():
    db_session = VectorSessionMaker()
    try:
        yield db_session
    finally:
        db_session.close()


vector_db_dependency = Annotated[Session, Depends(get_vector_db)]
