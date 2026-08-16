class Trade:
    def __init__(self, symbol, pnl):
        self.symbol = symbol
        self.pnl = pnl

    def ist_gewinn(self):
        return self.pnl > 0

    def beschreibung(self):
        return f"{self.symbol}: {self.pnl:.2f}"


t = Trade("NQ", 141.0)
f = Trade("SP", -100)

print(t.ist_gewinn())      # True
print(t.beschreibung())    # NQ: 141.00€

print(f.ist_gewinn())      
print(f.beschreibung()) 