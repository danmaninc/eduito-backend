from sqlalchemy import Integer, String, Boolean
from database import Base
from sqlalchemy.orm import mapped_column

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String, unique=True, index=True)
    email = mapped_column(String, unique=True, index=True)
    password = mapped_column(String)
    is_verified = mapped_column(Boolean, default=False)
    balance = mapped_column(Integer, default=0)
