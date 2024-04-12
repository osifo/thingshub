from faker import Faker
from domain.user.model import User
from sqlalchemy.orm import Session
from pytest import fixture

def user():
  faker = Faker()
  name = faker.user_name()
  email = faker.email()
  home_address = faker.address()

  return {
    'name': name,
    'email': email,
    'home_address': home_address
  }

# @fixture
async def create_user(db: Session):
  user_model = User(**user())
  db.add(user_model)
  db.commit()
  db.refresh(user_model)

  return user_model

