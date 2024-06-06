import hashlib
from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed = hashlib.sha256(user.password.encode("utf-8")).hexdigest()
    db_user = models.User(username=user.username, email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
