from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from domain.base import BaseModel

class User(BaseModel):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String(255), unique=True, index=True, nullable=False)
  name = Column(String(255))
  hashed_password = Column(String(255))
  is_active = Column(Boolean)
  home_address = Column(String(255))
  
  devices = relationship("Device", back_populates="owner")
