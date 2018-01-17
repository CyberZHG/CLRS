import math
import random
import unittest


def sort_by_polar_angle(p0, p):
    a = []
    for i in xrange(len(p)):
        a.append(math.atan2(p[i][1] - p0[1], p[i][0] - p0[0]))
    a = map(lambda x: x % (math.pi * 2), a)
    p = sorted(zip(a, p))
    return map(lambda x: x[1], p)


class ProblemTestCase(unittest.TestCase):

    def random_point(self):
        return (random.randint(0, 100), random.randint(0, 100))

    def test_random(self):
        for _ in xrange(1000):
            n = random.randint(1, 10000)
            p0 = self.random_point()
            p = [self.random_point() for _ in xrange(n)]
            s = sort_by_polar_angle(p0, p)
            for i in xrange(len(p) - 1):
                a1 = math.atan2(s[i][1] - p0[1], s[i][0] - p0[0])
                a2 = math.atan2(s[i + 1][1] - p0[1], s[i + 1][0] - p0[0])
                a1 %= math.pi * 2
                a2 %= math.pi * 2
                self.assertTrue(a1 <= a2)


if __name__ == '__main__':
    unittest.main()
