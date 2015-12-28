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
    j = i
    for k in range(i + 1, r):
        if a[k] == x:
            j += 1
            a[j], a[k] = a[k], a[j]
        k -= 1
    return i, j


def randomized_partition(a, p, r):
    x = random.randint(p, r - 1)
    a[x], a[r - 1] = a[r - 1], a[x]
    return partition(a, p, r)


def quicksort(a, p, r):
    if p < r - 1:
        q, t = randomized_partition(a, p, r)
        quicksort(a, p, q)
        quicksort(a, t + 1, r)


class HoareTestCase(unittest.TestCase):

    def test_partition(self):
        for _ in range(10000):
            a = [random.randint(0, 10) for _ in range(random.randint(1, 1000))]
            p = random.randint(0, len(a) - 1)
            r = random.randint(0, len(a) - 1)
            if p >= r:
                continue
            q, t = partition(a, p, r)
            for i in range(p, q):
                self.assertTrue(a[i] < a[q])
            for i in range(t + 1, r):
                self.assertTrue(a[i] > a[t])
            for i in range(q, t):
                self.assertEqual(a[i], a[t])

    def test_sort(self):
        for _ in range(10000):
            a = [random.randint(0, 10) for _ in range(random.randint(1, 1000))]
            b = sorted(a)
            quicksort(a, 0, len(a))
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
