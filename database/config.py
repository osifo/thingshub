import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

_db_url = URL.create(
  "mysql+pymysql",
  username=os.getenv("DB_USERNAME"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_NAME"),
  port=os.getenv("DB_PORT")
)
_db_engine = create_engine(_db_url)

DBSession = sessionmaker(autoflush=False, bind=_db_engine)

def get_database():
  db = DBSession()

  try:
    yield db
  finally:
    db.close()
