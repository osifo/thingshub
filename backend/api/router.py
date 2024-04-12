from fastapi import FastAPI
from api.routes import devices, users, bookings
from data.device.repository import DeviceRepository
from data.user.repository import UserRepository
from data.booking.repository import BookingRepository
from sqlalchemy.orm import Session

class AppRouter():
  @staticmethod
  def setup(app: FastAPI, dbConnection: Session) -> None:
    deviceRepo = DeviceRepository(database=dbConnection)
    userRepo = UserRepository(database=dbConnection)
    bookingRepo = BookingRepository(database=dbConnection)


    devices_controller = devices.controller(deviceRepo) 
    users_controller = users.controller(userRepo, deviceRepo) 
    booking_controllers = bookings.controller(bookingRepo)

    app.include_router(users_controller)
    app.include_router(devices_controller)
    app.include_router(booking_controllers)

    return app

  