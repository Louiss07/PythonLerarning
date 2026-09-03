import sqlite3

conn = sqlite3.connect("noten.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

with conn:
    cur.execute("""CREATE TABLE IF NOT EXISTS faecher (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            lehrer TEXT
 )""")



cur.execute("DELETE FROM faecher")
conn.commit()

cur.execute("SELECT DISTINCT fach FROM noten")
faecher_liste = cur.fetchall()



with conn:
   for z in faecher_liste:
       cur.execute("INSERT INTO faecher (name) VALUES (?)",(z['fach'],))


#cur.execute("ALTER TABLE noten ADD COLUMN fach_id INTEGER")
#conn.commit()
#cur.execute("SELECT id, name FROM faecher")
#faecher_l = cur.fetchall()
#with conn:
    #for f in faecher_l:
        #cur.execute("UPDATE noten SET fach_id = ? WHERE fach = ?", (f['id'], f['name']))

#cur.execute("SELECT COUNT(*) AS anzahl FROM noten")
#print("Noten gesamt:", cur.fetchone()["anzahl"])

#cur.execute("""SELECT COUNT(*) AS anzahl
               #FROM noten
               #JOIN faecher ON noten.fach_id = faecher.id""")
#print("Noten mit gültigem Fach:", cur.fetchone()["anzahl"])

#cur.execute("SELECT * FROM noten")
#for zeile in cur.fetchall():
    #print(dict(zeile))


    



conn.close()

