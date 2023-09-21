import unittest
from db_connection import connection

from change_to_table import connection, change_table_users


class MyTestCase(unittest.TestCase):

    def get_connection_and_cursor(self):
        conn = connection()
        cursor = conn.cursor()
        return conn, cursor

    def close_connection_and_cursor(self, conn, cursor):
        cursor.close()
        conn.close()

    def test_add_column_to_users_table(self):
        with connection() as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("ALTER TABLE users ADD COLUMN test_column VARCHAR(25);")
                conn.commit()
            finally:
                cursor.close()


if __name__ == '__main__':
    unittest.main()
