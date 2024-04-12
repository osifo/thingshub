import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from typing import Literal, NewType

load_dotenv()

class DatabaseConfig():
  def __init__(self, connection, session, engine) -> None:
    self.connection = connection
    self.session = session
    self.engine = engine

class Config:
  ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS').split(',')
  APP_ENV = os.getenv("APP_ENV")

  def __get_database_url( env: str):
    print(f"Config env ===== {env}")
    if env == 'development':
      return URL.create(
        "mysql+pymysql",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
      )
    if env == 'test':
      return 'sqlite:///./tests/utils/thingshub.db'

  @staticmethod
  def get_database(env: Literal['test', 'development', 'staging', 'production']):
    db_url = Config.__get_database_url(env)
    db_engine = create_engine(db_url)
    DBSession = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    db_connection = DBSession()

    try:
      yield DatabaseConfig(db_connection, DBSession, db_engine) 
    finally:
      db_connection.close()

