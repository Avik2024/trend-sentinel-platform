from pydantic import BaseModel

# Shared properties
class TrendBase(BaseModel):
    name: str
    mentions: int
    sentiment: str

# For creating a new trend
class TrendCreate(TrendBase):
    pass

# For returning a trend with ID
class Trend(TrendBase):
    id: int

    class Config:
        orm_mode = True
