from fastapi import FastAPI, HTTPException
from redis import Redis

import time

app = FastAPI()
redis_client = Redis(host='localhost', port=6379)

@app.get("/get/{key}")
async def get_value(key: str):
  """Retrieves the value for a given key."""
  t1 = time.time()
  value = redis_client.hget('data', key)
  if value is None:
    raise HTTPException(status_code=404, detail="Key not found")
  print('Time Taken ', time.time() - t1)
  return value.decode('utf-8')  # Decode byte string to string

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000)  # Change port if needed
