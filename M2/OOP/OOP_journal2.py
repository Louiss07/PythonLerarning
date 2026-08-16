class Journal:
    def __init__(self):
        self.trades = []


    def add_trade(self, symbol, pnl):
        self.trades.append({"symbol": symbol, "pnl": pnl})


    def stats(self):
        if len(self.trades) == 0:
            return "Keine Trades im Journal"

        gewinner = 0
        summe = 0

        for trade in self.trades:
            summe += trade["pnl"]
            if trade["pnl"] > 0:
                gewinner += 1


        winrate = gewinner / len(self.trades) * 100
        avg = summe / len(self.trades)

        return f"Trades: {len(self.trades)} | winrate: {winrate:.1f}% | Avg: {avg:.2f}€ "


j = Journal()
j.add_trade("NQ", 141)
j.add_trade("SP", -40.5)
j.add_trade("NQ", 300.0)

print(j.stats())
