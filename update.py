import psycopg2
from psycopg2 import Error
name = input('Введите имя таблицы ') 
column = input('Введите имя стобца ') 
new = input('Введите новые данные ')       
try:
    connection = psycopg2.connect(user="postgres",
                                  password="1488",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
   
    cursor.execute("update  %s set %s  = %s + 5 ",(name,column,new ))
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
        print('Данные изменены')
