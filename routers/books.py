from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import SessionLocal
from ..crud import create_book, get_books, get_book, update_book, delete_book
from ..schemas import Book, BookCreate, User
from .users import oauth2_scheme 
from .users import get_current_user 

router = APIRouter(prefix="/books", tags=["books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db=db, book=book)

@router.get("/", response_model=list[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db=db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_book = update_book(db=db, book_id=book_id, book=book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", response_model=Book)
def delete_existing_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_book = delete_book(db=db, book_id=book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book


