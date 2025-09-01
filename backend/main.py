# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI(
    title="Trend Sentinel Backend",
    description="Backend API for real-time trend detection project",
    version="1.0.0"
)

# Example data model
class Trend(BaseModel):
    id: int
    name: str
    mentions: int
    sentiment: str

# In-memory fake database
fake_trends_db = [
    {"id": 1, "name": "AI", "mentions": 5230, "sentiment": "positive"},
    {"id": 2, "name": "Elections", "mentions": 3110, "sentiment": "neutral"},
    {"id": 3, "name": "Stock Market", "mentions": 2100, "sentiment": "negative"},
]

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Trend Sentinel Backend API"}

# Get all trends
@app.get("/trends", response_model=List[Trend])
def get_trends():
    return fake_trends_db

# Get single trend by ID
@app.get("/trends/{trend_id}", response_model=Trend)
def get_trend(trend_id: int):
    for trend in fake_trends_db:
        if trend["id"] == trend_id:
            return trend
    return {"error": "Trend not found"}

# Add a new trend
@app.post("/trends", response_model=Trend)
def add_trend(trend: Trend):
    fake_trends_db.append(trend.dict())
    return trend
