import random
import unittest


def partition(a, p, r):
    if p == r:
        return p
    x = a[r - 1]
    i = p - 1
    cnt = 0
    for j in range(p, r - 1):
        if a[j] <= x:
            if a[j] == x:
                cnt += 1
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i - cnt // 2


class PartitionTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10000):
            a = [random.randint(0, 10000) for _ in range(random.randint(1, 100))]
            p = random.randint(0, len(a) - 1)
            r = random.randint(0, len(a) - 1)
            if p > r:
                p, r = r, p
            q = partition(a, p, r)
            for i in range(p, q):
                self.assertTrue(a[i] <= a[q])
            for i in range(q + 1, r):
                self.assertTrue(a[i] >= a[q])

    def test_uniform(self):
        for _ in range(10000):
            num = random.randint(0, 10000)
            a = [num for _ in range(random.randint(1, 100))]
            p = random.randint(0, len(a) - 1)
            r = random.randint(0, len(a) - 1)
            if p > r:
                p, r = r, p
            q = partition(a, p, r)
            self.assertEqual(q, (p + r) / 2)


if __name__ == '__main__':
    unittest.main()
