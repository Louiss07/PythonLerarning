import json

with open ("TJ.json", "r") as datei:
    trades = json.load(datei)

#print(trades)
print(trades[0]["pnl"] * 3)

