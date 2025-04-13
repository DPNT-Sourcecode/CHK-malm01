from solutions.CHK.checkout_solution import CheckoutSolution

class TestSum():
    def test_simple(self):
        chk = CheckoutSolution()
        assert chk.checkout("") == 0
        assert chk.checkout("AB") == 80
        assert chk.checkout("ABC") == 100

    def test_invalid(self):
        chk = CheckoutSolution()
        assert chk.checkout("ABCG") == -1
        assert chk.checkout("GABCE") == -1

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


