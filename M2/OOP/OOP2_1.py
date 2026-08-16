class Trade:
    def __init__(self, symbol, pnl):
        self.symbol = symbol
        self.pnl =  pnl


    def ist_gewinn(self):
        return self.pnl > 0

    def beschreibung(self):
        return f"{self.symbol}: {self.pnl:.2f}"


t = Trade("NQ", 139.0)
f = Trade("SPX", -33.4)



print(t.beschreibung())
print(t.ist_gewinn())

print(f.beschreibung())
print(f.ist_gewinn())