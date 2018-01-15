import random
import unittest


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    d, x, y = extended_euclid(b, a % b)
    return d, y, x - (a // b) * y


def modular_linear_equation_solver(a, b, n):
    d, x, y = extended_euclid(a, n)
    if b % d == 0:
        x0 = x * b / d % n
        return [(x0 + i * n / d) % n for i in xrange(d)]
    return []


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            a = random.randint(1, 10000)
            b = random.randint(1, 10000)
            n = random.randint(1, 10000)
            lst = modular_linear_equation_solver(a, b, n)
            for v in lst:
                self.assertEqual(a * v % n, b % n)


if __name__ == '__main__':
    unittest.main()
