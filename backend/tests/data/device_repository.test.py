from unittest import TestCase
from unittest.mock import MagicMock 
from data.device.repository import DeviceRepository
from config import get_test_database

import sys
sys.path.append('..')

class DeviceRepositoryTest(TestCase):
  device_repository = DeviceRepository(get_test_database)
  def test_get_devices(self):
    device_repository.get_devices
    pass

  def test_create_device(self):
    pass

  def test_get_device(self):
    pass

  def test_delete_device(self):
    pass

  def test_update_device(self):
    pass