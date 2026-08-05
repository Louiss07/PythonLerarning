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
gewinner = 0
verlierer = 0
brake_even = 0

for trade in Trade_List:
    if trade["pnl"] > 0:
        gewinner += 1
    elif trade["pnl"] < 0:
        verlierer += 1
    elif trade["pnl"] == 0:
        brake_even += 1

Win_Rate = gewinner / len(Trade_List) * 100


print(f"Du hast {gewinner} Trades Gewonnen")
print(f"Du hast {verlierer} Trades Veroren")
print(f"Du hast {brake_even} Trades Brake even gehittet")
print(f"Deine Winnrate liegt bei {Win_Rate:.1f} % auf {len(Trade_List)} Trades")