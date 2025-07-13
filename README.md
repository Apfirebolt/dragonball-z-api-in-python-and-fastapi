# Dragonball Z API using Python and FAST API

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Poetry](https://img.shields.io/badge/Poetry-181118?style=for-the-badge&logo=poetry&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Dragonball Z is a popular anime series featuring powerful warriors, epic battles, and a rich universe of characters. This API provides programmatic access to Dragonball Z data, allowing you to retrieve information about characters, sagas, transformations, and more.

![Project Image](https://static.wikia.nocookie.net/dragonball/images/2/23/Migatte_no_Gokui_Kizashi.png/revision/latest/scale-to-width-down/1200?cb=20181017065922)

This project was using venv with requirements.txt. It has been configured to use Poetry for package management and virtual environment.

## Steps to include Poetry for package management

### deactivate previous virtual environment

- rm -rf venv

### 1. Initialize Poetry (if not already done)

poetry init

### 2. Import main dependencies

poetry add $(cat requirements.txt | sed '/^\s*$/d' | sed '/^#/d')

### 3. Install all dependencies (if not already installed by `poetry add`)
poetry install

### 4. Install individual dependency

- poetry add fastapi-pagination  
- poetry add sqlalchemy psycopg2-binary 

### . Run your project and additional commands

- poetry run python main.py

- poetry run alembic revision --autogenerate -m "Added initial tables"

- poetry run alembic upgrade head

## Getting started

Create an env file with database related settings

```
DATABASE_USER=postgres
DATABASE_PASSWORD=pass123
DATABASE_HOST=localhost
# DATABASE_HOST=db
DATABASE_NAME=dbz-api
```

Install packages using the Poetry commands described above. Visit the docs of the application

http://localhost:8000/docs

Execute POST request to populate data from CSV file.

```
poetry add --dev pytest coverage httpx
```

## Updates

- Added RabbitMQ sample connection

