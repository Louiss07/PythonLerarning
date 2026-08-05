gewinn = 50
rendite = 3.5
stückzahl = 101

if gewinn > 0:
    print("trade im plus")
else:
    print("trade im Minus")


if rendite > 5:
    print("Top Trade")
elif rendite > 0:
    print("Solide")
elif rendite == 0:
    print("Brake Even")
else:
    print("Verlust")


if rendite > 0 and stückzahl > 100:
    print("Großer Gewinn-Trade")

if rendite < -5 or stückzahl == 0:
    print("Achtung: Problem")