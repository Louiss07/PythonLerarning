from datetime import date

d = date(2007, 9, 8)     # Jahr, Monat, 

print(d)
print(d.year)
print(d.month)
print(d.day)


print(d.weekday()) 





heute = date.today()
print(f"Heute ist der {heute}")





wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
d = date(2026, 8, 18)
print(wochentage[d.weekday()])    # Dienstag














