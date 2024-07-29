import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT name, age FROM users WHERE age > 30;"
try:
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print('Пользователи старше 30 лет:')
        for name, age in results:
            print(f'Имя: {name} Возраст:{age}')
    else:
        print('Пользователей старше 30 нет')
except sqlite3.Error as e:
    print(f'Ошибка при выполнении запроса: {e}')
finally:
    cursor.close()
    conn.close()