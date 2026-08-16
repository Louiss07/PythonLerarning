import json


class Journal:
    def __init__(self):
        self.trades = []

    def speichern(self, dateiname):
        with open(dateiname, "w") as datei:
            json.dump(self.trades, datei, indent=4)

    def laden(self, dateiname):
        try:
            with open (dateiname, "r") as datei:
                self.trades = json.load(datei)

        except FileNotFoundError:
            print("Datei nicht gefunden, journal bleibt leer")



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
                gewinner +=1


        winrate = gewinner / len(self.trades) * 100
        avg = summe / len(self.trades)

        return f"Trades: {len(self.trades)} | Win-Rate: {winrate:.1f}% | Avg: {avg:.2f}€"


    

j = Journal()
j.add_trade("NQ", 141.0)
j.add_trade("SP", -40.5)
j.add_trade("NQ", 300)
j.add_trade("SP", -102.0)
j.add_trade("NQ", 15.4)
j.add_trade("SP", -51.0)
j.add_trade("NQ", 234.4)
j.add_trade("SP", 0.0)
j.add_trade("NQ", 134.0)
j.add_trade("SP", -16.6)
j.speichern("Tradejournal.json")


j2 = Journal()
j2.laden("Tradejournal.json")

f = Journal()
f.laden("fafafa.json")
print(f.stats())

print(j2.stats())



