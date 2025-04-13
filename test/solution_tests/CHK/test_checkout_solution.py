from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum():
    def test_simple(self):
        chk = CheckoutSolution()
        assert chk.checkout("") == 0
        assert chk.checkout("AB") == 80

    def test_invalid(self):
        chk = CheckoutSolution()
        assert chk.checkout("ABCE") == -1
        assert chk.checkout("FABCE") == -1

    def test_offer(self):
        chk = CheckoutSolution()
        assert chk.checkout("AAAB") == 160
        assert chk.checkout("AAAA") == 180
        assert chk.checkout("AAABB") == 175
