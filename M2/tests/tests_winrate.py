def winrate(trades):
    if len(trades) == 0:
        return 0.0
    gewinner = len([t for t in trades if t["pnl"] > 0])
    return gewinner / len(trades) * 100


def test_normalfall():
    normal = [
        {"symbol": "NQ", "pnl": 100.0},
        {"symbol": "SP", "pnl": 50.0},
        {"symbol": "NQ", "pnl": -30.0},
        {"symbol": "SP", "pnl": -20.0}
    ]
    assert winrate(normal) == 50

def test_leere_liste():
    assert winrate([]) == 0.0


def test_nur_verluste():
    trade = [{"symbol": "NQ", "pnl": -100.0}]
    assert winrate(trade) == 0.0


print("Alle tests bestanden!")
