inventar = [
    {"name": "Schwert",  "wert": 50.0,  "gewicht": 3.0},
    {"name": "Trank",    "wert": 20.0,  "gewicht": 0.5},
    {"name": "Rüstung",  "wert": 150.0, "gewicht": 8.0},
    {"name": "Schild",   "wert": 80.0,  "gewicht": 5.0},
    {"name": "Fackel",   "wert": 5.0,   "gewicht": 1.0}
]


def gesamtwert(inventar):
    summe = 0
    for item in inventar:
        summe += item["wert"]
    return summe

wert = gesamtwert(inventar)

print(f"Gesamtwert: {wert:.2f} Gold")
