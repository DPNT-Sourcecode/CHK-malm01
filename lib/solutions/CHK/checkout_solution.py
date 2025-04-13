from collections import Counter

"""
Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""

class CheckoutSolution:

    def __init__(self):
        self.price_table = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }
        self.offers = {
            "A": (3, 130),
            "B": (2, 45)
        }

    # skus = unicode string
    def checkout(self, skus):
        total = 0
        items = Counter(skus)
        for sku, num in items.items():
            if sku not in self.price_table:
                return -1
            if sku in self.offers:
                offer = self.offers[sku]
                num_not_using_offer = num % offer[0]
                total += self.price_table[sku] * num_not_using_offer + offer[1] * (num // offer[0])
            else:
                total += self.price_table[sku] * num
        return total

