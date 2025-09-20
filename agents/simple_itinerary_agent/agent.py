from google.adk.agents import Agent

# Define a simple root agent
root_agent = Agent(
    model="gemini-2.5-flash",   # Or gemini-2.0-flash-001 if you want stable
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge.",
)
