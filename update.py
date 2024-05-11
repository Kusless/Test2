import psycopg2
from psycopg2 import Error

name = input("Введите имя таблицы ")
column = input("Введите имя столбца ")
new = input("Введите новое значение ")
id = input("Введите ID ")
query = f"""update {name} set {column} = '{new}' where id = {id} """
try:
    connection = psycopg2.connect(
        user="postgres",
        password="1488",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )

    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
        print("Данные изменены")
