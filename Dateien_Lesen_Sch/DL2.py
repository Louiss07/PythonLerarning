with open ("Tradejournal.txt", "r") as datei:
    inhalt = datei.read()
    zeile = "NQ,141.0"
    teile = zeile.split(",")
    symbol = teile[0]
    pnl = float(teile[1])

    print(pnl, symbol)  