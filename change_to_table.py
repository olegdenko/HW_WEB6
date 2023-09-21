# from psycopg2 import Error
import pprint
from db_connection import connection
from faker import Faker

fake = Faker('uk-UA')
change_table_users = """
ALTER TABLE users ADD COLUMN phone_number VARCHAR(25);"""


if __name__ == "__main__":
    with connection() as conn:
        c = conn.cursor()
        # c.execute(simple_select, (10,))
        # print(c.fetchone())
        c.execute(change_table_users)
        c.close()
