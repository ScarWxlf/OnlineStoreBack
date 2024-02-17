from fastapi import FastAPI, APIRouter
from sqlmodel import SQLModel

from src.auth.router import router as auth_router
from src.database import engine
from src.users.router import router as user_router

app = FastAPI()

SQLModel.metadata.create_all(bind=engine)

api_router = APIRouter(prefix='/api')

api_router.include_router(auth_router)
api_router.include_router(user_router)

app.include_router(api_router)
