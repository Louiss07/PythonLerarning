import random


letzter_Wurf = ""
aktuelle_Serie = 0
laengste_Serie = 0



for i in range(100):
    wurf = random.choice(["Kopf", "Zahl"])
    if wurf == letzter_Wurf:
        aktuelle_Serie += 1
    else:
        aktuelle_Serie = 1

    if aktuelle_Serie > laengste_Serie:
        laengste_Serie = aktuelle_Serie

    letzter_Wurf = wurf



print(f"Die Längste Serie lag bei {laengste_Serie} Würfen")