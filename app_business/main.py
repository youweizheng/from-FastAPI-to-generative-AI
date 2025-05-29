# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import inspect

from app_business.query_table import query_all_cuisines_from_db
from app_business.database import get_business_db

app = FastAPI()

# Initialize variables
table_exists = False

# Function to check if table exists
def check_table_exists():
    db = next(get_business_db())
    inspector = inspect(db.get_bind())
    return "cuisines" in inspector.get_table_names()

# Function to get latest cuisines data
def get_latest_cuisines():
    if table_exists:
        return query_all_cuisines_from_db()
    return []

# Default home page
@app.get("/", response_class=HTMLResponse)
async def home():
    if not table_exists:
        return """
        <!DOCTYPE html>
        <html>
            <head>
                <title>From FastAPI to GenAI Part 01</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                        text-align: center;
                    }
                    h1 {
                        color: #2c3e50;
                        margin-bottom: 10px;
                    }
                    h2 {
                        color: #7f8c8d;
                        font-weight: normal;
                    }
                    .error {
                        color: #e74c3c;
                        margin: 20px 0;
                    }
                </style>
            </head>
            <body>
                <h1>From FastAPI to GenAI Part 01: Business APP</h1>
                <h2>www.youtube.com/@youweizheng</h2>
                <div class="error">
                    <p>The cuisines table does not exist yet. Please run the database migrations first.</p>
                </div>
            </body>
        </html>
        """
    
    # Get latest data on each request
    cuisines = get_latest_cuisines()
    table_rows = "".join([
        f"<tr><td>{c.id}</td><td>{c.name}</td><td>{c.unit_price}</td><td>{c.is_available}</td></tr>" for c in cuisines
    ])
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>From FastAPI to GenAI Part 01</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    color: #2c3e50;
                    margin-bottom: 10px;
                }}
                h2 {{
                    color: #7f8c8d;
                    font-weight: normal;
                }}
                table {{
                    margin: 20px auto;
                    border-collapse: collapse;
                    width: 80%;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px 12px;
                }}
                th {{
                    background: #f4f4f4;
                }}
            </style>
        </head>
        <body>
            <h1>From FastAPI to GenAI Part 01: Business APP</h1>
            <h2>www.youtube.com/@youweizheng</h2>
            <table>
                <tr><th>ID</th><th>Name</th><th>Unit Price</th><th>Available</th></tr>
                {table_rows}
            </table>
        </body>
    </html>
    """

# Initialize table existence check when the application starts
@app.on_event("startup")
async def startup_event():
    global table_exists
    table_exists = check_table_exists()