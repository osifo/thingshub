from fastapi import APIRouter
from domain.device.schema import DeviceCreate, Device
from data.device.repository import DeviceRepository

router = APIRouter(prefix="/devices", tags=["devices"])
repository = DeviceRepository()

@router.get("/", response_model = list[Device])
async def index():
  return repository.get_devices()

@router.get("/{device_id}", response_model=Device)
async def get_device(device_id: str):
  return {"data": "device with id"}

@router.post("/", response_model=Device)
async def create_device(device: DeviceCreate):
  return repository.create_device(device_param=device)