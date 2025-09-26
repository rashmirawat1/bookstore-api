# Bookstore API

A RESTful API for managing an online bookstore using FastAPI and SQLite.

## Setup Instructions
1. Clone the repo: `git clone https://github.com/rashmirawat1/bookstore-api.git`
2. Create virtual env: `python -m venv env`
3. Activate: `env\Scripts\activate` (Windows)
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

## API Endpoints
| Endpoint       | Method | Description                  | Auth Required |
|----------------|--------|------------------------------|---------------|
| /users/       | POST   | Register user                | No            |
| /users/token  | POST   | Login for token              | No            |
| /books/       | POST   | Create book                  | Yes           |
| /books/       | GET    | List books                   | No            |
| /books/{id}   | GET    | Get book                     | No            |
| /books/{id}   | PUT    | Update book                  | Yes           |
| /books/{id}   | DELETE | Delete book                  | Yes           |

## Running Tests
Run `pytest` in the root.

## Screenshots

### Bookstore-API
![Swagger1](screenshots/Screenshot-1.png)  
![Swagger2](screenshots/Screenshot-2.png)
![Swagger3](screenshots/Screenshot-3.png)

## Postman Testing
![Swagger4](screenshots/Screenshot-4.png)