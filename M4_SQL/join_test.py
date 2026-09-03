import sqlite3
from datetime import date

conn= sqlite3.connect("schule_join.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS faecher(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    lehrer TEXT
)""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS noten_neu(
    id INTEGER PRIMARY KEY,
    fach_id INTEGER,
    note REAL,
    datum TEXT,
    art TEXT,
    FOREIGN KEY (fach_id) REFERENCES faecher(id)
)""")

conn.commit()


def fach_hinzufuegen(name, lehrer):
    cur.execute("INSERT INTO faecher (name, lehrer) VALUES (?, ?)", (name, lehrer))
    conn.commit()


def note_neu_hinzufuegen(fach_id, note, datum, art):
    cur.execute("INSERT INTO noten_neu (fach_id, note, datum, art) VALUES (?, ?, ?, ?)", (fach_id, note, datum, art))
    conn.commit()


cur.execute("""SELECT faecher.name, faecher.lehrer, ROUND(AVG(note), 2), COUNT(*)
                FROM noten_neu
                JOIN faecher ON noten_neu.fach_id = faecher.id
                GROUP BY faecher.name
                ORDER BY AVG(noten_neu.note) DESC
 """)


def noten_anzeigen_fachname():
    cur.execute("""SELECT noten_neu.note, faecher.name, noten_neu.datum, noten_neu.art
                    FROM noten_neu
                    JOIN faecher ON noten_neu.fach_id = faecher.id
         """)
    zeile = cur.fetchall()
    if not zeile:
        print("Das ist keine vorhandene id")
        return
    for z in zeile:
        print(f"Im Fach: {z[1]} hast du die Note {z[0]} am {z['datum']} in einer {z['art']} Prüfung bekommen \n")


noten_anzeigen_fachname()

conn.close()




