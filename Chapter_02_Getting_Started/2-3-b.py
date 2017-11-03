import unittest


def polynomial_evaluation(a, x):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * x ** i
    return sum


class PolynomialEvaluationTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(polynomial_evaluation([], 4), 0)

    def test_const(self):
        self.assertEqual(polynomial_evaluation([5], 2), 5)

    def test_simple(self):
        self.assertEqual(polynomial_evaluation([1, 2, 3], 4), 57)


if __name__ == '__main__':
    unittest.main()
