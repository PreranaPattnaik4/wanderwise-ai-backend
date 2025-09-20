import os
import asyncio
from google.adk.agents import LlmAgent

# Model for flights agent
MODEL = os.getenv("WANDERWISE_MODEL", "gemini-2.0-flash-001")

# Define FlightsAgent
flights_agent = LlmAgent(
    model=MODEL,
    name="FlightsAgent",
    description="Suggests and summarizes flight options for given origin/destination/dates.",
    instruction=(
        "Given origin, destination, start_date, end_date, and budget, "
        "return JSON with a 'flights' key containing a list of flight options "
        "(airline, price, depart, return). Keep results realistic but concise."
    ),
    disallow_transfer_to_peers=True,
)

# Mocked helper for testing (replace with EMT API later)
async def mock_get_flights(origin: str, destination: str, start_date: str, end_date: str):
    await asyncio.sleep(0.3)
    return [
        {"airline": "MockAir", "price": 350.0, "depart": start_date, "return": end_date},
        {"airline": "BudgetFly", "price": 280.0, "depart": start_date, "return": end_date},
    ]
 
