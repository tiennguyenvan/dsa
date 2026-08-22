from time_utils import to_minutes


class QuoteRepository:
    def __init__(self, quotes):
        self._quotes = list(quotes)

    def latest_prices(self, as_of):
        cutoff = to_minutes(as_of)
        latest_by_symbol = {}
        # print('as_of', as_of)
        for quote in self._quotes:
            if to_minutes(quote["time"]) > cutoff:
                continue
            # print('quote["time"]', quote["time"])

            symbol = quote["symbol"]
            current = latest_by_symbol.get(symbol)

            if current is None or to_minutes(quote["time"]) > to_minutes(current["time"]):
                latest_by_symbol[symbol] = quote

        return {
            symbol: quote["price"]
            for symbol, quote in latest_by_symbol.items()
        }
