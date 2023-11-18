from pg8000 import Cursor

from .connect import db_connect
from .create_tables import create_tables


def init(dbname: str, user: str = 'postgres', password: str = 'postgres', host: str = 'localhost',
         port: str = '5432') -> Cursor:
    cursor = db_connect(dbname, user, password, host, port)
    create_tables(cursor)

    return cursor
