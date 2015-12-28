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
    while p < r - 1:
        q, t = randomized_partition(a, p, r)
        if q - p < r - t:
            quicksort(a, p, q)
            p = t + 1
        else:
            quicksort(a, t + 1, r)
            r = q


class QuicksortStackTestCase(unittest.TestCase):

    def test_sort(self):
        for _ in range(10000):
            a = [random.randint(0, 10) for _ in range(random.randint(1, 1000))]
            b = sorted(a)
            quicksort(a, 0, len(a))
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
