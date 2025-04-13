from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum():
    def test_simple(self):
        chk = CheckoutSolution()
        assert chk.checkout("") == 0
        assert chk.checkout("AB") == 80
        assert chk.checkout("ABC") == 100

    def test_invalid(self):
        chk = CheckoutSolution()
        assert chk.checkout("ABC ") == -1
        assert chk.checkout(" ABCE") == -1
        assert chk.checkout("?") == -1

    def test_simple_offers(self):
        chk = CheckoutSolution()
        assert chk.checkout("AAAB") == 160
        assert chk.checkout("AAAA") == 180
        assert chk.checkout("AAABB") == 175
        assert chk.checkout("AAABBAA") == 245
        assert chk.checkout("AAAAAAAA") == 330
        assert chk.checkout("PPPPPQQQ") == 280
        assert chk.checkout("PPPPPQQQPQ") == 360

    def test_special_offer(self):
        chk = CheckoutSolution()
        assert chk.checkout("EE") == 80
        assert chk.checkout("EBE") == 80
        assert chk.checkout("EBEB") == 110
        assert chk.checkout("EBEBB") == 125
        assert chk.checkout("NNNM") == 120
        assert chk.checkout("NNNMM") == 135
    
    def test_buy_m_get_n_free(self):
        chk = CheckoutSolution()
        assert chk.checkout("F") == 10
        assert chk.checkout("FF") == 20
        assert chk.checkout("FFF") == 20
        assert chk.checkout("FFFF") == 30
        assert chk.checkout("FFFFF") == 40
        assert chk.checkout("FFFFFF") == 40
        assert chk.checkout("FFFFFFF") == 50
        assert chk.checkout("UU") == 80
        assert chk.checkout("UUU") == 120
        assert chk.checkout("UUUU") == 120
        assert chk.checkout("UUUUU") == 160
        assert chk.checkout("UUUUUU") == 200
        assert chk.checkout("UUUUUUU") == 240
        assert chk.checkout("UUUUUUUU") == 240
    
    def test_group_discount(self):
        chk = CheckoutSolution()
        assert chk.checkout("STXYZ") == 45 + 20 + 17
        assert chk.checkout("STXY") == 45 + 17
        assert chk.checkout("SSSSS") == 45 + 20 + 20
        assert chk.checkout("SSZZZ") == 40 + 45 # apply to most expensive item
        assert chk.checkout("XXX") == 45
        assert chk.checkout("XXXZ") == 17 + 45


"""
Our price table and offers:
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
"""