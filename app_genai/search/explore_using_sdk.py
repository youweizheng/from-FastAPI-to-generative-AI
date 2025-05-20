# app_genai/search_using_sdk.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from timescale_vector import client as timescale_client
from app_genai.database import DATABASE_VECTOR_URL

load_dotenv()