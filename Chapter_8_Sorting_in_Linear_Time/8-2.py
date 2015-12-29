import random
import unittest


def counting_in_place(a):
    k = max(a)
    c = [0 for _ in range(k + 1)]
    for v in a:
        c[v] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a)):
        while True:
            if a[i] == 0:
                if i < r[0]:
                    break
            else:
                if r[a[i] - 1] <= i < r[a[i]]:
                    break
            c[a[i]] -= 1
            pos = c[a[i]]
            a[i], a[pos] = a[pos], a[i]


class CountingInPlaceTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(0, 10) for _ in range(random.randint(1, 1000))]
            b = sorted(a)
            counting_in_place(a)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
