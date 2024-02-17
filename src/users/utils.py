import re

from passlib.context import CryptContext
from sqlmodel import select

from src.auth.dependencies import db_dependency
from src.users.models import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


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
