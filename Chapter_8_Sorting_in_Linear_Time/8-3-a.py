import random
import unittest


def counting_sort(a, m):
    b = [0 for _ in range(len(a))]
    k = 10
    c = [0 for _ in range(k)]
    for s in a:
        c[ord(s[m]) - ord('0')] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        c[ord(a[i][m]) - ord('0')] -= 1
        b[c[ord(a[i][m]) - ord('0')]] = a[i]
    return b


def radix_sort(a):
    for m in range(len(a[0]) - 1, -1, -1):
        a = counting_sort(a, m)
    return a


def count_and_divide(a):
    a = map(str, a)
    b = [0 for _ in range(len(a))]
    k = 0
    for s in a:
        k = max(k, len(s))
    c = [0 for _ in range(k + 1)]
    for s in a:
        c[len(s)] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    r = c[:]
    for i in range(len(a) - 1, -1, -1):
        c[len(a[i])] -= 1
        b[c[len(a[i])]] = a[i]
    for i in range(k + 1):
        if c[i] < r[i]:
            b[c[i]:r[i]] = radix_sort(b[c[i]:r[i]])
    return map(int, b)


class SortTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(0, 1000000) for _ in range(random.randint(1, 1000))]
            self.assertEqual(count_and_divide(a), sorted(a))


if __name__ == '__main__':
    unittest.main()
