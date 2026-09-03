import sqlite3

conn = sqlite3.connect("noten_test.db")
cur = conn.cursor()

fach = "mathe"

cur.execute("""SELECT id, fach, note, datum, art
                FROM noten
                WHERE fach = ? COLLATE NOCASE
                AND note <= 3
                ORDER BY note DESC
                """,(fach,))

liste = cur.fetchall()
for zeile in liste:
    print(f"{zeile[0]}: Das Fach {zeile[1]} mit der note {zeile[2]} am {zeile[3]} in einer {zeile[4]} prüfung")

conn.close()