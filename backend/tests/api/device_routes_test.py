from fastapi.testclient import TestClient
from fastapi.responses import Response
# import asyncio
from server import app
from tests.utils.TestBase import TestBase
from tests.fixtures.devices import create_user_with_devices

client = TestClient(app)

class DeviceRouteTest(TestBase):
  def setUp(self) -> None:
    return super().setUp()
  
  async def test_get_users_device(self):
    user_with_devices = await create_user_with_devices(self.dbConnection, 2)
    user_id = user_with_devices['user_id']

    response: Response =  client.get(f"users/{user_id}/devices")
    self.assertEqual(response.status_code, 200)
    response = response.json()
    self.assertEqual(len(response.get('data')), 2)


  def tearDown(self) -> None:
    return super().tearDown()
