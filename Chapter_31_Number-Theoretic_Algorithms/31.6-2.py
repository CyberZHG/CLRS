import random
import unittest


def modular_exponentiation(a, b, n):
    i, d = 0, 1
    while (1 << i) <= b:
        if (b & (1 << i)) > 0:
            d = (d * a) % n
        a = (a * a) % n
        i += 1
    return d


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            a = random.randint(1, 10000)
            b = random.randint(1, 10000)
            n = random.randint(1, 10000)
            self.assertEqual(modular_exponentiation(a, b, n), a ** b % n)


if __name__ == '__main__':
    unittest.main()
