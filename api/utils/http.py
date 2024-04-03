from fastapi import status

class HttpSuccessResponse:
  def __init__(data, http_code: str = status.HTTP_200_OK):
    data = data
    http_code = http_code

  def __str__():
    return json.dumps({"data": data, "http_code": http_code})

class HttpErrorResponse:
  def __init__(message, http_code: str = status.HTTP_400_BAD_REQUEST):
    message = message
    http_code = http_code

  def __str__():
    return json.dumps({"message": message, "http_code": http_code})