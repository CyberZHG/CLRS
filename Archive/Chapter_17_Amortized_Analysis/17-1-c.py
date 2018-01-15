import random
import unittest


class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0
        self.n = 1 << (self.k - 1)

    def increment(self):
        i = self.n
        for _ in xrange(self.k - 1, -1, -1):
            self.c ^= i
            if self.c & i > 0:
                break
            i >>= 1
        return self.c


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        counter = BitReversedCounter(4)
        self.assertEqual(counter.increment(), 8)
        self.assertEqual(counter.increment(), 4)
        self.assertEqual(counter.increment(), 12)
        self.assertEqual(counter.increment(), 2)
        self.assertEqual(counter.increment(), 10)


if __name__ == '__main__':
    unittest.main()
