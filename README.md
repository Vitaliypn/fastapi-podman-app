FastAPI Microservices – Client, Business, and DB Services
This project includes a system of three lightweight FastAPI-based microservices, containerized and networked using Podman and Podman Compose.

Overview
Microservices included:
Client Service
Handles external API requests, validates tokens, and orchestrates communication between services.

Business Logic Service
Simulates business logic by processing incoming data.

Database Service
Stores and retrieves data using an in-memory structure.

Project Structure
bash
Копіювати
Редагувати
.
├── client_service.py          # Main API gateway with authentication and orchestration
├── business_service.py        # Simulated data processor
├── db_service.py              # In-memory data storage
├── Dockerfile                 # Container for Client Service
├── Dockerfile.scheduler       # Container for optional scheduler service
├── podman-compose.yml         # Multi-container orchestration setup
└── README.md
Running the Services (Manually)
Use 3 separate terminals (or tools like tmux):

bash
Копіювати
Редагувати
uvicorn db_service:app --port 8001
uvicorn business_service:app --port 8002
uvicorn client_service:app --port 8000
Authentication
Requests to the Client Service must include the following header:

makefile
Копіювати
Редагувати
Authorization: Bearer SuperSecretToken
Example Request Flow
Trigger orchestration with:

bash
Копіювати
Редагувати
curl -X POST http://localhost:8000/orchestrate \
     -H "Authorization: Bearer SuperSecretToken"
How it works:
Client Service receives the request on /orchestrate

It sends a GET to DB Service to read data

Sends that data to Business Service to process

Sends the result back to DB Service to store

Returns the processed result to the client
