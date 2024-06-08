from fastapi import FastAPI, Depends, HTTPException
import crud
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users", response_model=schemas.UserCreateResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user=schemas.UserCreate(
        username=user.username,
        email=user.email,
        password=user.password)
                            )

@app.get("/users", response_model=schemas.UserGetResponse)
def get_user(user: schemas.UserGet, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Not found")
    return db_user
