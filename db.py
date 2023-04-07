# Загрузка библиотеки
import sqlite3 as sl

# Создание и соединение с базой данных
con = sl.connect('db.db')

cur = con.cursor()

# Создание таблиц базы данных
cur.execute(""" CREATE TABLE IF NOT EXISTS objects(
                    id integer primary key,
                    cadastral_number integer,
                    addres text,
                    problem_object integer,
                    document_link text,
                    foto_link text,
                    status integer,
                    tracking integer,
                    priority text,
                    deadline date
                    );
""")
con.commit()


# Добавление данных
# data = []
# cur.executemany("INSERT OR IGNORE INTO objects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", data)
# con.commit()

# Добавление данных
def db_table_val(id: int, cadastral_number: int, addres: str, problem_object: int, document_link: str, foto_link: str, status: int, tracking: int, priority: str, deadline: str):
	    cur.execute("""INSERT INTO objects (id, cadastral_number, addres, problem_object, document_link, foto_link, status, tracking, priority, deadline) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (id, cadastral_number,addres, problem_object, document_link, foto_link, status, tracking, priority, deadline))
con.commit()



