trades = [

    {"symbol": "NQ", "pnl": 141.0},
    {"symbol": "SP", "pnl": -40.5},
    {"symbol": "NQ", "pnl": 300.0}

]

gesamt = 0
for trade in trades:
    gesamt = gesamt + trade["pnl"]

print(f"Geamt PnL: {gesamt:.2f}€")

for trade in trades:
    print(f"{trade['symbol']}: {trade['pnl']}€")


gewinner = 0
for trade in trades: 
    if trade["pnl"] > 0:
        gewinner += 1

print(f"{gewinner} Gewinnende-Trades")