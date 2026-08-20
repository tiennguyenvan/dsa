class DiscountRepository:
    def __init__(self, rules):
        self._rules = [dict(rule) for rule in rules]

    def for_product_and_segment(self, product_id, segment):
        for rule in self._rules:
            if (
                rule["product_id"] == product_id
                and rule["segment"] == segment
            ):
                return rule["percent"]

        return None

