import random
import unittest


def cut_rod_sub(p, n, r, s):
    if r[n] >= 0:
        return r[n]
    r[n] = 0
    for i in range(1, n + 1):
        ret = p[i] + cut_rod_sub(p, n - i, r, s)
        if r[n] < ret:
            r[n] = ret
            s[n] = i
    return r[n]


def cut_rod(p, n):
    r = [-1 for _ in xrange(n + 1)]
    s = [i for i in xrange(n + 1)]
    cut_rod_sub(p, n, r, s)
    r = r[n]
    subs = []
    while n > 0:
        subs.append(s[n])
        n -= s[n]
    return r, subs


class ProblemTestCase(unittest.TestCase):

    def brute_force(self, p, n):
        r = [0 for _ in xrange(n + 1)]
        for j in range(1, n + 1):
            r[j] = p[j]
            for i in range(1, j):
                r[j] = max(r[j], p[i] + r[j - i])
        return r[n]

    def test_random(self):
        for _ in xrange(1000):
            p = [random.randint(0, 100) for _ in range(random.randint(1, 500))]
            p[0] = 0
            n = random.randint(1, 500)
            while len(p) <= n:
                p.append(0)
            r, subs = cut_rod(p, n)
            self.assertEqual(r, self.brute_force(p, n))
            self.assertEqual(sum(subs), n)
            total = 0
            for s in subs:
                total += p[s]
            self.assertEqual(total, r)


if __name__ == '__main__':
    unittest.main()
