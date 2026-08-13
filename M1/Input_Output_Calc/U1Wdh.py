#name = "Louis"
#alter = 18
#kontostand = 10000.5
#beschäftigt = False

#print(type(name)) ; print(name)
#print(type(alter)) ; print(alter)
#print(type(kontostand)) ; print(kontostand)
#print(type(beschäftigt)) ; print(beschäftigt)



#Rechnung1 = 10 / 3 #10 geteilt durch 3 
#Rechnung2 = 10 //3 #10 geteilt durch 3 gerundet = Ganzzahldivision von 10/3
##Rechnung3 = 10 % 3 #Rest von 10 / 3
#print(Rechnung1, Rechnung2, Rechnung3)

#warum print("Kontostand: " + 1200) crashed ? - weil print nicht alleine einen string und int zusammen ausgeben kann, durch einen
#f-string lässt sich mithilfe von {} eine Variablen string und intager also eine ganzzahl verbinden

#2.1    --------------------------------------------------

#geburtsjahr = int(input("Wann bist du geboren: "))
#aktuelles_jahr = 2026

#alter =  aktuelles_jahr - geburtsjahr
#print(alter)

#2.2    ---------------------------------------

#Zahl1 = int(input("Wie lautet die erste Zahl?: "))

#Zahl2 = int(input("Wie lautet die zweite Zahl?: "))

#grossere = (Zahl1 + Zahl2 + abs(Zahl1 - Zahl2)) / 2

#print(f"die grossere Zahl ist {grossere:g}")

# 2.3 -------------------------------


#Zahl = int(input("Zahl: "))
#print(Zahl)

#Phython will einen int also ganzzahl ausgeben bekommt aber einen string => schafft es nicht umzuwerten


#3.1-------------------------------------
Kontostand = int(input("Was ist dein Kontostand"))
Risiko = float(input("Wie hoch ist dein Risiko (in %)"))
Stop_Distanz = float(input("Wo liegt deine Stopdistanz")) 

Risikobetrag = Kontostand * (Risiko / 100)
Positionsgroesse = Risikobetrag / Stop_Distanz 

print(f"Dein Risiko liegt bei {Risikobetrag:g}")
print(f"{Positionsgroesse:.2f} ist deine Positionsgroesse")

#3.2----------------------

Entry1 = float(input("Einstieg: "))          #Fragt Entry ab
Exit1 = float(input("Exit: "))               #Fragt Exit ab 
Stückzahl = float(input("Stückzahl: "))     #Fragt Stückzahl ab

Gewinn = (Exit1 - Entry1) * Stückzahl         # Gewinn ist Kaufpreis  - einstiegspreis das ist für eine und dann das * die anzahl an gekauften
Rendite = (Exit1 - Entry1) / Entry1 * 100      # Die Rendite ist Exit - Enty und dann geteilt durch Entry * 100

print(f"Dein Gewinn beträgt {Gewinn:.2f} € ")
print(f"Die Rendite dabei ist {Rendite:.2f} % ")

#3.3 --------------------------

TakeProfit = float(input("Wo liegt dein TP"))
StopLoss = float(input("Wo liegt dein SL"))
Entry = float(input("Einstieg: "))          


                    
rrr = (TakeProfit - Entry) / (Entry - StopLoss)

print(f"Dein RRR beträgt 1 : {rrr:.2f}  ")














