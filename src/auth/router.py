from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.dependencies import db_dependency
from src.auth.exceptions import auth_exception
from src.auth.utils import create_token
from src.users.models import User
from src.users.schemas import UserIn, UserOutReg
from src.users.utils import get_user_by_email, get_hashed_password, verify_password

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/registration/', response_model=UserOutReg, status_code=status.HTTP_201_CREATED)
async def registration(user_data: UserIn, db: db_dependency):
    if get_user_by_email(user_data.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already in used")

    hashed_password = get_hashed_password(user_data.password)

    user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        username=user_data.username
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    jwt_token = create_token(user)

    user_output = user.dict()
    user_output['access_token'] = jwt_token

    return user_output


@router.post('/login/')
async def login(user_info: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = get_user_by_email(user_info.username, db=db)
    if not user:
        raise auth_exception

    if not verify_password(user_info.password, user.hashed_password):
        raise auth_exception

    return {
        'access_token': create_token(user)
    }
