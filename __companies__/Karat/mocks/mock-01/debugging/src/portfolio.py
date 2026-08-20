from quote_repository import QuoteRepository


class Portfolio:
    def __init__(self, positions, quotes):
        self._positions = list(positions)
        self._quotes = QuoteRepository(quotes)

    def value_at(self, as_of):
        prices = self._quotes.latest_prices(as_of)
        total = 0
        # print(as_of, prices)

        for position in self._positions:
            price = prices.get(position["symbol"])

            if price is not None:
                total += position["quantity"] * price

        return total
