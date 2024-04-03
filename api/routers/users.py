import traceback
from fastapi import APIRouter, HTTPException, status, Query
from domain.user import schema, exceptions
from data.user.repository import UserRepository
from data.device.repository import DeviceRepository
from domain.device.schema import DeviceListResponse
# from utils.http import HttpSuccessResponse


router = APIRouter(prefix="/users", tags=["users"])
user_repository = UserRepository()
device_repository = DeviceRepository()

# @router.get("/me")
# async def get_current_user():
#   return HttpResponse(data="current_user")

@router.get("/")
async def index(filter_params: str | None = None) -> schema.UserListHTTPResponse:
  try:  
    user_data = await user_repository.get_users()
    return {
      "success": True,
      "data": user_data
    }

  except exceptions.UserInvalidError as error:
      stack_trace = traceback.format_exc()
      print(f"error:\n{error}\ndetails:{stack_trace}")
      raise HTTPException(status_code=error.code, detail=error.message)
      # self.logger.info(error.message)
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User could not be created")

@router.post("/")
async def create_user(user_param: schema.UserCreate) -> schema.UserHTTPResponse:
  try:
    user = await user_repository.create_user(user_params=user_param)
    return {
      "data": user,
      "success": True
    }
  except exceptions.UserInvalidError as error:
    raise HTTPException(status_code=error.code, detail=error.message)
    # self.logger.info(error.message)
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User could not be created")

@router.get("/{user_id}")
async def show_user(user_id: str):
  try:  
    user_data = await user_repository.show_user(user_id)
    return {
      "success": True,
      "data": user_data
    }

  except exceptions.UserInvalidError as error:
      stack_trace = traceback.format_exc()
      print(f"error:\n{error}\ndetails:{stack_trace}")
      raise HTTPException(status_code=error.code, detail=error.message)
      # self.logger.info(error.message)
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User could not be created")


@router.get("/{user_id}/devices")
async def show_user(user_id: str) -> DeviceListResponse:
  try:
    user_devices = await device_repository.get_user_devices({"owner_id": user_id })
    return {
      "success": True,
      "data": user_devices
    }

  except exceptions.UserInvalidError as error:
      stack_trace = traceback.format_exc()
      print(f"error:\n{error}\ndetails:{stack_trace}")
      raise HTTPException(status_code=error.code, detail=error.message)
      # self.logger.info(error.message)
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User could not be created")

