from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import selectin_polymorphic, sessionmaker

SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_threads": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()