from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from vars import vars


SQLALCHEMY_DATABASE_URL = f"postgresql://{vars.DB_USER}:{vars.DB_PASS}@{vars.DB_HOST}:{vars.DB_PORT}/{vars.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()