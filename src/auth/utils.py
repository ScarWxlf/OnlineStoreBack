from datetime import datetime, timedelta

from jose import jwt, ExpiredSignatureError, JWTError

from src import settings
from src.auth.exceptions import token_exception
from src.users.models import User


def create_token(user: User):
    current_datetime = datetime.now()

    data = {
        'email': user.email,
        'id': user.id,
        'exp': current_datetime + timedelta(days=settings.ACCESS_TOKEN_EXPIRES_DAY)
    }

    encoded_jwt = jwt.encode(
        data,
        settings.SECRET_KEY,
        algorithm=settings.ALGORYTHM,
    )

    return encoded_jwt


def decode_jwt(token: str):
    try:
        decoded_jwt = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORYTHM])
    except ExpiredSignatureError:
        raise token_exception
    except JWTError:
        raise token_exception
    return decoded_jwt
