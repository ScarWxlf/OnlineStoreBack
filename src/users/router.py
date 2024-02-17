from fastapi import APIRouter
from sqlmodel import select

from src.auth.dependencies import db_dependency, token_dependency
from src.auth.exceptions import token_exception
from src.auth.utils import decode_jwt
from src.users.models import User
from src.users.schemas import UserOut

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
