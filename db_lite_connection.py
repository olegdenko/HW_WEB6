import sqlite3, errno
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = sqlite3.connect('hw_web6.db')
        yield conn
        conn.commit()
    except errno as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
