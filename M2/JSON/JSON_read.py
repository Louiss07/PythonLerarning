import json

with open("trades.json", "r") as datei:
    trades = json.load(datei)


print(trades)
print(trades[0])
print(trades[0]["symbol"])
print(trades[0]["pnl"] + 10)
