class Journal:
    def __init__(self):
        self.trades = []


    def add_trade(self, symbol, pnl):
        self.trades.append({"symbol": symbol, "pnl": pnl})


j = Journal()
j.add_trade("NQ", 141)
j.add_trade("SP", -40.5)
print(j.trades)
