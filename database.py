from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from vars import env_vars


SQLALCHEMY_DATABASE_URL = f"postgresql://{env_vars.DB_USER}:{env_vars.DB_PASS}@{env_vars.DB_HOST}:{env_vars.DB_PORT}/{env_vars.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()