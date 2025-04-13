from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum():
    def test_simple(self):
        chk = CheckoutSolution()
        assert chk.checkout("") == 0
        assert chk.checkout("AB") == 80
        assert chk.checkout("ABC") == 100

    def test_invalid(self):
        chk = CheckoutSolution()
        assert chk.checkout("ABCE") == -1
        assert chk.checkout("FABCE") == -1

    def test_simple_offers(self):
        chk = CheckoutSolution()
        assert chk.checkout("AAAB") == 160
        assert chk.checkout("AAAA") == 180
        assert chk.checkout("AAABB") == 175
        assert chk.checkout("AAABBAA") == 245
        assert chk.checkout("AAAAAAAA") == 330
