# import sqlite3

# db = sqlite3.connect('1zadan.db')

# cur = db.cursor()


# cur.execute('''  CREATE TABLE naselenie(
# id INTEGER PRIMARY KEY,
# oblast TEXT NOT NULL,
# goroda INTEGER DEFAULT 0,
# people INTEGER DEFAULT 0
# )''')

# cur.execute('INSERT INTO naselenie (oblast,people,goroda) VALUES (?,?,?)',['Новосибирская',2785836,7])

# cur.execute('INSERT INTO naselenie (oblast,people,goroda) VALUES (?,?,?)',['Омская',2785836,6])


# db.commit()

cur.execute('SELECT * FROM naselenie')
result = cur.fetchall()
print(result)

db.close()