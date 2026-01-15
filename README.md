# FastAPI TODO Project

A production-ready backend service built with FastAPI, PostgreSQL, and async SQLAlchemy.
The project follows Clean Architecture principles with a clear separation between API, business logic, and data access layers.

## Overview

This service provides:

* User authentication using JWT
* Secure password hashing
* Async database access
* Scalable and testable project structure

The codebase is designed to be easy to maintain, extend, and test in real-world environments.

## Technology Stack

* FastAPI
* PostgreSQL
* SQLAlchemy (Async)
* Pydantic
* JWT (python-jose)
* Passlib (bcrypt)
* Uvicorn

### Project Structure

```text
app/
├── main.py                # Application entry point
├── config/db.py            # Async database engine and session
├── config/                 # Configuration and security
├── models/                # Database models
├── schemas/               # Request and response schemas
├── routers/               # API routes (HTTP layer)
├── services/              # Business logic
```

## Architecture

The application follows a layered architecture:

* **Router layer**
  Handles HTTP requests and responses

* **Service layer**
  Contains all business logic and validations

* **Data layer**
  SQLAlchemy models and database access

Routers never access the database directly. All database interactions go through services.

### Setup Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/abhishekk75way/training-fastapi.git
cd training-fastapi
```

#### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### Configuration

Set environment variables in `config/db.py` or via `.env`:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/todo_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database

Ensure PostgreSQL is running and the database exists:

```sql
CREATE DATABASE todo_db;
```

### Running the Application

```bash
uvicorn app.main:app --reload
```

### Authentication

#### Register

```http
POST /auth/register
```

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

#### Login

```http
POST /auth/login
```

Response:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

### Authorized Requests

Include the token in the header:

```http
Authorization: Bearer <jwt_token>
```

### TODO API

#### Create TODO (Authenticated)

```http
POST /todos/
Authorization: Bearer <token>
```
