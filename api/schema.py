from typing import Optional, List
from pydantic import BaseModel, constr


class ApiDataBase(BaseModel):
    id: Optional[int]
    character: str
    power_level: str

    class Config:
        orm_mode = True


