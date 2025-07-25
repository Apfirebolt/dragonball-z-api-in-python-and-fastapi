from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
import db
from . import schema
from . import services
from . import validator

from . jwt import create_access_token, get_current_user

from . import hashing
from . models import User

router = APIRouter(tags=['Auth'], prefix='/api/auth')


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User,
                                   database: Session = Depends(db.get_db)):

    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail="This user with this email already exists in the system."
        )

    new_user = await services.new_user_register(request, database)
    return new_user


@router.get('/users', response_model=List[schema.DisplayAccount])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.all_users(database)

@router.get('/users/{user_id}', response_model=schema.DisplayAccount)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    user_info = await services.get_user_by_id(user_id, database)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return schema.DisplayAccount.from_orm(user_info)


@router.post('/login')
def login(request: schema.Login,
          database: Session = Depends(db.get_db)):    
    user = database.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")

    # Generate a JWT Token
    user = schema.DisplayAccount.from_orm(user)
    access_token = create_access_token(data={"sub": user.email, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer", "user": user}


@router.get('/profile', response_model=schema.DisplayAccount)
async def get_profile(database: Session = Depends(db.get_db), current_user: schema.User = Depends(get_current_user)):
    return await services.get_profile(database, current_user)










