import random
import unittest


def black_box_kth(a, k):
    return sorted(a)[k-1]


def black_box_median(a):
    return sorted(a)[(len(a) - 1) // 2]


def k_closest(a, k):
    median = black_box_median(a)
    b = [abs(a[i] - median) for i in xrange(len(a))]
    kth = black_box_kth(b, k)
    closest = []
    for i in xrange(len(a)):
        if abs(a[i] - median) < kth:
            closest.append(a[i])
    for i in xrange(len(a)):
        if abs(a[i] - median) == kth:
            closest.append(a[i])
        if len(closest) >= k:
            break
    return closest


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            a = random.sample(range(100000), 1000)
            k = random.randint(0, len(a))
            m = black_box_median(a)
            b = sorted(a, lambda x, y: abs(x - m) - abs(y - m))[:k]
            c = sorted(k_closest(a, k), lambda x, y: abs(x - m) - abs(y - m))
            for i in xrange(k):
                self.assertEqual(c[i] - m, b[i] - m)


if __name__ == '__main__':
    unittest.main()
