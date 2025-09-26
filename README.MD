# Bookstore API

A RESTful API for managing an online bookstore using FastAPI and SQLite.

## Setup Instructions
1. Clone the repo: `git clone https://github.com/your-username/bookstore-api.git`
2. Create virtual env: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install deps: `pip install -r requirements.txt`
5. Run the API: `uvicorn main:app --reload`
6. Access docs: http://127.0.0.1:8000/docs

## Features
- User registration and authentication
- Book management (CRUD)
- Database persistence

## Git Workflow
- Main: Stable code
- Dev: Integration of features
- Feature branches: For specific developments