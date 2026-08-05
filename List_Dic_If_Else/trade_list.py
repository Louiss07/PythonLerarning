

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

gesamt = Trade_List[0]["pnl"] + Trade_List[1]["pnl"] + Trade_List[2]["pnl"] + Trade_List[3]["pnl"] + Trade_List[4]["pnl"] + Trade_List[5]["pnl"] + Trade_List[6]["pnl"] + Trade_List[7]["pnl"] + Trade_List[8]["pnl"] + Trade_List[9]["pnl"]

print(f"Dein Gesamt PnL liegt bei {gesamt:.2f}€")

if gesamt > 0:
    print("Gute Trades")
else:
    print("schlechte Trades")
