from fastapi import APIRouter

from src.users.dependencies import user_dependency

router = APIRouter(
    prefix='/products',
    tags=['products'],
)


@router.get('/')
async def get_all_products(user: user_dependency):
    return {'yes': user}
