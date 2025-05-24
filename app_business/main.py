# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app_business.query_table import query_all_cuisines_from_db

app = FastAPI()

cuisines = query_all_cuisines_from_db()

# Default home page
@app.get("/", response_class=HTMLResponse)
async def home():
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