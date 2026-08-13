

Trade_List = [
    {"Symbol": "NQ", "pnl": 141 },
    {"Symbol": "SP", "pnl": -40.5 },
    {"Symbol": "NQ", "pnl": 141 },
    {"Symbol": "NQ", "pnl": -102 },
    {"Symbol": "SP", "pnl": 300 },
    {"Symbol": "NQ", "pnl": -123 },
    {"Symbol": "SP", "pnl": 15.4 },
    {"Symbol": "NQ", "pnl": 234.4},
    {"Symbol": "NQ", "pnl": -51 },
    {"Symbol": "SP", "pnl": 134 },
    {"Symbol": "NQ", "pnl": -16.6 }

]


print(Trade_List[2]["pnl"])
print(Trade_List[-1]["pnl"])

gesamt = 0
for trade in Trade_List:
    gesamt += trade["pnl"]


print(f"Dein Gesamt PnL liegt bei {gesamt:.2f}€")

if gesamt > 0:
    print("Gute Trades")
else:
    print("schlechte Trades")
