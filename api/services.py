from fastapi import HTTPException, status
from typing import List
from .models import ApiData

def create_new_data(character, power_level, saga_or_movie, dragon_ball_series, database) -> ApiData:

    new_data = ApiData(character=character, 
                        power_level=power_level,
                        saga_or_movie=saga_or_movie,
                        dragon_ball_series=dragon_ball_series)
    database.add(new_data)
    database.commit()
    database.refresh(new_data)
    return new_data


def get_api_data(database):
    data = database.query(ApiData).all()
    return data







