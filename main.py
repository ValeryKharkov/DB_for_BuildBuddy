import sqlite3 as sl

# открытие файла с базой данных
con = sl.connect('build_buddy.db')

# открытие базы
with con:
    # получение количества таблиц с нужным нам именем
    data = con.execute("select count(*) from sqlite_master where type='table' and name='objects'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:

            # создание таблицы
            with con:
                con.execute("""
                    CREATE TABLE objects (
                    id integer primary key,
                    cadastral_number integer,
                    addres varchar(20),
                    problem_object integer,
                    document_link varchar(20),
                    foto_link varchar(20),
                    status integer,
                    tracking integer,
                    priority varchar(20),
                    deadline date
                    );
                """)

# определение множественного запроса
sql = 'insert into objects (id, cadastral_number, addres, problem_object, document_link, foto_link, status, tracking, priority, deadline) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

# определение данных для запроса
data = [
    (1, 47141203001814, 'Полюстровский проспект, д.19, корп.1', 1, 'www.documentlink.ru/pol', 'www.fotolink.ru/pol', 0, 1, 'hard', '2023-10-07'),
    (2, 47141205001815, 'Пискарёвский проспект, д.2, корп.А', 0, 'www.documentlink.ru/pis', 'www.fotolink.ru/pis', 1, 1, 'medium', '2023-07-09'),
    (3, 47151505001816, 'Проспект металлистов, д.14, корп.8', 0, 'www.documentlink.ru/met', 'www.fotolink.ru/met', 1, 0, 'light', '2023-08-09'),
]

# добавление всех данных сразу
with con:
    con.executemany(sql, data)

# вывод содержимого таблицы на экран
with con:
    data = con.execute('SELECT * FROM objects')
    for row in data:
        print(row)