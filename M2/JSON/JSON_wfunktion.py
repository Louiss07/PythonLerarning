import json

trades = [
    {"symbol": "NQ", "pnl": 141.0},
    {"symbol": "SP", "pnl": -40.5},
    {"symbol": "NQ", "pnl": 300.0},
    {"symbol": "SP", "pnl": -102.0},
    {"symbol": "NQ", "pnl": 15.4},
    {"symbol": "SP", "pnl": -51.0},
    {"symbol": "NQ", "pnl": 234.4},
    {"symbol": "SP", "pnl": 0.0},
    {"symbol": "NQ", "pnl": 134.0},
    {"symbol": "SP", "pnl": -16.6}
]



def speichere_json(trades, dateiname):
    with open (dateiname, "w") as datei:
        json.dump(trades, datei, indent=4)
    return 


speichere_json(trades, "Tradejournal.json")



