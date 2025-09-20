import asyncio
from .agent import mock_get_flights

# Core task function for flight_agent
async def run(payload: dict):
    origin = payload.get("origin", "Unknown")
    destination = payload.get("destination", "Unknown")
    start_date = payload.get("start_date", "")
    end_date = payload.get("end_date", "")

    flights = await mock_get_flights(origin, destination, start_date, end_date)

    return {"flights": flights}
 
