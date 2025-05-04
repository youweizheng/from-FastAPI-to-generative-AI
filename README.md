# From FastAPI to generative AI
This comprehensive tutorial is divided into four parts that will guide you through using generative AI tools to seamlessly integrate AI capabilities into your business applications.

## Codebase setup
This helps you setup the codebase in order to run the app as demonstrated in the video which includes Virtual Environment, Docker and .env etc.

### Virtual Environment
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
