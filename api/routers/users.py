from fastapi import APIRouter, Depends
from ..utils.http import HttpSuccessResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def get_current_user():
  return HttpResponse(data="current_user")