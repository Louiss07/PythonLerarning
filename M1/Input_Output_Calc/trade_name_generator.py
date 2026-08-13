import random


name= input("Wie Lautet dein Name: ")

print(f"Dein name hat {len(name)} Buchstaben")

Trader_Name = "TR" + "_" + name[0:4].upper() + "_" + str(random.randint(1, 100))

print(f"Dein Neuer Name Lautet: {Trader_Name}")


