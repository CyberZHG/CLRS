import random
import unittest


def black_box_median(a, p, r):
    return sorted(a)[(p + r) // 2]


def partition(a, p, r, x):
    i = p - 1
    for k in range(p, r - 1):
        if a[k] == x:
            a[k], a[r - 1] = a[r - 1], a[k]
            break
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i


def select(a, p, r, i):
    if p + 1 == r:
        return a[p]
    x = black_box_median(a, p, r)
    q = partition(a, p, r, x)
    k = q - p + 1
    if i == k:
        return a[q]
    if i < k:
        return select(a, p, q, i)
    return select(a, q + 1, r, i - k)


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 1000000) for _ in range(random.randint(1, 1000))]
            i = random.randint(1, len(a))
            b = sorted(a)
            self.assertTrue(select(a, 0, len(a), i), b[i-1])


if __name__ == '__main__':
    unittest.main()
