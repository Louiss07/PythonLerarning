name = "Aragorn"
level = 5
gold = 120.50
lebendig = True

print(f"{name}(Level {level}) hat {gold:.2f} Gold und ist am leben?: {lebendig}")

rucksack = ["Schwert", "Trank", "Schild", "Karte", "Fackel"]

rucksack.append("Kompass")
rucksack.remove("Trank")


print(f"Es sind {len(rucksack)} Items im Inventar")
print(f"Der erste gegenstand ist {rucksack[0]} und der letzte gegenstand ist {rucksack[-1]}")




waffe = {
    "name": "Flammenschwert",
    "schaden": 45,
    "wert":200.0,
    "magisch":True
}

print(f"Das {waffe['name']} macht {waffe['schaden']} Schaden und kostet {waffe['wert']:.2f} Gold und ist Magisch: {waffe['magisch']}")

geld = float(input("Wie viel gold besitzt du: "))

if geld >= waffe["wert"]:
    print("Gekauft")
elif geld >= waffe["wert"] / 2:
    fehlend = waffe["wert"] - geld
    print(f"Fast dir fehlen noch {fehlend:.2f} Gold")
else:
    print("Viel zu teuer für dich")


inventar = [

    {"name": "Schwert",  "wert": 50.0,  "gewicht": 3.0},
    {"name": "Trank",    "wert": 20.0,  "gewicht": 0.5},
    {"name": "Rüstung",  "wert": 150.0, "gewicht": 8.0},
    {"name": "Schild",   "wert": 80.0,  "gewicht": 5.0},
    {"name": "Fackel",   "wert": 5.0,   "gewicht": 1.0}

]

gesamtwert = 0
gesamtgewicht = 0

for items in inventar:
    print(f"{items['name']}: kostet {items['wert']} und wiegt {items['gewicht']}")
    gesamtwert += items["wert"]
    gesamtgewicht += items["gewicht"]

print(f"Alle items zusammen haben einen wert von {gesamtwert:.2f} Gold und wiegen zusammen {gesamtgewicht} kg")



leichte = 0
wertvolle = 0

for i in inventar: 
    if i["gewicht"] < 2:
        leichte += 1
    if i["wert"] > 50:
        wertvolle += 1

print(f"Es sind {leichte} leichte und {wertvolle} wertvolle items im inventar")

tuerster_wert = 0


for it in inventar: 
    if it["wert"] > tuerster_wert:
        tuerster_wert = it["wert"]
        teuerster_name = it["name"]
    

print(f"Das teuerste item ist {teuerster_name} und kostet {tuerster_wert:.2f} gold")

kontostand = 10
Abenteuer = 0

while kontostand <= 100:
    kontostand += 15
    Abenteuer += 1

print(f"Nach {Abenteuer} Abenteuer hat der held {kontostand} Gold erreicht")