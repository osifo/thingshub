from sqlalchemy import and_
from sqlalchemy.orm import Session
from domain.device.repository import IDeviceRepository
from domain.device import schema, model

class DeviceRepository(IDeviceRepository):
  def __init__(self, database: Session) -> None:
    self.db = database

  async def create_device(self, device_param: schema.DeviceCreate) -> schema.Device:
    location_param = device_param.last_location
    device = model.Device(
      **device_param.model_dump(exclude=['last_location']),
      last_location=f"POINT({' '.join(location_param)})"
    )
    self.db.add(device)
    self.db.commit()
    self.db.refresh(device)
    return device

  async def get_devices(self, filter_params: dict | None = None) -> list[schema.Device]:
    # where_query = map(lambda key: model.Device[key] == filter_params[key], filter_params.keys())
    # print(f"where_query ========= {where_query}")
    # return self.db.query(model.Device).where(and_(','.join(where_query)))
    owner_id = filter_params.get("owner_id")
    return self.db.query(model.Device).where(model.Device.owner_id == owner_id)
  
  async def get_device(self, device_id: str) -> schema.Device:
    return self.db.query(model.Device).get(device_id)

  async def delete_device(database: Session, user_id: str):
    pass

  async def update_device(database: Session, user_id: str):
    pass