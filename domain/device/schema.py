from pydantic import BaseModel

class DeviceBase(BaseModel):
  name: str

class DeviceCreate(DeviceBase):
  owner_id: str

class Device(DeviceBase):
  id: str
  last_location: tuple[str, str]
  is_active: bool
  owner_id: str

