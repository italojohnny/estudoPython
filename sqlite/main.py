import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE stocks (\
            date text, \
            trans text,\
            symbol text,\
            qty real,\
            price real\
        );")

cursor.execute("INSERT INTO stocks VALUES ('2006-12-25', 'BUY', 'RHAT', 102, 68.14);")
cursor.execute("INSERT INTO stocks VALUES ('2006-12-24', 'BUY', 'RHAT', 101, 47.14);")
cursor.execute("INSERT INTO stocks VALUES ('2006-12-23', 'BUY', 'RHAT', 104, 38.14);")
conn.commit()

cursor.execute("SELECT * FROM stocks");
print(cursor.fetchone())
print(cursor.fetchall())

# http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
