from domain.booking.repository import IBookingRepository
from fastapi import HTTPException, status
from domain.booking.schema import BookingCreate, BookingResponse
from api.services import booking as bookingService
from fastapi import APIRouter
import asyncio

def controller(repository: IBookingRepository):
  router = APIRouter(prefix="/bookings", tags="bookings")

  MAX_REQUESTS_PER_SECOND = 5
  rate_limit = asyncio.Semaphore(MAX_REQUESTS_PER_SECOND)

  @router.post("/", summary="create booking", description="this endpoint is rate-limited")
  async def create_booking(booking_param: BookingCreate) -> BookingResponse | HTTPException:
    if rate_limit.locked():
      raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="too many requests, try again later")

    async with rate_limit:
      try:
        booking = repository.create_booking(booking_param)
        if booking:
          return { 'data': booking, 'success': True }
        else:
          raise HTTPException(status_code=400, details="Booking could not be created, please check your params")
      except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)

  return router

    
  
  
