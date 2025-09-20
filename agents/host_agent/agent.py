# agents/host_agent/agent.py
from fastapi import FastAPI, Body
from google.adk.agents import Agent, LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import vertexai

# --- Initialize Vertex AI (Gemini) ---
vertexai.init(project="wanderwise-ai-2025", location="us-central1")

# --- FastAPI app ---
app = FastAPI(title="WanderWise AI Backend")

MODEL = "gemini-2.0-flash-001"

# --- Flight Agent ---
flight_agent = LlmAgent(
    model=MODEL,
    name="FlightAgent",
    description="Finds best flight options for the trip. Return top 2 flights with price, timing, and airline."
)

# --- Stay Agent ---
stay_agent = LlmAgent(
    model=MODEL,
    name="StayAgent",
    description="Finds hotel or stay options within budget. Return top 2 hotels with name, location, price per night, and rating."
)

# --- Activity Agent ---
activity_agent = LlmAgent(
    model=MODEL,
    name="ActivityAgent",
    description="Suggests activities and attractions for the trip. Suggest 2-3 activities per day with timings and cost estimate."
)

# --- Planner (Root Orchestrator) ---
planner_agent = Agent(
    model=MODEL,
    name="PlannerAgent",
    description="Planner agent that builds structured travel itineraries",
    instruction="""
        You are a Travel Planner AI.
        Steps:
        1. Use FlightAgent for flights.
        2. Use StayAgent for hotels.
        3. Use ActivityAgent for activities.
        4. Build a day-by-day itinerary with morning, afternoon, evening.
        5. Respond ONLY in JSON with this format:
           {
             "itinerary": [
                {
                  "day": 1,
                  "morning": "string",
                  "afternoon": "string",
                  "evening": "string",
                  "notes": "string"
                }
             ]
           }
    """,
    sub_agents=[flight_agent, stay_agent, activity_agent]
)

# --- Session + Runner setup ---
session_service = InMemorySessionService()
runner = Runner(agent=planner_agent, session_service=session_service, app_name="wanderwise-ai")

# --- FastAPI Endpoint ---
@app.post("/itinerary")
async def generate_itinerary(user_request: dict = Body(...)):
    """
    Endpoint to generate a multi-day travel itinerary using ADK multi-agent setup.
    """
    query = user_request.get("query", "Plan a 3-day budget trip")

    try:
        # 1. Create a new session
        session = await session_service.create_session(
            app_name="wanderwise-ai", user_id="demo-user"
        )

        # 2. Run the query through the PlannerAgent
        events = await runner.run(
            user_id="demo-user",
            session_id=session.id,
            new_message={"role": "user", "text": query}
        )

        # 3. Extract final JSON response
        for e in events:
            if e.is_final_response():
                return {"itinerary": e.content.parts[0].text}

        return {"error": "No final response from planner_agent."}
    except Exception as e:
        return {"error": str(e)}
