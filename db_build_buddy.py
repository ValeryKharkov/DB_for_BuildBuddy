# Загрузка библиотеки
import sqlite3

# Создание и соединение с базой данных
con = sqlite3.connect('db_build_buddy.db')
cur = con.cursor()
con.commit()

# Создание таблиц базы данных
cur.execute(""" CREATE TABLE IF NOT EXISTS objects(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        cadastral_number INTEGER UNIQUE,
        addres TEXT UNIQUE,
        status_problem INTEGER NOT NULL,
        document BLOB UNIQUE,
        photo BLOB UNIQUE,
        status_execution INTEGER,
        tracking INTEGER,
        priority INTEGER,
        deadline TEXT
        );
""")
con.commit()


# Добавление данных в таблицу (хардкод)
# data = [
#     ('Кондратьевский просп., 44', '...', '...'),
#     ('Полюстровский просп., 18', '...', '...')
# ]
#
# cur.executemany("""INSERT OR IGNORE INTO objects VALUES (?, ?, ?, ?);""", data)
# con.commit()


# Добавление данных через функцию def db_table_val(id: int, cadastral_number: int, addres: str, problem_object: int,
# document: str, foto: str, status: int, tracking: int, priority: str, deadline: str): cur.execute("""INSERT INTO
# objects ( id, cadastral_number, addres, problem_object, document_link, foto_link, status, tracking, priority,
# deadline) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (id, cadastral_number, addres, problem_object, document, foto,
# status, tracking, priority, deadline)) con.commit()

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
def add_object(arg_addres: int):
    con = sqlite3.connect('db_build_buddy.db')
    cur = con.cursor()
    data = []
    data.append(arg_addres)
    cur.execute("""INSERT OR IGNORE INTO objects(addres) VALUES(?)""", data)
    con.commit()
    cur.close()


# Функция: просмотр добавленных объектов
def view_object():
    pass


# Функция: конвертация изображений и файлов в бинарные данные
def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


# Функция: добавить данные в таблицу
def insert_data_to_the_table(arg_cadastral_number, arg_addres, arg_status_problem, arg_document, arg_photo,
                             arg_status_execution, arg_tracking, arg_priority, arg_deadline):
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('db_build_buddy.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT OR IGNORE INTO objects
                                  (cadastral_number, addres, status_problem, document, photo,
                             status_execution, tracking, priority, deadline) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        document_mod = convert_to_binary_data(arg_document)
        photo_mod = convert_to_binary_data(arg_photo)
        # Преобразование данных в формат кортежа
        data_tuple = (arg_cadastral_number, arg_addres, arg_status_problem, document_mod, photo_mod,
                      arg_status_execution, arg_tracking, arg_priority, arg_deadline)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        print("Данные успешно вставлены в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


# Тестирование: добавление blob файлов (хардкод)
insert_data_to_the_table(47141203001814, 'Проезд Смольный, д. 1, лит. Б.', 1, 'blob_files/document_1.docx',
                         'blob_files/photo_1.jpg', 1, 1, 1, '24.05.2023')
insert_data_to_the_table(84141203001815, 'Лахтинский проспект, 2 к3 ст1', 0, 'blob_files/document_2.docx',
                         'blob_files/photo_2.jpg', 0, 0, 0, '06.10.2024')
