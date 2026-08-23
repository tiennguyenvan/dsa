class ProductRepository:
    def __init__(self, products):
        self._products = [dict(product) for product in products]

    def find_by_id(self, product_id):
        for product in self._products:
            if product["id"] == product_id:
                return dict(product)

        return None

