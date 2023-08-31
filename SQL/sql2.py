# Cвязанные
import sqlite3
# Создание базы 
db = sqlite3.connect('sql_20.db')
cur = db.cursor()

# # Создание первой таблицы       Имя 
# cur.execute('''CREATE TABLE userBank(
# id INTEGER PRIMARY KEY,
# name text NOT NULL,
# numCart INTEGER NOT NULL 

# )''')


## Cоздание второй таблицы 
# cur.execute(''' CREATE TABLE trans (

#  id INTEGER PRIMARY KEY,
#  user_id INTENGER NOT NULL,
#  shop text NOT NULL,
#  money INTEGER NOT NULL,
## Конектим к таблице что           к кому 
#  FOREIGN KEY (user_id) REFERENCES userBank(id)
# ) 
# ''') 
#            Данные ввод                  Куда         Надо       Кто 
# cur.execute('INSERT INTO userBank (name,numCart) VALUES(?,?) ',['Vsafasy',1235]) 
# # Добавляем 
# db.commit
#         Выбрать *(всё) Где  и название
cur.execute('SELECT * FROM userBank')
result = cur.fetchall()
print(result)

db.close()