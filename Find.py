import psycopg2
from psycopg2 import Error

id = input('Введите ID ')
try:
    connection = psycopg2.connect(
        user="postgres",
        password="1488",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )

    cursor = connection.cursor()
    cursor.execute(f"select * from product where id = '{id}' ")
    row = cursor.fetchone()
    print(row)
    

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
