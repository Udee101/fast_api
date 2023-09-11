from sqlalchemy.orm import Session
from . import models, schemas



def get_users(db: Session):
  return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
  return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
  fake_hashed_password = user.password + "notReallyHashed"
  db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


def get_items(db: Session):
  return db.query(models.Item).all()


def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
  db_item = models.Item(**item.model_dump(), owner_id=user_id)
  db.add(db_item)
  db.commit()
  db.refresh(db_item)
  return db_item

