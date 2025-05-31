# From FastAPI to generative AI
This comprehensive tutorial is divided into four parts that will guide you through using generative AI tools to seamlessly integrate AI capabilities into your business applications.

## Virtual Environment
I use uv from astral to setup virtual environment und make sure you update uv to the latest version. 

- This project runs uv v0.7.2
```bash
>> uv self update
info: Checking for updates...
success: Upgraded uv from v0.6.10 to v0.7.2! https://github.com/astral-sh/uv/releases/tag/0.7.2
```

- This project runs Python 3.12.8
```bash
>> uv run python
Python 3.12.8 (main, Jan  5 2025, 06:55:30) [Clang 19.1.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

- Initialize virtual environment
```bash
>> mkdir your-project-name
>> uv init --no-workspace
Initialized project `your-project-name`
```

- Create virtual environment and print hello message
```bash
>> uv run main.py
Using CPython 3.12.8
Creating virtual environment at: .venv
Hello from `your-project-name`!
```

- Install dependencies
```bash
>> uv pip install -r requirements.txt
Resolved 31 packages in 2.66s
Prepared 10 packages in 1.41s
Installed 31 packages in 61ms
```

## Codebase setup
This helps you setup the codebase in order to run the app as demonstrated in the video which includes Virtual Environment, Docker and .env etc.

### Part 01: You don't even need vector database
- Create new branch
```bash
>> git checkout -b part01
Switched to a new branch 'part01'
```

- Create **app** folder and `main.py`
```bash
>> cd app_business
>> uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Create *Docker* folder and files
01. Create a folder called `docker`<br>
02. Create a file called `Dockerfile.app`<br>
03. Create a file called `docker-compose-business.yml`<br>

- Run **app** and **business database** with *Docker*
```bash
docker compose -f docker/docker-compose-business.yml up -d --build
```

- Run without **app** with *Docker*
```bash
docker-compose -f docker/docker-compose-genai.yml up -d --scale app_business=0
```

- Run **app** independently with *Docker*
```bash
docker-compose -f docker/docker-compose-genai.yml up -d app_business
```


- Create `models_business.py` to model business data
- Create `create_table.py` and run
- Create `insert_table.py` and run

- To run the business app directly from CLI
```bash
>> uv run uvicorn app_business.main:app --host 0.0.0.0 --port 8000 --reload
```

### Part 02: The only bridge you need is pagi
- Run **vector database** and **vectorizer worker** with *Docker*
```bash
>> docker compose -f docker/docker-compose-genai.yml up -d --build
```

- Create *content table* via `create_content_table.py`
- Migrate data from business to content table via `migrate_table.py`
- Create *vector table* via `create_vector_table.py`

### Part 03: Search vector table using sdk
- To re-create all the tables, you need to run:
```bash
docker compose -f docker/docker-compose-genai.yml down -v
```

- Create `explore_using_sdk.py` and demo
- Create `search_using_sdk.py` and run examples

### Part 04: Bring pieces together.
- Use openai responses api to create chat function
- Run app_fastapi endpoint locally
```bash
uv run uvicorn app_fastapi.main:app --host 0.0.0.0 --port 8008 --reload
```
- Exercise: make app_fastapi integrated in the Docker

### Part 05: Streamlit as frontend
```bash
uv run streamlit run frontend/app.py
```