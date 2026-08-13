with open("Notiz.txt", "w") as datei:
    datei.write("Mein erster Trade\n")
    datei.write("NQ: +141 Gold\n")

with open("Notiz.txt", "a") as datei:
    datei.write("Sp: -40 Gold\n")
