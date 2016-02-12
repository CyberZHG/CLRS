import random
import unittest


class BitReversedCounter:
    def __init__(self, k):
        self.k = k
        self.c = 0

    def increment(self):
        for i in xrange(self.k - 1, -1, -1):
            self.c ^= 1 << i
            if self.c & (1 << i) > 0:
                break
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
