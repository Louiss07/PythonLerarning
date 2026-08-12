try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(f"Das Doppelte ist {zahl * 2}")
except ValueError:
    print("Das war keine gültige Zahl!")