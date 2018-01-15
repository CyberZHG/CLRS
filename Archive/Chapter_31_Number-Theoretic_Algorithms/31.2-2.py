import random
import unittest


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    (d, x, y) = extended_euclid(b, a % b)
    return (d, y, x - (a // b) * y)


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            (d, x, y) = extended_euclid(a, b)
            self.assertEqual(a * x + b * y, d)


if __name__ == '__main__':
    unittest.main()
