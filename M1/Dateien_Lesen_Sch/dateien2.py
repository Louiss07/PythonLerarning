#with open("Tagebuch.txt", "r") as datei:
    #inhalt = datei.read()
    #print(inhalt)


with open("Tagebuch.txt", "r") as datei:
    Zaehler = 0
    for zeile in datei:
        Zaehler += 1
        print(f"{Zaehler}: {zeile.strip()}") 
