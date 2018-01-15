import random
import unittest


def partition(a, p, r):
    x = a[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if a[j] >= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i


def quicksort(a, p, r):
    if p < r - 1:
        q = partition(a, p, r)
        quicksort(a, p, q)
        quicksort(a, q + 1, r)


class PartitionTestCase(unittest.TestCase):

    def test_partition(self):
        for _ in range(10000):
            a = [random.randint(0, 10000) for _ in range(random.randint(1, 100))]
            p = random.randint(0, len(a) - 1)
            r = random.randint(0, len(a) - 1)
            if p > r:
                p, r = r, p
            if p < r - 1:
                q = partition(a, p, r)
                for i in range(p, q):
                    self.assertTrue(a[i] >= a[q])
                for i in range(q + 1, r):
                    self.assertTrue(a[i] <= a[q])

    def test_sort(self):
        for _ in range(10000):
            a = [random.randint(0, 10000) for _ in range(random.randint(1, 100))]
            b = sorted(a)[::-1]
            quicksort(a, 0, len(a))
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
