import uvicorn
from fastapi import FastAPI, APIRouter
from sqlmodel import SQLModel

from src.auth.router import router as auth_router
from src.database import engine
from src.users.router import router as user_router
from src.products.router import router as product_router

app = FastAPI(
    docs_url='/api/docs',
)

SQLModel.metadata.create_all(bind=engine)

api_router = APIRouter(prefix='/api')

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(product_router)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
