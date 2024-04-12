from faker import Faker
from pytest import fixture
import random
from domain.device.model import Device
from sqlalchemy.orm import Session
from .users import create_user


def device():
  faker = Faker()
  name = faker.name()

  return {
    "name": name
  }

async def create_device(db: Session, owner_id: str = random.randint(1,50)):
  new_device = device()
  device_model = Device(**new_device, owner_id=owner_id)
  db.add(device_model)
  db.commit()
  db.refresh(device_model)
  return device_model

async def create_user_with_devices(dbConnection: Session, device_count: int):
  devices = []
  user = await create_user(db=dbConnection)

  for i in range(device_count):
    new_device = await create_device(db=dbConnection, owner_id=user.id)
    devices.append(new_device)

  return { 'user_id': user.id, 'devices': devices }
  
