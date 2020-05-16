import mysql.connector

#mysqlのバージョン8.0からは認証方式が変わっているため、コンソールで下記のようなコマンドを打つ
#userの認証方式書き換え
#alter user kazu@localhost identified with mysql_native_password by ‘kazu’;
conn = mysql.connector.connect(
    user='root',
    password='password',
    host='localhost',
    database='test_mysql_database'
    )
cursor = conn.cursor()
#
# cursor.execute('CREATE DATABASE test_mysql_database')

# cursor.execute(
#     'CREATE TABLE persons('
#     'id int NOT NULL AUTO_INCREMENT,'
#     'name varchar(14) NOT NULL,'
#     'PRIMARY KEY(id))'
# )

cursor.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.close()
conn.close()