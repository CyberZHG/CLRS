import random
import unittest


def euclid_1(a, b):
    if b == 0:
        return a
    return euclid_1(b, a % b)


def euclid_2(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            a = random.randint(0, 100000)
            b = random.randint(0, 100000)
            self.assertEqual(euclid_2(a, b), euclid_1(a, b))


if __name__ == '__main__':
    unittest.main()
