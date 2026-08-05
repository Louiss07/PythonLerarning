Rendite = float(input("Wie hoch ist deine Rendite: "))

if Rendite > 5:
    print(f"Starker Trade, deine Rendite liegt bei {Rendite} %")

elif Rendite > 0:
    print(f"Solider Trade, deine Rendite liegt bei {Rendite} %")

elif Rendite == 0:
    print("Brake Even")

else:
    print("Verlust")

