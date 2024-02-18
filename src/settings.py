from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_AVATAR = BASE_DIR / 'upload/images/users'
UPLOAD_AVATAR_URL = '/media/users/'

DEFAULT_AVATAR = UPLOAD_AVATAR / 'default.jpg'
DEFAULT_AVATAR_URL = UPLOAD_AVATAR_URL + 'default.jpg/'

ALGORYTHM = config("ALGORYTHM")
SECRET_KEY = config("SECRET_KEY")
ACCESS_TOKEN_EXPIRES_DAY = 14
