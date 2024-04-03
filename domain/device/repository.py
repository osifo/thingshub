import abc
from abc import ABCMeta
from sqlalchemy.orm import Session
from .schema import DeviceCreate, Device

class DeviceRepository(metaclass=ABCMeta): # or DeviceRepository(ABC)
  @abc.abstractmethod
  def __init__(self, dbConnection: Session) -> None:
    """ Creates a new device repository """
    raise NotImplementedError

  @abc.abstractmethod
  def create_device(device_param: DeviceCreate) -> Device:
    """Create a new device"""
    raise NotImplementedError
  
  @abc.abstractmethod
  def update_device(device_id: int, device_param: Device) -> Device:
    """Updates the device that matches the id passed or throws an exception"""
    raise NotImplementedError
  
  @abc.abstractmethod
  def list_devices(filter: dict) -> list[Device]:
    """ returns a list of devices that matches teh filter """
    raise NotImplementedError
  
  @abc.abstractmethod
  def get_device(device_id: str) -> Device:
    """ returns the device that matches this id """
    raise NotImplementedError
  
  @abc.abstractmethod
  def delete_device(device_id: str) -> bool:
    """ deletes the device that matches this id """
    raise NotImplementedError
  
