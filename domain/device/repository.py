import abc
from abc import ABCMeta
from sqlalchemy.orm import Session
from .schema import DeviceCreate, Device

class IDeviceRepository(metaclass=ABCMeta): # or DeviceRepository(ABC)
  @abc.abstractmethod
  def create_device(self, device_params: DeviceCreate) -> Device:
    """Create a new device"""
    raise NotImplementedError
  
  @abc.abstractmethod
  def update_device(self, device_id: int, device_param: Device) -> Device:
    """Updates the device that matches the id passed or throws an exception"""
    raise NotImplementedError
  
  @abc.abstractmethod
  def get_devices(self, filter_params: dict | None = None) -> list[Device]:
    """ returns all devices that matches the filter params """
    raise NotImplementedError
  
  @abc.abstractmethod
  def get_device(self, device_id: str) -> Device:
    """ returns the device that matches this id """
    raise NotImplementedError
  
  @abc.abstractmethod
  def delete_device(self, device_id: str) -> bool:
    """ deletes the device that matches this id """
    raise NotImplementedError
  
