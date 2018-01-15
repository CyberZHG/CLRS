import random
import unittest


def black_box_median(a, p, r):
    return sorted(a[p:r])[(r - p - 1) // 2]


def partition(a, p, r, x):
    s = x
    i = p - 1
    for j in xrange(p, r - 1):
        if a[j] == x:
            a[j], a[r - 1] = a[r - 1], a[j]
            break
    for j in xrange(p, r - 1):
        if a[j] < x:
            i += 1
            s += a[j]
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i, s


def weighted_median(a, p, r, w=0.5):
    if p + 1 >= r:
        return a[p]
    x = black_box_median(a, p, r)
    q, s = partition(a, p, r, x)
    if s - a[q] < w and s >= w:
        return a[q]
    if s >= w:
        return weighted_median(a, p, q, w)
    return weighted_median(a, q + 1, r, w - s)


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(1000):
            a = random.sample(xrange(10000), 1000)
            s = sum(a)
            x = [float(v) / s for v in a]
            w = weighted_median(x, 0, len(x))
            s1, s2 = 0.0, 0.0
            for v in x:
                if v < w:
                    s1 += v
                elif v > w:
                    s2 += v
            self.assertTrue(s1 < 0.5 + 1e-8)
            self.assertTrue(s2 <= 0.5 + 1e-8)


if __name__ == '__main__':
    unittest.main()
