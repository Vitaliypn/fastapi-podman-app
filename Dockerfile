FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn requests

EXPOSE 5000

CMD ["uvicorn", "client_service:app", "--host", "0.0.0.0", "--port", "5000"]
