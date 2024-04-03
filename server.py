from fastapi import FastAPI
from api.routers import devices, users

app = FastAPI()

@app.get("/")
async def api_details():
  return { "data": "thingshub API 0.0.1" }
app.include_router(users.router)
app.include_router(devices.router)