from pydantic import BaseModel, Field
from datetime import datetime

class BookingBase(BaseModel):
  origin_airport: str
  destination_airport: str

class Booking(BookingBase):
  id: str
  code: str
  created_at: datetime
  customer: 'User'

class BookingCreate(BookingBase):
  customer_id: str

class BookingResponse(BaseModel):
  success: bool
  data: Booking | None
  error: Exception | None
  
from domain.user.schema import User

#cos of the potential cyclic dependencies
Booking.model_rebuild()
