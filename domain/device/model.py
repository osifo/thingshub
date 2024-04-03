from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from ..base import BaseModel

class Device(BaseModel):
  __tablename__ = "devices"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255), index=True, nullable=False)
  last_location = Column(Geometry('Point'))
  is_active = Column(Boolean)
  owner_id = Column(Integer, ForeignKey("users.id"))
  
  owner = relationship("User", back_populates="devices")
