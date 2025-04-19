from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"description": "Business Logic Service - processes data."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process_data(payload: dict):
    time.sleep(2)
    return {"original": payload, "processed": True}