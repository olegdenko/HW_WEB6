from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='cornelius.db.elephantsql.com', user='fopwhyax',
                       database='fopwhyax', password='A7tLGSCso6pdYIfwtB423s9ZHflD2MLg')
        yield conn
        conn.commit()
    except Error as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
