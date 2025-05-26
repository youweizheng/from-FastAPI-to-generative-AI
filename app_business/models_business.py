# models_business.py
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cuisine(Base):
    __tablename__ = "cuisines"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    unit_price = Column(Integer, index=True, nullable=False)
    is_available = Column(Boolean, index=True, nullable=False)
    instock = Column(Integer, index=True, nullable=False, default=0)  # Column for inventory tracking
    rating = Column(Float, index=True, nullable=False, default=0.0)  # Default rating of 0.0
    
    def __repr__(self):
        return f"<Cuisine(id={self.id}, name={self.name}, unit_price={self.unit_price}, is_available={self.is_available}, instock={self.instock}, rating={self.rating})>"
    
