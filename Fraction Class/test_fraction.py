import unittest
import fraction


class TestFraction(unittest.TestCase):

    def setUp(self) -> None:
        self.a_frac = fraction.Fraction(1, 2)
        self.b_frac = fraction.Fraction(3, 4)
        self.c_frac = fraction.Fraction(-1, 2)
        self.e_frac = fraction.Fraction(-1, -2)

    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(fraction.Fraction.__add__(self.a_frac, self.b_frac), fraction.Fraction(5, 4))
        self.assertEqual(fraction.Fraction.__add__(self.a_frac, self.c_frac), fraction.Fraction(0, 1))
        self.assertEqual(fraction.Fraction.__add__(self.a_frac, self.e_frac), fraction.Fraction(1, 1))

    def test_sub(self):
        self.assertEqual(fraction.Fraction.__sub__(self.a_frac, self.b_frac), fraction.Fraction(-2, 8))
        self.assertEqual(fraction.Fraction.__sub__(self.a_frac, self.c_frac), fraction.Fraction(1, 1))
        self.assertEqual(fraction.Fraction.__sub__(self.a_frac, self.e_frac), fraction.Fraction(0, 1))

    def test_mul(self):
        self.assertEqual(fraction.Fraction.__mul__(self.a_frac, self.b_frac), fraction.Fraction(3, 8))
        self.assertEqual(fraction.Fraction.__mul__(self.a_frac, self.c_frac), fraction.Fraction(-1, 4))
        self.assertEqual(fraction.Fraction.__mul__(self.a_frac, self.e_frac), fraction.Fraction(1, 4))

    def test_div(self):
        self.assertEqual(fraction.Fraction.__truediv__(self.a_frac, self.b_frac), fraction.Fraction(2, 3))
        self.assertEqual(fraction.Fraction.__truediv__(self.a_frac, self.c_frac), fraction.Fraction(-1, 1))
        self.assertEqual(fraction.Fraction.__truediv__(self.a_frac, self.e_frac), fraction.Fraction(1, 1))

    def test_eq(self):
        self.assertFalse(fraction.Fraction.__eq__(self.a_frac, self.c_frac))

    def test_lt(self):
        self.assertFalse(fraction.Fraction.__lt__(self.a_frac, self.c_frac))

    def test_gt(self):
        self.assertTrue(fraction.Fraction.__gt__(self.a_frac, self.c_frac))

    def test_ne(self):
        self.assertTrue(fraction.Fraction.__ne__(self.a_frac, self.c_frac))


if __name__ == '__main__':
    unittest.main()
