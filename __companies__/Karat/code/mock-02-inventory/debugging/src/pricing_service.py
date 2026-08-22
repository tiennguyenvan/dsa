from discount_repository import DiscountRepository
from product_repository import ProductRepository


class PricingService:
    def __init__(self, products, discount_rules):
        self._products = ProductRepository(products)
        self._discounts = DiscountRepository(discount_rules)

    def final_price(self, product_id, segment):
        product = self._products.find_by_id(product_id)
        if product is None:
            return None

        segment_discount = self._discounts.for_product_and_segment(
            product_id,
            segment,
        )
        discount = (
            segment_discount
            if segment_discount is not None
            else product["default_discount_percent"]
        )

        return product["price"] * (100 - discount) // 100
