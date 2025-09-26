from fastapi import FastAPI
from .routers import users, books

app = FastAPI(title="Bookstore API", description="API for bookstore management")

app.include_router(users.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bookstore API"}