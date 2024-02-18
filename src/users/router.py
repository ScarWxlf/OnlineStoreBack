from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, UploadFile, Form
from sqlmodel import select

from src.auth.dependencies import db_dependency, token_dependency
from src.auth.exceptions import token_exception
from src.auth.utils import decode_jwt
from src.settings import UPLOAD_AVATAR_URL
from src.users.dependencies import user_dependency
from src.users.models import User
from src.users.schemas import UserOut, UserChange
from src.users.utils import save_image, check_valid_extends

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/', response_model=list[UserOut])
async def get_users(db: db_dependency, token: token_dependency):
    if not decode_jwt(token):
        raise token_exception
    stat = select(User)
    result = db.exec(stat).all()
    return result


@router.get('/me/', response_model=UserOut)
async def get_current_user(user: user_dependency):
    return user


@router.patch('/me/', response_model=UserOut)
async def change_user(
        user: user_dependency,
        db: db_dependency,
        username: Annotated[str, Form()] = None,
        image: UploadFile = None,
):
    if username is not None:
        user_data = UserChange(username=username)
        user.username = user_data.username

    if image is not None:
        image_extends = check_valid_extends(image.filename)

        file_name = f'{uuid4()}.{image_extends}'

        await save_image(image, file_name)
        user.image = f"{UPLOAD_AVATAR_URL}{file_name}/"

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
