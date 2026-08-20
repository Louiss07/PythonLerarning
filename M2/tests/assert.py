#assert 2 + 2 == 4        # wahr → läuft durch, still
#assert 2 + 2 == 5        # falsch → AssertionError, Crash
test_trades = [
    {"symbol": "NQ", "pnl": 100.0},   # Gewinner
    {"symbol": "SP", "pnl": -50.0}    # Verlierer
]


def winrate(trades):
    if len(trades) == 0:
        return 0.0
    gewinner = len([t for t in trades if t["pnl"] > 0])
    return gewinner / len(trades) * 100




assert winrate(test_trades) == 50.0