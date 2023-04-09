# Загрузка библиотеки
import sqlite3

# Создание и соединение с базой данных
con = sqlite3.connect('db_build_buddy.db')
cur = con.cursor()
con.commit()

# Создание таблиц базы данных
cur.execute(""" CREATE TABLE IF NOT EXISTS objects(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        --cadastral_number INTEGER UNIQUE,
        addres TEXT UNIQUE,
        --problem_object INTEGER NOT NULL,
        document BLOB UNIQUE,
        photo BLOB UNIQUE
        --status INTEGER,
        --tracking INTEGER,
        --priority INTEGER,
        --deadline TEXT
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


# Функция: добавить данные типа BLOB
def insert_blob(arg_document, arg_foto):
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect('db_build_buddy.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO objects
                                  (document, photo) VALUES (?, ?)"""

        object_photo = convert_to_binary_data(arg_foto)
        object_document = convert_to_binary_data(arg_document)
        # Преобразование данных в формат кортежа
        data_tuple = (object_photo, object_document)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


# Тестирование: добавление blob файлов (хардкод)
insert_blob('blob_files/document_1.docx', 'blob_files/photo_1.jpg')
insert_blob('blob_files/document_2.docx', 'blob_files/photo_2.jpg')
