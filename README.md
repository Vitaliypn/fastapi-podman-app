## Overview

This project includes three microservices:
- `Client Service` – handles external requests, validates token, and orchestrates between services.
- `Business Logic Service` – simulates processing of data.
- `Database Service` – stores and retrieves data in-memory.

## Structure

```
client_service.py
business_service.py
db_service.py
README.md
```

## Running the Services

Use 3 separate terminals or tools like tmux:

```bash
uvicorn db_service:app --port 8001
uvicorn business_service:app --port 8002
uvicorn client_service:app --port 8000
```

## Authentication

Client requests must include this header:

```
Authorization: Bearer SuperSecretToken
```

## Example Request Flow

```bash
curl -X POST http://localhost:8000/orchestrate \
     -H "Authorization: Bearer SuperSecretToken"
```

The flow is:
1. Client calls `/orchestrate` on Client Service.
2. Client Service reads data from DB Service.
3. It sends data to Business Logic Service.
4. It saves the processed data back to DB.
5. Returns the result to the client.