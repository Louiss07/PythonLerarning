Trade = {
    "Symbol" : "NQ",
    "Entry": 100.0,
    "Exit": 105.5,
    "Stückzahl": 5

}

Gewinn =  (Trade["Exit"] - Trade["Entry"]) * Trade["Stückzahl"]



print(f"{(Trade['Symbol'])}: {Gewinn:.2f}€ Gewinn")
