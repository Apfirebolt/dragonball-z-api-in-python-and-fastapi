from typing import List
from fastapi import APIRouter, Depends, status, Response, Request
from sqlalchemy.orm import Session
from .models import ApiData
import pandas as pd
from typing import List
from .schema import ApiDataBase, ApiDataCreate
from fastapi_pagination import Page, add_pagination, paginate, Params
from auth.jwt import get_current_user

import db

from . import services

router = APIRouter(tags=["DBZ"], prefix="/api")


@router.get("/", status_code=status.HTTP_200_OK, response_model=Page[ApiDataBase])
async def api_data(params: Params = Depends(), database: Session = Depends(db.get_db)):
    result = services.get_api_data(database)
    return paginate(result, params)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ApiDataBase)
async def get_api_data_by_id(id: int, database: Session = Depends(db.get_db)):
    result = services.get_api_data_by_id(id, database)
    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ApiDataBase)
async def create_api_data(
    request: ApiDataCreate,
    database: Session = Depends(db.get_db),
    current_user: str = Depends(get_current_user),
):
    if not current_user:
        return Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="You do not have permission to perform this action.",
        )
    result = services.create_new_data(request, database)
    return result


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=ApiDataBase)
async def update_api_data(
    id: int,
    request: ApiDataCreate,
    database: Session = Depends(db.get_db),
    current_user: str = Depends(get_current_user),
):
    if not current_user:
        return Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="You do not have permission to perform this action.",
        )
    result = services.update_api_data(id, request, database)
    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return result


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_api_data(
    id: int,
    database: Session = Depends(db.get_db),
    current_user: str = Depends(get_current_user),
):
    if not current_user:
        return Response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content="You do not have permission to perform this action.",
        )
    result = services.delete_api_data(id, database)
    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/populate", status_code=status.HTTP_201_CREATED)
async def create_api_data(database: Session = Depends(db.get_db)):
    df = pd.read_csv("data/data.csv")
    for index, data in df.iterrows():
        result = services.create_new_data(
            data["Character"],
            data["Power_Level"],
            data["Saga_or_Movie"],
            data["Dragon_Ball_Series"],
            database,
        )
    return {"message": "Data populated successfully"}
