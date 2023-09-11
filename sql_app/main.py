from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/users/", response_model = schemas.User, status_code = status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail = "Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/api/v1/users/", response_model = list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/api/v1/users/{user_id}", response_model = schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "User not found")
    return user


@app.post("/api/v1/users/{user_id}/items/", response_model = schemas.Item, status_code = status.HTTP_201_CREATED)
def create_user_item(item: schemas.ItemCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, user_id=user_id)


@app.get("/api/v1/items/", response_model = list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items
