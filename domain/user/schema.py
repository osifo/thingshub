from pydantic import BaseModel, EmailStr, Field
from domain.device.schema import Device


class UserBase(BaseModel):
  name: str = Field(min_length=5)
  email: EmailStr
  home_address: str | None

class UserCreate(UserBase):
  password: str = Field(min_length=8, pattern='\d+\w+')

class User(UserBase):
  id: str
  is_active: bool | None
  devices: list[Device]

class UserHTTPResponse(BaseModel):
  success: bool
  data: User
class UserListHTTPResponse(BaseModel):
  success: bool
  data: list[User]

  class Config:
    from_attributes = True
  
