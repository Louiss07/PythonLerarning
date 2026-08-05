trade = {
        "symbol": "AAPL",
        "entry": 100.5,
        "exit":100, 
        "stückzahl": 10
}

trade["exit"] = 101
trade["gebühr"] = 10

print(trade["symbol"])
print(trade["entry"])
print(trade["exit"])
print(trade["gebühr"])