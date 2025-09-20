from fastapi import FastAPI, Request
import uvicorn
import asyncio
from .task_manager import run

app = FastAPI(title="Flights Agent")

@app.post("/run")
async def execute(request: Request):
    payload = await request.json()
    result = await run(payload)
    return result

if __name__ == "__main__":
    uvicorn.run("agents.flight_agent.__main__:app", host="0.0.0.0", port=8001, reload=True)
 
