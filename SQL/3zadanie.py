import sqlite3
db = sqlite3.connect('exam1.db')
cur = db.cursor()

cur.execute('SELECT sum(people) FROM subjectrf WHERE name="Тыва" OR id=9 OR id = 11')
result = cur.fetchall()
print(result)

db.close

