from sqlalchemy.orm import Session
from .models import User, Book
from .schemas import UserCreate, BookCreate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError, NoResultFound
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    try:
        return db.query(User).filter(User.username == username).one()  # Use .one() to raise NoResultFound
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

def create_user(db: Session, user: UserCreate):
    try:
        hashed_password = pwd_context.hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()  # Undo partial changes if unique constraint fails
        raise HTTPException(status_code=400, detail="Username or email already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def create_book(db: Session, book: BookCreate):
    try:
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Book already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def get_books(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(Book).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

def get_book(db: Session, book_id: int):
    try:
        book = db.query(Book).filter(Book.id == book_id).one()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query error: {str(e)}")

def update_book(db: Session, book_id: int, book: BookCreate):
    try:
        db_book = get_book(db, book_id)  
        if db_book:
            db_book.title = book.title
            db_book.author = book.author
            db_book.price = book.price
            db_book.stock = book.stock
            db.commit()
            db.refresh(db_book)
            return db_book
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Update conflict: Book data already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    return None  

def delete_book(db: Session, book_id: int):
    try:
        db_book = get_book(db, book_id)  
        if db_book:
            db.delete(db_book)
            db.commit()
            return db_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    return None

