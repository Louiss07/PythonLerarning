def winrate(trades):
    gewinn = 0
    for trade in trades:
        if trade["pnl"] > 0:
            gewinn += 1
    return gewinn / len(trades) * 100


def avg_winn(trades):
    summe = 0
    for t in trades:
        summe += t["pnl"]
    return summe / len(trades)

def lade_trades(dateiname):
    trades = []
    with open (dateiname, "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            symbol = teile[0]
            pnl = float(teile[1])
            trades.append({"symbol": symbol, "pnl": pnl})
    return trades
    




#

if __name__ == "__main__":
    # Dieser Code läuft NUR, wenn die Datei direkt gestartet wird
    # NICHT, wenn sie importiert wird
    test_trades = [
    {"symbol": "NQ", "pnl": 100.0},
    {"symbol": "NQ", "pnl": 45.0},
    {"symbol": "NQ", "pnl": 24.0},
    {"symbol": "NQ", "pnl": -56.0}
]


    print(winrate(test_trades))