import sqlite3
# Создание базы 
db = sqlite3.connect('sql_20.db')
cur = db.cursor()


db.execute("PRAGMA foreign_keys = 1")
# cur.execute('''CREATE TABLE facultets(
# id INTEGER PRIMARY KEY, 
# name TEXT NOT NULL,
# date INTEGER NOT NULL,
# boss TEXT NOT NULL
#  ) ''')

# cur.execute('''CREATE TABLE student123(
# id INTEGER PRIMARY KEY, 
# fio TEXT NOT NULL,
# city TEXT NOT NULL,
# year INTEGER NOT NULL,
# facultet_id INTEGER NOT NULL,
# FOREIGN KEY(facultet_id) REFERENCES facultets(id)
#  ) ''')
 

# cur.execute('INSERT INTO facultets (name,date,boss) VALUES (?,?,?)',['Программирование',2010,'Смирнов Анатолий Сергеевич'])
# cur.execute('INSERT INTO facultets (name,date,boss) VALUES (?,?,?)',['Администрирование',2002,'Иванов Иван Александрович'])

db.commit()

cur.execute('SELECT * FROM facultets')
result = cur.fetchall()
print(result)


db.close()