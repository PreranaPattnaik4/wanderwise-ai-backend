# agents/stay_agent/agent.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio

# Initialize FastAPI app
app = FastAPI(
    title="Stay Agent",
    description="Agent that provides hotel stay options",
    version="1.0.0"
)

# ✅ Request schema (aligned with Host Agent)
class StayRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: float

# ✅ Response schema
class StayOption(BaseModel):
    name: str
    price_per_night: float
    total: float

# Mocked hotels for demo
async def mock_get_hotels(destination: str, budget: float) -> List[Dict[str, Any]]:
    await asyncio.sleep(0.2)  # simulate API latency
    return [
        {"name": "Hotel Comfort", "price_per_night": 120, "total": 480},
        {"name": "Budget Inn", "price_per_night": 80, "total": 320},
        {"name": "Luxury Palace", "price_per_night": 250, "total": 1000},
    ]

# ✅ Endpoint
@app.post("/run")
async def run_agent(request: StayRequest) -> Dict[str, Any]:
    stays = await mock_get_hotels(request.destination, request.budget)
    return {
        "destination": request.destination,
        "stays": stays
    }

# ✅ Run with: python -m agents.stay_agent.agent
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agents.stay_agent.agent:app", host="0.0.0.0", port=8002, reload=True)
