# ai_genai/models_vector.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CuisinesContent(Base):
    __tablename__ = "cuisines_content"

    id = Column('id', Integer, primary_key=True, index=True)
    metadata_value = Column('metadata', String)
    contents = Column('contents', String)
    
    def __repr__(self):
        return f"<CuisineContent(id={self.id}, metadata_value={self.metadata_value}, contents={self.contents})>"
