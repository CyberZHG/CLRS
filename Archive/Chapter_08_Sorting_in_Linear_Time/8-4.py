import random
import unittest


def partition(a, b, p, r):
    pos = random.randint(p, r - 1)
    i = p - 1
    for j in range(p, r):
        if b[j] <= a[pos]:
            i += 1
            b[i], b[j] = b[j], b[i]
            if b[i] == a[pos]:
                k = i
    b[i], b[k] = b[k], b[i]
    pos = i
    i = p - 1
    for j in range(p, r):
        if a[j] <= b[pos]:
            i += 1
            a[i], a[j] = a[j], a[i]
            if a[i] == b[pos]:
                k = i
    a[i], a[k] = a[k], a[i]
    return pos


def quick_sort(a, b, p, r):
    if p + 1 < r:
        q = partition(a, b, p, r)
        quick_sort(a, b, p, q)
        quick_sort(a, b, q + 1, r)


class SortTestCase(unittest.TestCase):

    def random_shuffle(self, a):
        for i in range(len(a)):
            j = random.randint(0, i)
            a[i], a[j] = a[j], a[i]

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 1000) for _ in range(random.randint(1, 1000))]
            b = a[:]
            self.random_shuffle(b)
            quick_sort(a, b, 0, len(a))
            self.assertEqual(a, b)

    def test_duplicate(self):
        for _ in range(1000):
            a = [random.randint(1, 20) for _ in range(random.randint(1, 1000))]
            b = a[:]
            self.random_shuffle(b)
            quick_sort(a, b, 0, len(a))
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
