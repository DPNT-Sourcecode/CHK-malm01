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

    def test_special_offer(self):
        chk = CheckoutSolution()
        assert chk.checkout("EE") == 80
        assert chk.checkout("EBE") == 80
        assert chk.checkout("EBEB") == 110
        assert chk.checkout("EBEBB") == 125
    
    def test_buy_m_get_n_free(self):
        chk = CheckoutSolution()
        assert chk.checkout("F") == 10
        assert chk.checkout("FF") == 20
        assert chk.checkout("FFF") == 20
        assert chk.checkout("FFFF") == 30
        assert chk.checkout("FFFFF") == 40
        assert chk.checkout("FFFFFF") == 40
        assert chk.checkout("FFFFFFF") == 50
