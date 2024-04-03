import traceback
from fastapi import APIRouter, HTTPException, status
from domain.device.schema import DeviceCreate
from data.device.repository import DeviceRepository
from domain.device.schema import DeviceListResponse, DeviceResponse
# from domain.device.exceptions

router = APIRouter(prefix="/devices", tags=["devices"])
repository = DeviceRepository()

@router.get("/")
async def index() -> DeviceListResponse:
  devices = await repository.get_devices()
  return { "success": True, "data": devices }

@router.get("/{device_id}")
async def get_device(device_id: str) -> DeviceResponse:
  return {"data": "device with id"}

@router.post("/")
async def create_device(device: DeviceCreate):
  try:
    new_device = await repository.create_device(device_param=device)
    print(f"device ====== {new_device}")
    return {
      "success": True,
      "data": new_device
    }
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Device could not be created")
