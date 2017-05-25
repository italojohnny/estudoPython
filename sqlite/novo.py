import sqlite3

def insert (tuple_values):
    conn = None
    try:
        conn = sqlite3.connect("arquivo.db")
        sql = "INSERT INTO latlng (id, latitude, longitude, dtRegister, numSats, altitude, horizontalDil)\
                VALUES (?, ?, ?, ?, ?, ?, ?);"
        cursor = conn.cursor()
        cursor.execute(sql, tuple_values)
        conn.commit()

    except Exception as e:
        print e

    finally:
        if conn: conn.close()

if __name__ == "__main__":

    tuple_values = (2, 2.6, 3.1, None, 6.5, 8.7, 2.9)
    insert(tuple_values)
