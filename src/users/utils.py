import re
from enum import Enum

from fastapi import UploadFile
from passlib.context import CryptContext
from sqlmodel import select

from src.auth.dependencies import db_dependency
from src.dependencies import image_extends_exception
from src.settings import UPLOAD_AVATAR
from src.users.models import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


valid_image_extends = [
    'jpg',
    'png',
    'jpeg'
]


def get_user_by_email(email: str, db: db_dependency):
    stat = select(User).where(User.email == email)
    user = db.exec(stat).first()
    return user


def get_hashed_password(password: str):
    return pwd_context.hash(password)


def password_validation(password: str):
    password_regex = r"((?=.*\d)(?=.*[a-z]).{8,64})"
    return re.match(password_regex, password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def check_valid_extends(filename: str):
    image_extend = filename.split('.')[-1]
    if image_extend not in valid_image_extends:
        raise image_extends_exception
    return image_extend


async def save_image(image: UploadFile, file_name: str):
    image = await image.read()

    path = f"/{UPLOAD_AVATAR}/{file_name}"

    with open(path, "wb") as f:
        f.write(image)
