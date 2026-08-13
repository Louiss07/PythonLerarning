def speichere_trade(symbol, pnl):
    with open("Tradejournal.txt", "a") as datei:
        datei.write(f"{symbol},{pnl}\n")
    

speichere_trade("NQ", 141.0)
speichere_trade("SP", -40.5)
speichere_trade("NQ", -16)
speichere_trade("SP", 134.0)


