from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(prefix="/trends", tags=["trends"])

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Trend])
def read_trends(db: Session = Depends(get_db)):
    return crud.get_trends(db)

@router.get("/{trend_id}", response_model=schemas.Trend)
def read_trend(trend_id: int, db: Session = Depends(get_db)):
    db_trend = crud.get_trend(db, trend_id)
    if not db_trend:
        raise HTTPException(status_code=404, detail="Trend not found")
    return db_trend

@router.post("/", response_model=schemas.Trend)
def create_trend(trend: schemas.TrendCreate, db: Session = Depends(get_db)):
    return crud.create_trend(db, trend)
