from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class LoggerMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request,  call_next):
    payload = request.headers
    print(f"headers ========== {payload}")
    return await call_next(request)