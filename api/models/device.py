from pydantic import BaseModel, Field

class ReadModel(BaseModel):
  name: str
  last_location: tuple[str, str] = Field(min_length=2, max_length=2)
  user_id: str

class WriteModel(BaseModel):
  name: str
  last_location: tuple[str, str]
  user_id: str