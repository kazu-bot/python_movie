import sqlite3

conn = sqlite3.connect('test_sqlite.db')

#sqlite側でメモリ上に一時テーブルを作成することができる。
#試験的にやるならこっちでやる。
conn = sqlite3.connect(':memory')

curs = conn.cursor()
# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRONG)'
# )
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("Mike")'
# )
# conn.commit()

curs.execute(
             'SELECT * FROM persons'
)
print(curs.fetchall())
curs.close()
conn.close()