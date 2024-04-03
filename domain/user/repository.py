import abc
from abc import ABC
from sqlalchemy.orm import Session
from domain.user.schema import UserCreate, User

class IUserRepository(ABC):  
  @abc.abstractmethod
  def create_user(self, user_params: UserCreate) -> User:
    """ creates a user """
    raise NotImplementedError
  
  @abc.abstractmethod
  def get_users(self, *filter_param: object) -> list[User]:
    """ return a list of users based on the filter param """
    raise NotImplementedError
  
  @abc.abstractmethod
  def show_user(self, user_id: str) -> User:
    """ returns a user that matches the supplied Id """
    raise NotImplementedError
  

