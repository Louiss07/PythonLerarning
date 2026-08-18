from datetime import datetime


wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

tag_pnl = {"Montag": 0, "Dienstag": 0, "Mittwoch": 0, "Donnerstag": 0, "Freitag": 0, "Samstag": 0, "Sonntag": 0}

schlechtester_tag = ""
schlechtester_wert = 99999

trades = [
    {"symbol": "NQ", "pnl": 141.0, "date": "2026-08-17"},
    {"symbol": "SP", "pnl": -40.5, "date": "2026-08-17"},
    {"symbol": "NQ", "pnl": 300.0, "date": "2026-08-18"},
    {"symbol": "SP", "pnl": -102.0, "date": "2026-08-18"},
    {"symbol": "NQ", "pnl": 15.4, "date": "2026-08-19"},
    {"symbol": "SP", "pnl": -51.0, "date": "2026-08-19"},
    {"symbol": "NQ", "pnl": 234.4, "date": "2026-08-20"},
    {"symbol": "SP", "pnl": 0.0, "date": "2026-08-20"},
    {"symbol": "NQ", "pnl": 134.0, "date": "2026-08-21"},
    {"symbol": "SP", "pnl": -16.6, "date": "2026-08-21"}
]

for t in trades:
    text = t["date"]
    d = datetime.strptime(text ,"%Y-%m-%d").date()
    print(f"{t['symbol']} mit dem pnl {t['pnl']} war ein {wochentage[d.weekday()]}")


for p in trades:
    d = datetime.strptime(p["date"],"%Y-%m-%d").date()
    tag = wochentage[d.weekday()]
    tag_pnl[tag] += p["pnl"]
    

for tag, wert in tag_pnl.items():
    if wert < schlechtester_wert:
        schlechtester_wert = wert
        schlechtester_tag = tag

print(f"Schlechtester Tag: {schlechtester_tag} mit {schlechtester_wert:.2f}€")





