from typing import Optional, List
from pydantic import BaseModel 


class ApiDataBase(BaseModel):
    id: Optional[int]
    character: str
    power_level: str

    class Config:
        from_attributes = True



class ApiDataCreate(BaseModel):
    character: str
    power_level: str
    saga_or_movie: Optional[str] = None
    dragon_ball_series: Optional[str] = None

    class Config:
        from_attributes = True