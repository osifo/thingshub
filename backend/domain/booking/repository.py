from abc import ABC, abstractmethod
from .schema import BookingCreate, Booking

class IBookingRepository(ABC):
  @abstractmethod
  def create_booking(self, bookingDetails: BookingCreate) -> Booking:
    """implements creating a new booking"""
    raise NotImplementedError
  
  def fetch_booking_by_code(self, booking_code: str, user_id: str) -> Booking:
    """fetches a booking code linked to a user"""
    raise NotImplementedError
  
  def fetch_booking_by_id(self, booking_id: str) -> Booking:
    """fetches a booking code linked to a user"""
    raise NotImplementedError