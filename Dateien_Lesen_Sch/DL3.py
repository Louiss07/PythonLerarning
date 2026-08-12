


def lade_trades(dateiname):
    trades = []
    with open (dateiname, "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            symbol = teile[0]
            pnl = float(teile[1])
            trades.append({"symbol": symbol, "pnl": pnl})
    return trades
    



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




trades = lade_trades("Tradejournal.txt")
Avg = avg_winn(trades)

print(f"Win-Rate: {winrate(trades):.1f} %")
print(f"Dein Average win liegt bei {Avg:.2f} €")
        


