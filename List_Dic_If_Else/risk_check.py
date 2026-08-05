
Kontostand = float(input("Wie hoch ist dein Kontostand: "))
Risiko = float(input("Wie hoch ist dein Risiko: "))

if Risiko >=  0.02 * Kontostand:
    print("Risiko zu hoch")
else:
    print("Risiko ok")