import psycopg2
from psycopg2 import Error

try:
    
    connection = psycopg2.connect(
        user="postgres",
        password="1488",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )
    cursor = connection.cursor()

    cursor.execute("select * from product")
    row = cursor.fetchall()
    print(row)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
