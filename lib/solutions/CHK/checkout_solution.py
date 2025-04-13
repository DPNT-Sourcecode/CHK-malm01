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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""

def simple_item_rule(code, price):
    def apply(counts, total):
        num = counts.pop(code, 0)
        return counts, total + num * price
    return apply

def buy_m_get_n_free_rule(code, m, n, price):
    def apply(counts, total):
        num = counts.pop(code, 0)
        num_free = (num // (m + n)) * n
        return counts, total + (num - num_free) * price
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

def buy_m_X_get_Y_free_rule(m, X, Y):
    def apply(counts, total):
        num_X = counts.get(X, 0)
        num_free_Y = num_X // m
        counts[Y] = max(counts.get(Y, 0) - num_free_Y, 0)
        return counts, total
    return apply


class CheckoutSolution:

    def __init__(self):
        self.rules = [
            buy_m_X_get_Y_free_rule(2, "E", "B"),
            buy_m_X_get_Y_free_rule(3, "N", "M"),
            buy_m_X_get_Y_free_rule(3, "R", "Q"),
            offer_item_rule("A", 5, 200),
            offer_item_rule("A", 3, 130),
            simple_item_rule("A", 50),
            offer_item_rule("B", 2, 45),
            simple_item_rule("B", 30),
            simple_item_rule("C", 20),
            simple_item_rule("D", 15),
            simple_item_rule("E", 40),
            buy_m_get_n_free_rule("F", 2, 1, 10),
            simple_item_rule("G", 20),
            offer_item_rule("H", 10, 80),
            offer_item_rule("H", 5, 45),
            simple_item_rule("H", 10),
            simple_item_rule("I", 35),
            simple_item_rule("J", 60),
            offer_item_rule("K", 2, 150),
            simple_item_rule("K", 80),
            simple_item_rule("L", 90),
            simple_item_rule("M", 15),
            simple_item_rule("N", 40),
            simple_item_rule("O", 10),
            offer_item_rule("P", 5, 200),
            simple_item_rule("P", 50),
            offer_item_rule("Q", 3, 80),
            simple_item_rule("Q", 30),
            simple_item_rule("R", 50),
            simple_item_rule("S", 30),
            simple_item_rule("T", 20),
            buy_m_get_n_free_rule("U", 3, 1, 40),
            offer_item_rule("V", 3, 130),
            offer_item_rule("V", 2, 90),
            simple_item_rule("V", 50),
            simple_item_rule("W", 20),
            simple_item_rule("X", 90),
            simple_item_rule("Y", 10),
            simple_item_rule("Z", 50),
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


