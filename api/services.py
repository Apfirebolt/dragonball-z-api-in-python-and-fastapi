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


def get_api_data_by_id(id: int, database) -> ApiData:
    data = database.query(ApiData).filter(ApiData.id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    return data


def create_new_data(request, database) -> ApiData:
    new_data = ApiData(
        character=request.character,
        power_level=request.power_level,
        saga_or_movie=request.saga_or_movie,
        dragon_ball_series=request.dragon_ball_series
    )
    database.add(new_data)
    database.commit()
    database.refresh(new_data)
    return new_data


def update_api_data(id: int, request, database) -> ApiData:
    data = database.query(ApiData).filter(ApiData.id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    
    data.character = request.character or data.character
    data.power_level = request.power_level or data.power_level
    data.saga_or_movie = request.saga_or_movie or data.saga_or_movie
    data.dragon_ball_series = request.dragon_ball_series or data.dragon_ball_series
    
    database.commit()
    database.refresh(data)
    return data


def delete_api_data(id: int, database):
    data = database.query(ApiData).filter(ApiData.id == id).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    database.delete(data)
    database.commit()
    return {"message": "Data deleted successfully"}







