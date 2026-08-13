from trade_tools import winrate, avg_winn, lade_trades

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

print(f"Win-Rate: {winrate(trades):.1f}%")
print(f"Average: {avg_winn(trades):.2f}€")
print(f"{lade_trades('Tradejournal.txt')}\n")