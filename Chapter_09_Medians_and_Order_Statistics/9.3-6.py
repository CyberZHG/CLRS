import random
import unittest


def partition(a, p, r):
    x = a[r - 1]
    i = p - 1
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i


def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)


def randomized_select(a, p, r, i):
    while True:
        if p + 1 == r:
            return p, a[p]
        q = randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return q, a[q]
        if i < k:
            r = q
        else:
            p = q + 1
            i -= k


def k_quantiles_sub(a, p, r, pos, f, e, quantiles):
    if f + 1 > e:
        return
    mid = (f + e) // 2
    q, val = randomized_select(a, p, r, pos[mid])
    quantiles[mid] = val
    k_quantiles_sub(a, p, q, pos, f, mid, quantiles)
    k = q - p + 1
    for i in xrange(mid + 1, e):
        pos[i] -= k
    k_quantiles_sub(a, q + 1, r, pos, mid + 1, e, quantiles)


def k_quantiles(a, k):
    num = len(a) / k
    mod = len(a) % k
    pos = [num for _ in xrange(k)]
    for i in xrange(mod):
        pos[i] += 1
    for i in xrange(1, k):
        pos[i] += pos[i - 1]
    quantiles = [0 for _ in xrange(k)]
    k_quantiles_sub(a, 0, len(a), pos, 0, len(pos), quantiles)
    return quantiles


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 100000) for _ in range(random.randint(1, 1000))]
            k = random.randint(1, len(a))
            b = sorted(a)
            j = 0
            r = k_quantiles(a, k)
            for i in range(k):
                j += len(a) / k
                if i < len(a) % k:
                    j += 1
            self.assertTrue(r[i], b[j - 1])


if __name__ == '__main__':
    unittest.main()
