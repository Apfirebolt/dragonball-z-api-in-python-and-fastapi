from typing import List
from fastapi import APIRouter, Depends, status, Response, Request
from sqlalchemy.orm import Session
from .models import ApiData
import pandas as pd
from typing import List
from . schema import ApiDataBase
from fastapi_pagination import Page, add_pagination, paginate, Params

import db

from .import services

router = APIRouter(
    tags=["DBZ"],
    prefix='/api'
)
    

@router.get('/', status_code=status.HTTP_200_OK, response_model=Page[ApiDataBase])
async def api_data(params: Params = Depends(), database: Session = Depends(db.get_db)):
    result = services.get_api_data(database)
    return paginate(result, params)


@router.post('/populate', status_code=status.HTTP_201_CREATED)
async def create_api_data(database: Session = Depends(db.get_db)):
    df = pd.read_csv('data/data.csv')
    for index, data in df.iterrows():
        result = services.create_new_data(data['Character'], data['Power_Level'], data['Saga_or_Movie'], data['Dragon_Ball_Series'], database)
    return {
        'message': 'Data populated successfully'
    }

