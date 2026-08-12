with open("Tagebuch.txt", "w") as datei:
    datei.write("Essen\n")
    datei.write("Shoppen\n")
    datei.write("Trinken\n")

with open("Tagebuch.txt", "a") as datei:
    datei.write("Hallo\n")
