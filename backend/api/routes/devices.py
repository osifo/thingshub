import traceback
from fastapi import APIRouter, HTTPException, status
from domain.device.repository import IDeviceRepository
from domain.device.schema import DeviceListResponse, DeviceResponse, DeviceCreate
# from domain.device.exceptions

def controller(repository: IDeviceRepository):
  router = APIRouter(prefix="/devices", tags=["devices"])

  @router.get("/")
  async def index() -> DeviceListResponse:
    devices = await repository.get_devices()
    return { "success": True, "data": devices }

  @router.get("/{device_id}")
  async def get_device(device_id: str) -> DeviceResponse:
    return {"data": "device with id"}

  @router.post("/")
  async def create_device(device: DeviceCreate) -> DeviceResponse:
    try:
      new_device = await repository.create_device(device_param=device)
      return {
        "success": True,
        "data": new_device
      }
    except Exception as error:
      stack_trace = traceback.format_exc()
      print(f"error:\n{error}\ndetails:{stack_trace}")
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Device could not be created")

  return router
