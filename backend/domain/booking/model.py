from sqlalchemy import (
  event,
  Column, 
  String, 
  Integer, 
  DateTime, 
  ForeignKey,
  UniqueConstraint,
  CheckConstraint
  )
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from domain.base import BaseModel
import string, random

class Booking(BaseModel):
  __tablename__ = 'bookings'

  id = Column(Integer, primary_key=True, index=True);
  code = Column(String(10), index=True, nullable=False)
  destination_airport = Column(String(255), nullable=False),
  origin_airport = Column(Geometry(geometry_type='POINT'), nullable=False)
  customer_id = Column(Integer, ForeignKey("users.id"))
  created_at = Column(DateTime, index=True, nullable=False)
  customer = relationship("User", back_populates="bookings")

  # origin = Column(Geometry(geometry_type='POINT'), nullable=False)

  __table_args__ = (
    UniqueConstraint('code', 'customer_id', name='unique_user_pnrcode'),
  )

@event.listens_for(Booking, 'before_insert')
def generate_pnr_code(_mapper, _connection, target):
  code_length = 6
  pnr_code = []

  for _ in range(code_length):
    pnr_code.append(random.choice(string.ascii_uppercase + string.digits))
  target.code = ''.join(pnr_code)




    