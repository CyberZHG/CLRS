import random
import unittest


def weighted_median(x):
    x.sort()
    s = 0.0
    for i in xrange(len(x)):
        s += x[i]
        if s >= 0.5:
            return x[i]


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(1000):
            a = random.sample(xrange(10000), 1000)
            s = sum(a)
            x = [float(v) / s for v in a]
            w = weighted_median(x)
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
