import json

trades = [
    {"symbol": "NQ", "pnl": 141.0},
    {"symbol": "SP", "pnl": -40.5},
    {"symbol": "NQ", "pnl": 300.0}
]

with open ("trades.json", "w") as datei:
    json.dump(trades, datei, indent=4)
    