from typing import Optional

from sqlmodel import SQLModel, Field

from src.settings import DEFAULT_AVATAR_URL


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    username: str
    email: str = Field(unique=True)
    hashed_password: str
    image: str = Field(default=str(DEFAULT_AVATAR_URL))
