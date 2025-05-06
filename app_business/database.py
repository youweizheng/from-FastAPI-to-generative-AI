# client_database.py
from typing import Annotated

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi import Depends

# business database
DATABASE_BUSINESS_URL = "postgresql://youwei:fromfastapi2genai@localhost:5118/business"
business_engine = create_engine(DATABASE_BUSINESS_URL)
BusinessSessionMaker = sessionmaker(
    autocommit=False, autoflush=False, bind=business_engine
)


def get_business_db():
    db_session = BusinessSessionMaker()
    try:
        yield db_session
    finally:
        db_session.close()


business_db_dependency = Annotated[Session, Depends(get_business_db)]
