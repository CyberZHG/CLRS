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
            return a[p]
        q = randomized_partition(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        if i < k:
            r = q
        else:
            p = q + 1
            i -= k


class SecondSmallestTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 1000000) for _ in range(random.randint(1, 1000))]
            i = random.randint(1, len(a))
            b = sorted(a)
            self.assertTrue(randomized_select(a, 0, len(a), i), b[i-1])


if __name__ == '__main__':
    unittest.main()
