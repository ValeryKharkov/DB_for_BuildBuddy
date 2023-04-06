import sqlite3 as sl

# открытие файла с базой данных
con = sl.connect('build_buddy.db')

# создание таблицы
with con:
    con.execute("""
        CREATE TABLE objects (
        id integer primary key,
        cadastral_number integer primary key,
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