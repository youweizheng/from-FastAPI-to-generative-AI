# create_table.py
import models_business
from app_business.database import business_engine

models_business.Base.metadata.create_all(bind=business_engine)