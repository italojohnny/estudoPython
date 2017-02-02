import sqlite3


result = []
conn = sqlite3.connect("arquivo.db")
try:
    sql = "SELECT id, latitude, longitude, dtRegister, numSats, altitude, horizontalDil \
        FROM latlng \
        ORDER BY datetime(dtRegister) DESC LIMIT 1"
    row = conn.cursor().execute(sql).fetchone()
    if row:
        print(row)

finally:
    conn.close()


