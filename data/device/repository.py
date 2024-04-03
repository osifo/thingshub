from sqlalchemy.orm import Session
from fastapi import Depends;
from domain.device.repository import DeviceRepository as IDeviceRepository
from domain.device import schema, model
from database.config import get_database

class DeviceRepository(IDeviceRepository):
  def __init__(self, database: Session = Depends(get_database)) -> None:
    self.db = database

  def create_device(self, device_param: schema.DeviceCreate) -> schema.Device:
    device = model.Device(**device_param.model_dump())
    self.db.add(device)
    self.db.commit()
    self.db.refresh(device)
    return device

  def list_devices(self) -> list[schema.Device]:
    return self.db.query(model.Device).all()
  
  def get_device(self, device_id: str) -> schema.Device:
    return self.db.query(model.Device).get(device_id)

  def delete_device(database: Session, user_id: str):
    pass

  def update_device(database: Session, user_id: str):
    pass