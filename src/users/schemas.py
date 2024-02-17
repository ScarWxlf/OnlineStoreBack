from pydantic import BaseModel, EmailStr, field_validator

from src.users.utils import password_validation


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserIn(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, password):
        if not password_validation(password):
            raise ValueError("Password is to week")
        return password


class UserInDB(UserBase):
    hashed_password: str


class UserOut(UserBase):
    id: int
    image: str


class UserOutReg(BaseModel):
    id: int
    username: str
    image: str
    access_token: str
