zahlen =  [1, 2, 3, 4, 5, 6]
quadrate = [z * z for z in zahlen]
gerade = [i * i for i in zahlen if i % 2 == 0]

print(zahlen)
print(quadrate)
print(gerade)