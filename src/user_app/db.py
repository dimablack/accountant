import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
db.custom_schema = os.environ.get('USER_APP_DB_SCHEMA', 'user_app')


class CustomSchema():
    """Custom schema class"""
    CUSTOM_SCHEMA = os.environ.get('USER_APP_DB_SCHEMA', 'user_app')
