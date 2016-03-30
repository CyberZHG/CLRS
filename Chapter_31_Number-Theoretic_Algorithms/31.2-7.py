import random
import unittest


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    d, x, y = extended_euclid(b, a % b)
    return (d, y, x - (a // b) * y)


def extended_eculid_multi(a):
    if len(a) == 1:
        return (a[0], [1])
    g = a[-1]
    xs = [1] * len(a)
    ys = [0] * len(a)
    for i in xrange(len(a) - 2, -1, -1):
        g, xs[i], ys[i + 1] = extended_euclid(a[i], g)
    m = 1
    for i in xrange(1, len(a)):
        m *= ys[i]
        xs[i] *= m
    return (g, xs)


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            n = random.randint(1, 1000)
            k = random.randint(1, 10)
            lst = [k * random.randint(0, 10000) for _ in xrange(n)]
            d, xs = extended_eculid_multi(lst)
            s = sum(map(lambda (x, y): x * y, zip(lst, xs)))
            self.assertEqual(s, d)


if __name__ == '__main__':
    unittest.main()
