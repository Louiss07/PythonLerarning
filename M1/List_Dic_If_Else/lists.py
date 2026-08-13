preise = [10, 15, 20.5, 25]
namen =  ["AAPL", "TSLA", "NVDA", "NQ"]

preise[0] = 11
preise.append(30)
preise.remove(20.5)



print(preise[2])

print(len(preise))    # Anzahl Elemente
print(max(preise))    # größter Wert
print(min(preise))    # kleinster Wert
print(sum(preise))    # Summe aller Werte

print(sum(preise) / len(preise))