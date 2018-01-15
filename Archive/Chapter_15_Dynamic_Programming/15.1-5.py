import random
import unittest


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(1, n):
        c = a + b
        a, b = b, c
    return c


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        self.assertEqual(fib(100), 354224848179261915075)


if __name__ == '__main__':
    unittest.main()
