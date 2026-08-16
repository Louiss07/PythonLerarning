class Trade: 
    def __init__(self, symbol, pnl):
        self.symbol = symbol
        self.pnl = pnl

mein_trade = Trade("NQ", 141.0)

print(mein_trade.symbol)
print(mein_trade.pnl)
