import random
import unittest


def hoare_partition(a, p, r):
    x = a[p]
    i = p - 1
    j = r
    while True:
        while True:
            j -= 1
            if a[j] <= x:
                break
        while True:
            i += 1
            if a[i] >= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j


def quicksort(a, p, r):
    if p < r - 1:
        q = hoare_partition(a, p, r)
        quicksort(a, p, q + 1)
        quicksort(a, q + 1, r)


class HoareTestCase(unittest.TestCase):

    def test_sort(self):
        for _ in range(10000):
            a = [random.randint(0, 10000) for _ in range(random.randint(1, 100))]
            b = sorted(a)
            quicksort(a, 0, len(a))
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
