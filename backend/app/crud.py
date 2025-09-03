from sqlalchemy.orm import Session
from . import models, schemas

def get_trends(db: Session):
    return db.query(models.Trend).all()

def get_trend(db: Session, trend_id: int):
    return db.query(models.Trend).filter(models.Trend.id == trend_id).first()

def create_trend(db: Session, trend: schemas.TrendCreate):
    db_trend = models.Trend(**trend.dict())
    db.add(db_trend)
    db.commit()
    db.refresh(db_trend)
    return db_trend
