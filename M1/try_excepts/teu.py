try:
    zahl = int(input("Welche Zahl möchtest du quadrieren?: "))
    quadrat = zahl * zahl
    print(f"Deine Zahl lautet {quadrat}")
except ValueError:
    print("Das ist leider keine zahl")
