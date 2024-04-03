from pydantic import BaseModel
import geoalchemy2

class DeviceBase(BaseModel):
  name: str

class DeviceCreate(DeviceBase):
  owner_id: int
  last_location: list[str]
  
class Device(DeviceBase):
  id: int
  # last_location: geoalchemy2.elements.WKBElement
  is_active: bool | None
  owner_id: int

  class Config:
    from_attributes = True
    arbitrary_types_allowed=True


class DeviceListResponse(BaseModel):
  success: bool
  data: list[Device]

class DeviceResponse(BaseModel):
  success: bool
  data: Device