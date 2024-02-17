from fastapi import HTTPException, status

auth_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Incorrect email or password',
)

token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
)

token_time_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Token has been expired',
)
