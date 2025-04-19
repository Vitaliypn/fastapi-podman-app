from fastapi import FastAPI, Header, HTTPException
import requests

app = FastAPI()
APP_TOKEN = "SuperSecretToken"

DB_SERVICE_URL = "http://localhost:8001"
BUSINESS_SERVICE_URL = "http://localhost:8002"

@app.get("/")
def root():
    return {"description": "Client Service - gateway to interact with the system."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/orchestrate")
def orchestrate(authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    read_response = requests.get(f"{DB_SERVICE_URL}/read")
    data = read_response.json()
    process_response = requests.post(f"{BUSINESS_SERVICE_URL}/process", json=data)
    processed_data = process_response.json()
    save_response = requests.post(f"{DB_SERVICE_URL}/save", json=processed_data)

    return {"final_response": processed_data}