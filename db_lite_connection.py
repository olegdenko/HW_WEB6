from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='hw_web6.db')
        yield conn
        conn.commit()
    except Error as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
