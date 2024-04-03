import json
from fastapi import status

class UserBaseError(Exception):
  def __init__(self, message: str, code: str) -> None:
    super().__init__(message)
    self.message = message 
    self.code = code

  def __str__(self) -> str:
    return json.dumps({
      "success": False,
      "message": self.message,
      "code": self.code
      })

class UserInvalidError(UserBaseError):
  message = "The user parameters provided are invalid."
  code = status.HTTP_400_BAD_REQUEST

  def __str__(self):
    return UserBaseError(
      message = UserInvalidError.message,
      code = UserInvalidError.code
    )