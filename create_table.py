from psycopg2 import Error
from db_lite_connection import connection

create_table_groups = """
CREATE TABLE IF NOT EXISTS groups (
id SERIAL PRIMARY KEY NOT NULL,
name VARCHAR(255) UNIQUE
);"""

create_table_teachers = """
CREATE TABLE IF NOT EXISTS teachers (
id SERIAL PRIMARY KEY NOT NULL,
fullname VARCHAR(255)
);"""

create_table_students = """
CREATE TABLE IF NOT EXISTS students (
id SERIAL PRIMARY KEY NOT NULL,
fullname VARCHAR(255),
group_id INTEGER,
FOREIGN KEY (group_id) REFERENCES groups (id)
);"""

create_table_subjects = """
CREATE TABLE IF NOT EXISTS subjects (
id SERIAL PRIMARY KEY NOT NULL,
name VARCHAR(255),
teacher_id INTEGER,
FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);"""

create_table_grades = """
CREATE TABLE IF NOT EXISTS grades (
id SERIAL PRIMARY KEY NOT NULL,
subject_id INTEGER,
FOREIGN KEY (subject_id) REFERENCES subjects (id),
student_id INTEGER,
FOREIGN KEY (student_id) REFERENCES students (id),
grade INTEGER,
date_of DATE
);"""


if __name__ == "__main__":
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_groups)
        c.execute(create_table_teachers)
        c.execute(create_table_students)
        c.execute(create_table_subjects)
        c.execute(create_table_grades)
        c.close()
