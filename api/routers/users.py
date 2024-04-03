import traceback
from fastapi import APIRouter, HTTPException, status
from domain.user import schema, exceptions
from data.user.repository import UserRepository
# from utils.http import HttpSuccessResponse


router = APIRouter(prefix="/users", tags=["users"])
repository = UserRepository()

# @router.get("/me")
# async def get_current_user():
#   return HttpResponse(data="current_user")

@router.post("/")
async def create_user(user_param: schema.UserCreate) -> schema.UserHTTPResponse:
  try:
    user = repository.create_user(user_params=user_param)
    return {
      "data": user,
      "success": True
    }
  except exceptions.UserInvalidError as error:
    print(f"error ========== \n{error.message}")
    return HTTPException(status_code=error.code, detail=error.message)
    # self.logger.info(error.message)
  except Exception as error:
    stack_trace = traceback.format_exc()
    print(f"error:\n{error}\ndetails:{stack_trace}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User could not be created")

@router.get("/{user_id}")
async def show_user(user_id: str):
  user_data = repository.show_user(user_id)

  return {
    "success": True,
    "data": user_data
  }