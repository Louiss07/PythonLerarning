from datetime import datetime, date

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
text = "2026-08-19"
d = datetime.strptime(text, "%Y-%m-%d").date()
print(wochentage[d.weekday()])


b = date(2026, 8, 18)
text = b.strftime("%Y-%m-%d")
print(text)