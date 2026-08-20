
#assert 2 + 2 == 4        # wahr → läuft durch, still
#assert 2 + 2 == 5        # falsch → AssertionError, Crash
test_trades = [
    {"symbol": "NQ", "pnl": 100.0},   # Gewinner
    {"symbol": "SP", "pnl": -50.0}    # Verlierer
]
normal = [
    {"symbol": "NQ", "pnl": 100.0},
    {"symbol": "SP", "pnl": 50.0},
    {"symbol": "NQ", "pnl": -30.0},
    {"symbol": "SP", "pnl": -20.0}
]


nur_verluste = [
    {"symbol": "NQ", "pnl": -100.0},
    {"symbol": "SP", "pnl": -50.0}
]


def winrate(trades):
    if len(trades) == 0:
        return 0.0
    gewinner = len([t for t in trades if t["pnl"] > 0])
    return gewinner / len(trades) * 100




assert winrate(test_trades) == 50.0
assert winrate(normal) == 50.0
assert winrate([]) == 0.0
assert winrate(nur_verluste) == 0.0
print("Alle Tests bestanden!")









def test_normalfall():
    normal = [
        {"symbol": "NQ", "pnl": 100.0},
        {"symbol": "SP", "pnl": -50.0}
    ]
    assert winrate(normal) == 50.0

def test_leere_liste():
    assert winrate([]) == 0.0

def test_nur_verluste():
    trades = [{"symbol": "NQ", "pnl": -100.0}]
    assert winrate(trades) == 0.0
