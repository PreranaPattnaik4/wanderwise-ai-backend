# agents/host_agent/__main__.py
from agents.host_agent.agent import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("agents.host_agent.agent:app", host="0.0.0.0", port=8000, reload=True)
