from pydantic import BaseModel, field_validator, Field
# from geoalchemy2.shape import to_shape
import re
class DeviceBase(BaseModel):
  name: str # = Field(min_length=5)

class DeviceCreate(DeviceBase):
  owner_id: int
  # last_location: list[str]
  
class Device(DeviceBase):
  id: int
  # last_location: list[str]
  is_active: bool | None
  owner_id: int

  # @field_validator('last_location', mode='before')
  # def serialize_last_location(cls, value):
  #   coords = re.search(r"\((\d+\.\d+)\s+(\d+\.\d+)\)", to_shape(value).wkt)
  #   return list(coords.groups())


  class Config:
    from_attributes = True
    arbitrary_types_allowed=True


class DeviceListResponse(BaseModel):
  success: bool
  data: list[Device]

class DeviceResponse(BaseModel):
  success: bool
  data: Device