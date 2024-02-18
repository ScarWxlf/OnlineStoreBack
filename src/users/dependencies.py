from typing import Annotated

from fastapi import Depends

from src.auth.dependencies import token_dependency, db_dependency
from src.auth.exceptions import token_exception
from src.auth.utils import decode_jwt
from src.users.utils import get_user_by_email


def get_user_by_token(token: token_dependency, db: db_dependency):
    payload = decode_jwt(token)
    user_email = payload.get('email')
    if not user_email:
        raise token_exception
    user = get_user_by_email(user_email, db)
    return user


user_dependency = Annotated[get_user_by_token, Depends()]
