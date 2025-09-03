from sqlalchemy import Column, Integer, String
from .database import Base

# Example Trend model (you can extend later)
class Trend(Base):
    __tablename__ = "trends"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mentions = Column(Integer)
    sentiment = Column(String)
