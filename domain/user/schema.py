from pydantic import BaseModel
from domain.device.schema import Device

class UserBase(BaseModel):
  name: str
  email: str
  home_address: str | None

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: str
  is_active: bool
  devices: list[Device]
  
