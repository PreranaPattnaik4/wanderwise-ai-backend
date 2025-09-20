# agents/activities_agent/agent.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="Activities Agent",
    description="Agent that provides activity and attraction options",
    version="1.0.0"
)

# ✅ Request schema
class ActivityRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str

# ✅ Response schema
class ActivityOption(BaseModel):
    name: str
    description: str
    price: float
    duration_hours: int

# ✅ Endpoint
@app.post("/run")
async def run_agent(request: ActivityRequest) -> Dict[str, Any]:  # FIXED typing
    """
    Mock activities agent endpoint.
    Returns a list of fun activities for the requested trip.
    """

    activities = [
        ActivityOption(
            name="Walking Food Tour",
            description="Taste local street food and specialties",
            price=45.0,
            duration_hours=3
        ),
        ActivityOption(
            name="Museum Pass",
            description="Access to top museums with skip-the-line tickets",
            price=25.0,
            duration_hours=2
        ),
        ActivityOption(
            name="City Bike Ride",
            description="Guided cycling tour around main attractions",
            price=30.0,
            duration_hours=4
        )
    ]

    return {
        "destination": request.destination,
        "activities": [act.dict() for act in activities]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agents.activities_agent.agent:app", host="0.0.0.0", port=8003, reload=True)
