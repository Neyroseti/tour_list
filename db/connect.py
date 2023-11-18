from pg8000 import connect, Cursor


def db_connect(dbname: str, user: str = 'postgres', password: str = 'postgres', host: str = 'localhost',
               port: str = '5432') -> Cursor:
    conn = connect(user=user, password=password, host=host, port=port, database=dbname)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor



