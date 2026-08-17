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


verluste = [ t for t in trades if t["pnl"] < 0]

pnl = sum([t["pnl"] for t in trades ])

gewinner = len([t["pnl"] for t in trades if t["pnl"] > 0])

reihenfolge = sorted([i["pnl"] for i in trades], reverse=True)

for i, trade in enumerate(trades, 1):
    print(f"Trade {i}: {trade['symbol']}, {trade['pnl']}")



print(f"Gesamt-P&L: {pnl}")
print(f"Verlust-Trades: {verluste}")
print(f"Gewinner-Anzahl: {gewinner}")
print(f"Sortierte pnl: {reihenfolge}")
