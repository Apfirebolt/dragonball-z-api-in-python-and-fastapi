from sqlalchemy import Column, String, Integer

from db import Base

class ApiData(Base):
    __tablename__ = "api_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    character = Column(String(100))
    power_level = Column(String(100))
    saga_or_movie = Column(String(100))
    dragon_ball_series = Column(String(100))
   