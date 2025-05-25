# main.py
from fastapi import FastAPI
from pydantic import BaseModel

from app_business.models_business import Cuisine
from app_business.database import business_db_dependency

# Pydantic model for request
class CuisineCreate(BaseModel):
    name: str
    description: str
    unit_price: int
    is_available: bool

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the tutorial Part 01: From FastAPI to GenAI"}

@app.post("/cuisines/add")
def create_cuisine(cuisine: CuisineCreate, db: business_db_dependency):
    db_cuisine = Cuisine(**cuisine.model_dump())
    db.add(db_cuisine)
    db.commit()
    db.refresh(db_cuisine)
    return db_cuisine

@app.get("/cuisines/get")
def get_cuisines(db: business_db_dependency):
    return db.query(Cuisine).all()