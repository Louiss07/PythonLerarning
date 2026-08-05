def verdoppelte(zahl):
    return zahl * 2
text=(verdoppelte(3))
print(text)
print(verdoppelte(4))


def mehrwertsteuer(preis):
    return preis * 1.19 
print(mehrwertsteuer(100))


def begruessung(name, uhrzeit):
    if uhrzeit <= 12:
        return f"Guten Morgen, {name}"
    else:
        return f"Guten Tag, {name}"

print(begruessung("Louis", 12))
print(begruessung("Louis", 6))
print(begruessung("Louis", 16))
