import random
import unittest


def cut_rod(p, n, c):
    r = [0 for _ in xrange(n + 1)]
    for j in range(1, n + 1):
        r[j] = p[j]
        for i in range(1, j):
            r[j] = max(r[j], p[i] + r[j - i] - c)
    return r[n]


class ProblemTestCase(unittest.TestCase):

    def brute_force(self, p, n, c):
        r = p[n]
        for i in range(1, n):
            r = max(r, p[i] + self.brute_force(p, n - i, c) - c)
        return r

    def test_random(self):
        for _ in xrange(1000):
            p = [random.randint(0, 100) for _ in xrange(random.randint(1, 20))]
            p[0] = 0
            n = random.randint(1, 20)
            c = random.randint(1, 100)
            while len(p) <= n:
                p.append(0)
            self.assertEqual(cut_rod(p, n, c), self.brute_force(p, n, c))


if __name__ == '__main__':
    unittest.main()
