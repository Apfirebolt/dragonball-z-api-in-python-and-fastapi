# Dragonball Z API using Python and FAST API

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

# Optional: Clean up old venv
# deactivate
# rm -rf venv

# 1. Initialize Poetry (if not already done)
poetry init

# 2. Import main dependencies
poetry add $(cat requirements.txt | sed '/^\s*$/d' | sed '/^#/d')

# 3. Import development dependencies (if you had a dev-requirements.txt)
# poetry add $(cat dev-requirements.txt | sed '/^\s*$/d' | sed '/^#/d') --group dev

# 4. Remove old requirements file
rm requirements.txt

# 5. Install all dependencies (if not already installed by `poetry add`)
poetry install

# 6. Run your project
poetry run python your_app.py

