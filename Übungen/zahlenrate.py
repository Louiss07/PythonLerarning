import random

print("Das ist ein zahlenrate spiel, du musst die zahl des computers erraten!")

czahl = random.randint(1, 100)
versuchszähler = 0


while True:
    try:
        gzahl = int(input("Wie lautet deine Zahl: "))
        versuchszähler +=1
        if gzahl == czahl:
            print(f"Stark du hast die Zahl erraten, sie wae {czahl}, du hast {versuchszähler} Versuche gebraucht")#
            break
        elif gzahl > czahl:
            print("Die Zahl ist kleienr, rate nochmal.")
        elif gzahl < czahl:
            print("Die Zahl ist größer, rate nochmal")


            


    except ValueError:
        print("Das ist keine Zahl, probiere es erneut!")