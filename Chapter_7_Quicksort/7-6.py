import random
import unittest


class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __lt__(self, other):
        return self.r < other.l

    def __str__(self):
        return '(' + str(self.l) + ', ' + str(self.r) + ')'

    def get_intersect(self, interval):
        return Interval(max(self.l, interval.l), min(self.r, interval.r))


def partition(a, p, r):
    x = a[r - 1]
    for k in range(p, r - 1):
        next_x = x.get_intersect(a[k])
        if next_x.l <= next_x.r:
            x = next_x
    i = p - 1
    for k in range(p, r - 1):
        if a[k] < x:
            i += 1
            a[i], a[k] = a[k], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    j = i
    inter = a[i]
    for k in range(i + 1, r):
        next_x = x.get_intersect(a[k])
        if next_x.l <= next_x.r:
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


class FuzzySortTestCase(unittest.TestCase):

    def test_sort(self):
        for _ in range(1000):
            a = [Interval(0, -1) for _ in range(random.randint(1, 1000))]
            for i in range(len(a)):
                while a[i].l > a[i].r:
                    a[i].l = random.randint(-1000, 1000)
                    a[i].r = random.randint(-1000, 1000)
            quicksort(a, 0, len(a))
            c = a[0].l
            for i in range(1, len(a)):
                if a[i].l > c:
                    c = a[i].l
                self.assertTrue(a[i].l <= c <= a[i].r)

    def test_uniform(self):
        for _ in range(1000):
            l = random.randint(0, 100)
            r = l + random.randint(0, 100)
            a = [Interval(l, r) for _ in range(random.randint(1, 1000))]
            q, t = partition(a, 0, len(a))
            self.assertEqual(q, 0)
            self.assertEqual(t, len(a) - 1)


if __name__ == '__main__':
    unittest.main()
