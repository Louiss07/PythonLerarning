import sqlite3

conn = sqlite3.connect("noten_test.db")
cur = conn.cursor()
art = "Schriftlich"
cur.execute(""" SELECT fach, COUNT(*),
                ROUND(AVG(note), 2)
                FROM noten
                WHERE art = ? COLLATE NOCASE
                GROUP BY fach
                HAVING COUNT(*) >= 2
                ORDER BY AVG(note) DESC



""",(art, ))



print(cur.fetchall())

conn.close()