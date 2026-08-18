from datetime import datetime, date

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
d = date(2007, 9, 8)

print(d.year)
print(d.month)
print(d.day)


heute = date.today()
print(heute)
print(heute.weekday())
print(wochentage[heute.weekday()])
