import datetime
from pydantic import BaseModel, Field

class UserReadModel(BaseModel):
  name: str
  email: str
  birthdate: datetime
  address: str | None = Field(None, description="Where you do live")

class UserWriteModel(UserReadModel):
  password: str = Field(min_length=8, regex="\d+\w+")
