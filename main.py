from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel, Field

app = FastAPI()

class Thing(BaseModel):
  name: str
  last_location: str | None = None
  test: str | None = Field(None, hidden=True)

@app.get("/", tags=["things"])
async def index():
  return {
    "data": { 
      "things": [
        {"name": "key", "last_location": "3.4145, 6,4349"},
        {"name": "bike", "last_location": "4.4145, 1,4349"},
      ] 
    },
    "success": True
  }

@app.post("/create", tags=["things"])
async def create(thing_param: Thing, creator_id: int = Body()):
  return {
    "data": thing_param,
    "success": True
  }

@app.get("/things/{user_id}/", description="User's things", tags=["users"])
async def list_user_things(user_id: int = Path(le=20, gt=10), query: str | None = Query(None, min_length=5)):
  return {
    "data": { 
      "user_id": user_id,
      "things": [
        {"name": "key", "last_location": "3.4145, 6,4349"},
        {"name": "bike", "last_location": "4.4145, 1,4349"},
      ] 
    },
    "success": True
  }

  

  # for a long-running synchronous call, use asyncio.run_in_executor() to offshore the operation to a thread or process pool, in order to free up the main thread.
  # -  thread pool for tasks I/O tasks or non-CPU-intensive tasks, and process pools for CPU-intensive tasks.


