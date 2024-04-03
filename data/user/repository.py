import bcrypt
from fastapi import Depends
from sqlalchemy.orm import Session 
from config import get_database
from domain.user.repository import IUserRepository
from domain.user.schema import User as UserSchema, UserCreate as UserCreateSchema
from domain.user.exceptions import UserInvalidError
from domain.user.model import User as UserModel


class UserRepository(IUserRepository):
  def __init__(self) -> None:
    self.database = next(get_database())

  async def create_user(self, user_params: UserCreateSchema) -> UserSchema:
    try:
      hashed_password = bcrypt.hashpw(user_params.password.encode('utf-8'), bcrypt.gensalt())
      new_user = UserModel(
        **user_params.model_dump(exclude=['password']), 
        # **user_params.model_dump(exclude=['password']), 
        hashed_password=hashed_password
      )
      
      if not new_user:
        raise UserInvalidError
      
      self.database.add(new_user)
      self.database.commit()
      self.database.refresh(new_user)
      return new_user
    
    except Exception as error:
      # handle logging here
      raise error
  
  async def show_user(self, user_id: str) -> UserSchema:
    user = self.database.query(UserModel).get(user_id)
    print(f"user ========== {user}")

    if not user:
      raise UserInvalidError
    return user
  
  def get_users(self, *filter_param: object) -> list[UserSchema]:
    users = self.database.query(UserModel).all()
    return users
