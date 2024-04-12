from domain.booking.schema import Booking, BookingCreate
from domain.booking.repository import IBookingRepository
from domain.booking.model import Booking as BookingModel
from domain.user.model import User as UserModel
from sqlalchemy.orm import Session

class BookingRepository(IBookingRepository):
  def __init__(self, database: Session) -> None:
    self.db = database

  async def create_booking(self, booking_params: BookingCreate) -> Booking:
    booking_model = BookingModel(**booking_params.model_dump())
    self.db.add(booking_model)
    self.db.commit()
    self.db.refresh(booking_model)
    return booking_model
  
  async def fetch_booking_by_code(self, booking_code: str, user_id: str) -> Booking:
    self.db.query(BookingModel).where(
      BookingModel.code == booking_code, BookingModel.user_id == user_id
    ).join(UserModel).order_by(BookingModel.created_at.desc())

  async def fetch_booking_by_id(self, booking_id: str) -> Booking:
    pass
