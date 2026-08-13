Entry = float(input("Wo leigt deine Entry? "))
Exit = float(input("Wo leigt deine Exit? "))
Stückzahl = float(input("Wie viel hast du gekauft? "))

GewinnAbsolut = (Exit - Entry) * Stückzahl
Rendite = (Exit - Entry) / Entry * 100

print(f"Dein Absoluter gewinn berträgt {round(GewinnAbsolut, 2)} wobei deine Rendite bei {round(Rendite, 2)} in % liegt")
