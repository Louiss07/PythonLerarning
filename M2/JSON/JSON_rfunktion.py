import json

def lade_json(dateiname):
    try:
        with open (dateiname, "r") as datei:
            trades = json.load(datei)
        return trades
    except FileNotFoundError:
        print("Diese Datei Existiert nicht!")
        return []



trades = lade_json("afhaflaf.json")
print(trades)