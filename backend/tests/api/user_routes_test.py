from fastapi.testclient import TestClient
from fastapi.responses import Response
from server import app
from tests.utils.TestBase import TestBase

client = TestClient(app)

class UserRouteTest(TestBase):
  def test_index(self):
    response: Response = client.get("/users")
    self.assertEqual(response.status_code, 200)
    response = response.json()
    self.assertEquals(len(response.get('data')), 0)


  # def test_get_device(self):
  #   response = client.get("/devices/1")
  #   self.assertEqual(response.status_code, 200)