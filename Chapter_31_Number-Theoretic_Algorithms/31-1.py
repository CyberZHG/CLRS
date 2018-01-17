import random
import unittest


def binary_gcd(a, b):
    if a < b:
        return binary_gcd(b, a)
    if b == 0:
        return a
    if (a & 1 == 1) and (b & 1 == 1):
        return binary_gcd((a - b) >> 1, b)
    if (a & 1 == 0) and (b & 1 == 0):
        return binary_gcd(a >> 1, b >> 1) << 1
    if a & 1 == 1:
        return binary_gcd(a, b >> 1)
    return binary_gcd(a >> 1, b)


class ProblemTestCase(unittest.TestCase):

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def test_random(self):
        for _ in xrange(100000):
            a = random.randint(1, 1000000)
            b = random.randint(1, 1000000)
            self.assertEqual(binary_gcd(a, b), self.gcd(a, b))


if __name__ == '__main__':
    unittest.main()
