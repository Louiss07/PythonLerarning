Kontostand = float(input(f"Was Beträgt dein Kontostand?: "))
Risiko = float(input(f"Wie hoch ist dein Risiko in %: "))
StopDistanz = float(input(f"Stop Distanz?: "))

Positionsgroesse = Kontostand * (Risiko / 100 ) / StopDistanz

print(f"Du darfst {int(Positionsgroesse)} Aktien kaufen")