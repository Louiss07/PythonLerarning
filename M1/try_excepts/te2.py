try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Keine Zahl!")
else:
    print(f"Alles gut, Zahl war {zahl}")   # läuft NUR wenn kein Fehler kam
finally:
    print("Fertig.")                        # läuft IMMER, egal was passiert