trades = [
    {"symbol": "NQ", "pnl": 141.0},
    {"symbol": "SP", "pnl": -40.5},
    {"symbol": "NQ", "pnl": 300.0},
    {"symbol": "SP", "pnl": -102.0},
    {"symbol": "NQ", "pnl": 15.4},
    {"symbol": "SP", "pnl": -51.0},
    {"symbol": "NQ", "pnl": 234.4},
    {"symbol": "SP", "pnl": 0.0},
    {"symbol": "NQ", "pnl": 134.0},
    {"symbol": "SP", "pnl": -16.6}
]

with open("TJ.txt", "w") as datei:
    for trade in trades:
        datei.write(f"{trade['symbol']},{trade['pnl']}\n")


def trades_laden(dateiname):
    trades = []
    try:
        with open (dateiname, "r") as datei: 
            for trade in datei:
                teile = trade.strip().split(",")
                symbol = teile[0]
                pnl = float(teile[1])
                trades.append({"symbol": symbol, "pnl": pnl})
        return trades     
    except FileNotFoundError:
        print("Diese Datei konnte nicht gefunden werden!")
        return []



trades = trades_laden("TJ2.txt")
print(f"{trades}\n")

