# Загрузка библиотеки
import sqlite3 as sl

# Создание и соединение с базой данных
con = sl.connect('db_build_buddy.db')
cur = con.cursor()

# Создание таблиц базы данных
cur.execute(""" CREATE TABLE IF NOT EXISTS objects(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        cadastral_number INTEGER UNIQUE,
        addres TEXT UNIQUE,
        problem_object INTEGER NOT NULL,
        document TEXT UNIQUE,
        foto TEXT UNIQUE,
        status INTEGER,
        tracking INTEGER,
        priority INTEGER,
        deadline TEXT);
""")
con.commit()

# Добавление данных в таблицу (хардкод)
data = [
    (1, 47141203001814, 'Кондратьевский просп., 44', 1, '...', '...', 0, 1, 1, '23/10/2025'),
    (2, 47141203001815, 'Полюстровский просп., 18', 0, '...', '...', 1, 1, 0, '16/08/2024')
]

cur.executemany("""INSERT OR IGNORE INTO objects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", data)
con.commit()


# Добавление данных через функцию
# def db_table_val(id: int, cadastral_number: int, addres: str, problem_object: int, document: str, foto: str,
#                  status: int, tracking: int, priority: str, deadline: str):
#     cur.execute("""INSERT INTO objects (
#     id, cadastral_number, addres, problem_object, document_link, foto_link, status, tracking, priority, deadline) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#         (id, cadastral_number, addres, problem_object, document, foto, status, tracking, priority, deadline))
# con.commit()

# Функция: поиск объекта
def search_object(text, search_type):
    object_info = []  # готовим выходное представление
    sql = ''  # инициализируем базу данных
    # здесь поиск по базе
    if search_type == 'номер':
        pass  # алгоритм поиска по кадастровому номеру в БД
    elif search_type == 'адрес':
        pass  # алгоритм поиска по адресу в БД
    if text in sql:  # готовим нужный вариант вывода, если text в базе
        object_info.append(0)
        object_info.append('данные из БД')
    else:  # если в БД не находится нужный объект, выдаём код ошибки
        object_info.append(1)
    return object_info


# Функция: добавить объект
def add_object(id: int):
    con = sl.connect('db_build_buddy.db')
    cur = con.cursor()
    data = []
    data.append(id)
    cur.execute("""INSERT INTO shop VALUES(?)""", data)
    con.commit()
    cur.close()


# Функция: просмотр добавленных объектов
def view_object():
    pass


# Вывод данных для тестирования
cur.execute("""SELECT * FROM objects""")
result = cur.fetchall()
print(result)
