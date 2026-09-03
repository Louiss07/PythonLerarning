import sqlite3

conn = sqlite3.connect("noten_test.db")
cur = conn.cursor()


cur.execute(""" SELECT * FROM noten

""")

print(cur.fetchall())


fach = "testfach"
cur.execute("INSERT INTO noten (fach) VALUES (?)",(fach,))
conn.commit()



cur.execute(""" SELECT * FROM noten WHERE fach = 'testfach'

""")

print(cur.fetchall())


cur.execute("""DELETE FROM noten
                WHERE fach = 'testfach'

""")

conn.commit()




print(cur.rowcount)
conn.close()