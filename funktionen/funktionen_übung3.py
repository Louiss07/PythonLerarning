def zaehle_vokale(wort):
    wort.lower()
    zaehler = 0
    for buchstabe in wort:
        if buchstabe in "aeiou":
            zaehler +=1
    return(zaehler)

print(zaehle_vokale("Hallo"))
print(zaehle_vokale("Rindfleisch"))


def ist_volljaehrig(alter):
    if alter >= 18:
        return f"ist volljährig, dar rein"
    else:
        return f"darf nicht rein, ist {alter} Jahre alt!"

print(ist_volljaehrig(17))



def groesste(zahlenliste):
    groesste1 = 0
    for zahlen in zahlenliste:
        if zahlen > groesste1:
            groesste1 = zahlen
    return(groesste1)


ergebnis = groesste([3, 17, 9, 42, 8])
print(f"{ergebnis} ist die größte zahl")


