import random
import unittest


def get_key(s, i):
    if i >= len(s):
        return 0
    return ord(s[i]) - ord('a') + 1


def counting_sort(a, p=0):
    k = 27
    b = ['' for _ in range(len(a))]
    c = [0 for _ in range(k)]
    for s in a:
        c[get_key(s, p)] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a) - 1, -1, -1):
        c[get_key(a[i], p)] -= 1
        b[c[get_key(a[i], p)]] = a[i]
    for i in range(1, k):
        if c[i] < r[i]:
            b[c[i]:r[i]] = counting_sort(b[c[i]:r[i]], p+1)
    return b


class SortTestCase(unittest.TestCase):

    def random_str(self):
        n = random.randint(1, 100)
        s = ""
        for i in range(n):
            s += chr(ord('a') + random.randint(0, 25))
        return s

    def test_random(self):
        for _ in range(100):
            a = [self.random_str() for _ in range(random.randint(1, 1000))]
            self.assertEqual(counting_sort(a), sorted(a))


if __name__ == '__main__':
    unittest.main()
