def quadrat(zahl):
    return zahl * zahl

print(quadrat(3))
print(quadrat(4))
print(quadrat(5))


def begruessung(name, level):
    return f"{name} ist Level {level}!"

print(begruessung("Aragon", 5))
text = begruessung("Louis", 35)
print(text)





def ist_gerade(zahl):
    return zahl % 2 == 0
        

print(ist_gerade(4))




inventar = [
    {"name": "Schwert",  "wert": 50.0,  "gewicht": 3.0},
    {"name": "Trank",    "wert": 20.0,  "gewicht": 0.5},
    {"name": "Rüstung",  "wert": 150.0, "gewicht": 8.0},
    {"name": "Schild",   "wert": 80.0,  "gewicht": 5.0},
    {"name": "Fackel",   "wert": 5.0,   "gewicht": 1.0}
]


def durchschnittswert(inventar):
    summe = 0
    for items in inventar:
        summe += items["wert"] 
    return summe / len(inventar)


durschnitts_wert = durchschnittswert(inventar)
print(f"Der durchsnittswert des inventars ist {durschnitts_wert:.2f} Gold")





def teuerste_item(inventar):
    teuerster_wert = 0
    teuerster_name = ""
    for it in inventar:
        if it["wert"] > teuerster_wert:
            teuerster_wert = it["wert"]
            teuerster_name = it["name"]
    return teuerster_name



t_name = teuerste_item(inventar)
print(f"{t_name} ist das teuerste item in deinem inventar")
      


            
            


