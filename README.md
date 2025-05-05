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

### Part 01
- Create new branch
```bash
>> git checkout -b part01
Switched to a new branch 'part01'
```

- Create **app** folder and `main.py`
```bash
>> cd app
>> uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Create *Docker* folder and files
01. Create a folder called `docker`<br>
02. Create a file called `Dockerfile.app`<br>
03. Create a file called `docker-compose.yml`<br>

- Run **app** with *Docker*
```bash
>> docker compose -f docker/docker-compose-base.yml up -d --build
```

- Create `models_business.py` to model business data
- Run **app** and **business database** with *Docker*
```bash
>> docker compose -f docker/docker-compose-business.yml up -d --build
```
- Create `create_table.py`
- Create `insert_table.py`
