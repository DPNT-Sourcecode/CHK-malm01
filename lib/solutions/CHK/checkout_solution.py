from collections import Counter

"""
Our price table and offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""

def simple_item_rule(code, price):
    def apply(counts, total):
        num = counts.pop(code, 0)
        return counts, total + num * price
    return apply

def offer_item_rule(code, offer_count, offer_price):
    def apply(counts, total):
        num = counts.get(code, 0)
        if num % offer_count == 0:
            del counts[code]
        else:
            counts[code] %= offer_count
        return counts, total + offer_price * (num // offer_count)
    return apply

class CheckoutSolution:

    def __init__(self):
        def special_rule_2e_free_b(counts, total):
            num_e = counts.get("E", 0)
            num_free_b = num_e // 2
            counts["B"] = max(counts.get("B", 0) - num_free_b, 0)
            return counts, total
        
        self.rules = [
            special_rule_2e_free_b,
            offer_item_rule("A", 5, 200),
            offer_item_rule("A", 3, 130),
            offer_item_rule("B", 2, 45),
            simple_item_rule("A", 50),
            simple_item_rule("B", 30),
            simple_item_rule("C", 20),
            simple_item_rule("D", 15),
            simple_item_rule("E", 40),
        ]

    # skus = unicode string
    def checkout(self, skus):
        total = 0
        counts = Counter(skus)
        for rule in self.rules:
            counts, total = rule(counts, total)
            if total == -1:
                return -1
        if len(counts) > 0:
            return -1
        return total

