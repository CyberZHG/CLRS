import random
import unittest


def rev_k(k, a):
    x = 0
    for _ in xrange(k):
        x <<= 1
        x += a & 1
        a >>= 1
    return x


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        self.assertEqual(rev_k(4, 3), 12)


if __name__ == '__main__':
    unittest.main()
