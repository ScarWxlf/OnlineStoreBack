from decouple import config
from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = None

if not config('DEBUG', True):
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{config('PG_USER')}:{config('PG_PASS')}@db:5432/{config('PG_DB')}"
    )
else:
    SQLALCHEMY_DATABASE_URL = (
        "sqlite:///db.sqlite3"
    )

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
