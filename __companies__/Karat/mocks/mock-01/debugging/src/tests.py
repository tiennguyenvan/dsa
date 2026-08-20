import unittest

from portfolio import Portfolio


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.positions = [
            {"symbol": "AAPL", "quantity": 2},
            {"symbol": "MSFT", "quantity": 3},
        ]

        self.quotes = [
            {"symbol": "AAPL", "time": "10:15", "price": 110},
            {"symbol": "MSFT", "time": "9:30", "price": 50},
            {"symbol": "AAPL", "time": "9:45", "price": 100},
            {"symbol": "MSFT", "time": "10:00", "price": 60},
            {"symbol": "AAPL", "time": "10:30", "price": 120},
        ]

    def test_value_uses_latest_prices_before_cutoff(self):
        portfolio = Portfolio(self.positions, self.quotes)

        self.assertEqual(portfolio.value_at("10:20"), 400)

    def test_value_at_earlier_time(self):
        portfolio = Portfolio(self.positions, self.quotes)

        self.assertEqual(portfolio.value_at("9:50"), 350)

    def test_quote_order_does_not_matter(self):
        portfolio = Portfolio(self.positions, reversed(self.quotes))

        self.assertEqual(portfolio.value_at("10:20"), 400)

    def test_no_prices_before_cutoff(self):
        portfolio = Portfolio(self.positions, self.quotes)

        self.assertEqual(portfolio.value_at("8:00"), 0)


if __name__ == "__main__":
    unittest.main()
