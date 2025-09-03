from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Mount static folder
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# ----------------- Models -----------------
class Trend(BaseModel):
    id: int
    name: str
    mentions: int
    sentiment: str

# ----------------- Fake DB -----------------
fake_trends_db: List[Trend] = [
    Trend(id=1, name="AI", mentions=5230, sentiment="positive"),
    Trend(id=2, name="Elections", mentions=3110, sentiment="neutral"),
    Trend(id=3, name="Stock Market", mentions=2100, sentiment="negative"),
]

# ----------------- Routes -----------------
@app.get("/")
def read_root():
    return {"message": "Welcome to Trend Sentinel Backend API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/trends", response_model=List[Trend])
def get_trends():
    return fake_trends_db

@app.get("/trends/{trend_id}", response_model=Trend)
def get_trend(trend_id: int):
    for trend in fake_trends_db:
        if trend.id == trend_id:
            return trend
    raise HTTPException(status_code=404, detail="Trend not found")

@app.post("/trends", response_model=Trend)
def add_trend(trend: Trend):
    new_id = max([t.id for t in fake_trends_db]) + 1 if fake_trends_db else 1
    new_trend = Trend(id=new_id, name=trend.name, mentions=trend.mentions, sentiment=trend.sentiment)
    fake_trends_db.append(new_trend)
    return new_trend

# ----------------- Serve favicon.ico -----------------
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = os.path.join(static_dir, "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    raise HTTPException(status_code=404, detail="Favicon not found")
