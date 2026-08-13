kontostand = 1000
tage = 0

while kontostand < 2000:
    kontostand = kontostand * 1.05
    tage += 1

print(f"Nach {tage} Tage bei {kontostand:.2f}€")


x = 10
while x > 0:
    x -= 1
    print(x)
    # x wird nie kleiner → läuft EWIG