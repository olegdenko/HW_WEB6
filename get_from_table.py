"""Для отримання результату запроса до бази данних
 потрібно запустити бробку з аргументом у якості якого вказати файл
   з інструкціями SQL. Example: 'py get_from_table.py query_11.sql'"""
import pprint
import sys
from db_lite_connection import connection


def main():
    try:
        if len(sys.argv) != 2:
            print('Usage: python your_script.py your_query.sql')
            sys.exit(1)

        with open(sys.argv[1], 'r', encoding='utf-8') as fh:
            sql_query = fh.read()

            # Перемістіть покажчик файлу на початок
            fh.seek(0)

            for line in fh:
                if "--" in line:
                    comment = line.split("--")[1]
                    print("Comment:", comment.strip())

        with connection() as conn:
            c = conn.cursor()
            c.execute(sql_query)
            pprint.pprint(c.fetchall())
            c.close()
    except FileNotFoundError as err:
        print('File not found:', err)
    except Exception as err:
        print('An error occurred:', err)


if __name__ == "__main__":
    main()
