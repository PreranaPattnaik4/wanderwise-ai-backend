🌍 WanderWise AI – Backend

FastAPI backend powered by **Google Cloud’s Agentic AI + Gemini**.  
This service provides AI-driven travel itinerary generation using the **Google Agents Developer Kit (ADK)**.  
Designed for deployment on **Google Cloud Run** and integration with a React frontend on Firebase Hosting.  

---

🚀 Features
- ✈️ AI-powered travel itinerary planner (Gemini 2.5 Flash)
- ⚡ RESTful endpoints via FastAPI
- 🌐 Cloud-ready deployment with Docker + Cloud Run
- 📊 Future expansion for Firestore and booking APIs

---

🛠️ Tech Stack
- **FastAPI** – Backend framework  
- **Google ADK** – Agent orchestration  
- **Gemini 2.5 Flash** – Core AI model  
- **Cloud Run** – Serverless deployment  
- **Firestore (planned)** – Persistent storage  

---

📂 Folder Structure

wanderwise_ai_backend/
├── agents/
│ ├── activities_agent/ # Handles activities planning
│ ├── flight_agent/ # Handles flight search & booking logic
│ ├── host_agent/ # Main orchestrator agent
│ ├── simple_itinerary_agent/ # Gemini-powered travel itinerary agent
│ ├── stay_agent/ # Handles stay/hotel planning
│ └── init.py
├── routers/
│ └── itinerary_router.py # API route for itinerary generation
├── main.py # FastAPI entrypoint
├── requirements.txt
├── Dockerfile
└── README.md

