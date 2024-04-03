from sqlalchemy.orm import Session
from geoalchemy2 import Geometry
from domain.device.repository import IDeviceRepository
from domain.device import schema, model
from config import get_database

class DeviceRepository(IDeviceRepository):
  def __init__(self) -> None:
    self.db = next(get_database())

  async def create_device(self, device_param: schema.DeviceCreate) -> schema.Device:
    location_param = device_param.last_location
    device = model.Device(
      **device_param.model_dump(exclude=['last_location']),
      last_location=f"POINT({' '.join(location_param)})"
    )
    print(f"device ========= {device}")
    self.db.add(device)
    self.db.commit()
    self.db.refresh(device)
    return device

  async def get_devices(self, filter_params: dict | None = None) -> list[schema.Device]:
    return self.db.query(model.Device).where(filter_params)
  
  async def get_device(self, device_id: str) -> schema.Device:
    return self.db.query(model.Device).get(device_id)

  async def delete_device(database: Session, user_id: str):
    pass

  async def update_device(database: Session, user_id: str):
    pass