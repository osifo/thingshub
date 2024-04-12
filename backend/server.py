import sys
from fastapi import FastAPI
from api.router import AppRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.middlewares.logger import LoggerMiddleware
from config import Config, DatabaseConfig

app = FastAPI()

# if Config.APP_ENV != 'test':


app.add_middleware(LoggerMiddleware)
app.add_middleware(
  CORSMiddleware, 
  allow_origins=Config.ALLOWED_ORIGINS,
  allow_methods=['*'],
  allow_headers=['*'],
  allow_credentials=True
)

app.mount("/static", StaticFiles(directory="public"))

@app.get("/")
async def api_details():
  return { "data": "thingshub API 0.0.1" }

databaseConfig: DatabaseConfig = next(Config.get_database(Config.APP_ENV))
AppRouter.setup(app, databaseConfig.connection)
