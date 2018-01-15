import random
import unittest


def median_of_two(a, b):
    if len(a) == 1:
        return min(a[0], b[0])
    mid = (len(a) - 1) // 2
    k = mid + 1
    if a[mid] <= b[mid]:
        return median_of_two(a[-k:], b[:k])
    return median_of_two(a[:k], b[-k:])


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            n = random.randint(1, 1000)
            a = sorted([random.randint(1, 100000) for _ in xrange(n)])
            b = sorted([random.randint(1, 100000) for _ in xrange(n)])
            median = sorted(a + b)[(2 * n - 1) // 2]
            self.assertEqual(median_of_two(a, b), median)


if __name__ == '__main__':
    unittest.main()
