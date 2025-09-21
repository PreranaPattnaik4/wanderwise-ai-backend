from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="WanderWise AI Backend")

# CORS: allow frontend (for demo we allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # during demo: allow all; later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ItineraryRequest(BaseModel):
    source: str
    destination: str
    days: int = 3
    budget: str = "medium"

@app.get("/")
def read_root():
    return {"message": "WanderWise AI Backend is running!"}

@app.post("/itinerary")
async def generate_itinerary(req: ItineraryRequest):
    # ----- Dummy itinerary response (replace with ADK/Gemini call when ready) -----
    plan = []
    for d in range(1, max(1, req.days) + 1):
        if d == 1:
            morning = f"Arrive in {req.destination}. Settle into accommodation."
            afternoon = f"Explore downtown and local markets of {req.destination}."
            evening = f"Sunset dinner at a local restaurant."
        elif d == req.days:
            morning = f"Leisure morning and final shopping in {req.destination}."
            afternoon = f"Pack and prepare for departure back to {req.source}."
            evening = f"Transfer to airport/train and depart."
        else:
            morning = f"Visit morning attraction #{d} in {req.destination}."
            afternoon = f"Local sightseeing and lunch."
            evening = f"Relax at beach/cafe."
        plan.append({
            "day": d,
            "morning": morning,
            "afternoon": afternoon,
            "evening": evening,
        })

    response = {
        "trip_request": {
            "source": req.source,
            "destination": req.destination,
            "days": req.days,
            "budget": req.budget,
        },
        "itinerary": plan,
        "general_notes": [
            "Purchase local transport passes for savings.",
            "Check weather before travel and pack accordingly.",
            "Local restaurants may accept card or cash depending on area."
        ],
    }
    return response
