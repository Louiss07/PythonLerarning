while True:
    try:
        Entry = float(input("Wo liegt deine Entry: "))
        Exit = float(input("Wo liegt dein Exit: "))
        Win = Entry - Exit
        print(Win)
        break
    
    except ValueError:
        print("Das ist kein Valider Trade, bitte erneut eingeben")









