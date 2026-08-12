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


def winrate(trades):
    gewinn = 0
    for trade in trades:
        if trade["pnl"] > 0:
            gewinn += 1
    return gewinn / len(trades) * 100


Winn_Rate = winrate(trades)

print(f"Die Gewinnrate liegt bei {Winn_Rate} Prozent")


def avg_winn(trades):
    summe = 0
    for t in trades:
        summe += t["pnl"]
    return summe / len(trades)

def lade_trades(dateiname):
    trades = []
    with open ("Tradejournal.txt", "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            symbol = teile[0]
            pnl = float(teile[1])
            trades.append({"symbol": symbol, "pnl": pnl})
        return trades
    






trades = lade_trades("Tradejournal.txt")


Avg = avg_winn(trades)
print(f"Win-Rate: {winrate(trades):.1f} %")
print(f"Dein Average win liegt bei {Avg:.2f} €")
        