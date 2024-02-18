from fastapi import HTTPException, status


image_extends_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='Invalid image extends. Accepting only (JPG, JPEG, PNG)'
)
