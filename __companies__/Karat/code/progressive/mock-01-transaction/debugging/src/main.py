from portfolio import Portfolio


positions = [
    {"symbol": "AAPL", "quantity": 2},
    {"symbol": "MSFT", "quantity": 3},
]

quotes = [
    {"symbol": "AAPL", "time": "10:15", "price": 110},
    {"symbol": "MSFT", "time": "9:30", "price": 50},
    {"symbol": "AAPL", "time": "9:45", "price": 100},
    {"symbol": "MSFT", "time": "10:00", "price": 60},
    {"symbol": "AAPL", "time": "10:30", "price": 120},
]

portfolio = Portfolio(positions, quotes)
print(portfolio.value_at("10:20"))
