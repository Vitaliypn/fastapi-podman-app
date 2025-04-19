from fastapi import FastAPI
import requests
import time
import threading
import os

app = FastAPI()
MAIN_APP_URL = os.environ.get("MAIN_APP_URL", "http://client-service:5000")

def scheduler():
    while True:
        try:
            response = requests.get(f"{MAIN_APP_URL}/health")
            print(f"[Scheduler] Main App response: {response.json()}")
        except Exception as e:
            print(f"[Scheduler] Failed to reach main app: {e}")
        time.sleep(10)

@app.on_event("startup")
def startup_event():
    threading.Thread(target=scheduler, daemon=True).start()

@app.get("/")
def root():
    return {"description": "Scheduler Service - calls main app every 10 seconds"}
