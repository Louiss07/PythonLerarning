import sqlite3

conn = sqlite3.connect("noten_test.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS noten(
    id INTEGER PRIMARY KEY,
    fach TEXT,
    note REAL,
    datum TEXT,
    art TEXT
    )""")
conn.commit()

def noten_hinzufuegen(fach, note, datum, art):
    cur.execute("INSERT INTO noten (fach, note, datum, art) VALUES (?, ?, ?, ?)", (fach, note, datum, art))
    conn.commit()


noten_hinzufuegen("Bio", 2.6, "2026-09-04", "Mündlich")
noten_hinzufuegen("Erdkunde", 2.1, "2026-09-03", "Schriftlich")
noten_hinzufuegen("Mathe", 2.4, "2026-09-10", "Schriftlich")
noten_hinzufuegen("English", 2.8, "2026-09-11", "Mündlich")
noten_hinzufuegen("Deutsch", 4.0, "2026-09-07", "Schriftlich")
noten_hinzufuegen("Mathe", 2.9, "2026-09-10", "Schriftlich")
noten_hinzufuegen("Mathe", 2.1, "2026-09-10", "Schriftlich")
noten_hinzufuegen("Mathe", 2.2, "2026-09-10", "Schriftlich")
noten_hinzufuegen("Mathe", 3.5, "2026-09-10", "Schriftlich")


cur.execute(""" SELECT fach, note
                FROM noten
                WHERE fach = 'Mathe'
                ORDER BY note DESC
                LIMIT 3
""")
print(cur.fetchall())

conn.close()

