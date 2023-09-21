# from psycopg2 import Error
import pprint
from db_connection import connection
from faker import Faker

fake = Faker('uk-UA')
simple_select = """
SELECT * FROM users WHERE id=%s;"""

select_regex = """
    SELECT id, name, email
    FROM users
    WHERE name SIMILAR TO '%(рій|ко)%'
    ORDER BY name
    LIMIT 10;
"""
select = """
    SELECT id, name, email
    FROM users
    WHERE age > 45
    ORDER BY name, age DESC
    LIMIT 10;
    """

if __name__ == "__main__":
    with connection() as conn:
        c = conn.cursor()
        # c.execute(simple_select, (10,))
        # print(c.fetchone())
        c.execute(select_regex)
        pprint.pprint(c.fetchall())
        c.close()
