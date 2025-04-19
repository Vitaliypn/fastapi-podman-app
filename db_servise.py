from fastapi import FastAPI, Request

app = FastAPI()
data_store = {"example": "data"}

@app.get("/")
def root():
    return {"description": "Database Service - stores and retrieves data."}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/read")
def read():
    return data_store

@app.post("/save")
async def save(request: Request):
    body = await request.json()
    data_store.update(body)
    return {"status": "saved", "data": body}