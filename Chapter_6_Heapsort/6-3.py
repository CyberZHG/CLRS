import math
import random
import unittest


def extract_min(a):
    m, n = len(a), len(a[0])
    val = a[0][0]
    a[0][0] = 1e8

    def maintain(i, j):
        min_i, min_j = i, j
        if i + 1 < m and a[i + 1][j] < a[min_i][min_j]:
            min_i, min_j = i + 1, j
        if j + 1 < n and a[i][j + 1] < a[min_i][min_j]:
            min_i, min_j = i, j + 1
        if min_i != i or min_j != j:
            a[i][j], a[min_i][min_j] = a[min_i][min_j], a[i][j]
            maintain(min_i, min_j)

    maintain(0, 0)
    return val


def insert(a, val):
    m, n = len(a), len(a[0])
    a[m - 1][n - 1] = val

    def maintain(i, j):
        max_i, max_j = i, j
        if i - 1 >= 0 and a[i - 1][j] > a[max_i][max_j]:
            max_i, max_j = i - 1, j
        if j - 1 >= 0 and a[i][j - 1] > a[max_i][max_j]:
            max_i, max_j = i, j - 1
        if max_i != i or max_j != j:
            a[i][j], a[max_i][max_j] = a[max_i][max_j], a[i][j]
            maintain(max_i, max_j)

    maintain(m - 1, n - 1)


def sort_elements(a):
    m = len(a)
    n = int(math.ceil(math.sqrt(m)))
    y = [[1e8 for _ in range(n)] for _ in range(n)]
    for val in a:
        insert(y, val)
    a = []
    for _ in range(m):
        a.append(extract_min(y))
    return a


def find(a, val):
    m, n = len(a), len(a[0])
    i, j = 0, n - 1
    while i < m and j >= 0:
        if a[i][j] == val:
            return i, j
        elif a[i][j] > val:
            j -= 1
        else:
            i += 1
    return -1, -1


class YoungTestCase(unittest.TestCase):

    def randomYoung(self):
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        a = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    a[i][j] = a[i][j - 1] + random.randint(0, 10)
                elif i > 0 and j == 0:
                    a[i][j] = a[i - 1][j] + random.randint(0, 10)
                elif i > 0 and j > 0:
                    a[i][j] = max(a[i - 1][j], a[i][j - 1]) + random.randint(0, 10)
        return a

    def checkYoung(self, a):
        m = len(a)
        n = len(a[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    if a[i][j] < a[i][j - 1]:
                        return False
                elif i > 0 and j == 0:
                    if a[i][j] < a[i - 1][j]:
                        return False
                elif i > 0 and j > 0:
                    if a[i][j] < max(a[i - 1][j], a[i][j - 1]):
                        return False
        return True

    def test_extract_min(self):
        for _ in range(1000):
            a = self.randomYoung()
            b = []
            for v in a:
                b += v
            b = sorted(b)[::-1]
            n = len(b)
            for _ in range(n):
                r = extract_min(a)
                self.assertEqual(r, b[-1])
                self.checkYoung(a)
                del b[-1]

    def test_insert(self):
        for _ in range(100):
            a = self.randomYoung()
            for _ in range(100):
                insert(a, random.randint(1, 10000))
                self.assertTrue(self.checkYoung(a))

    def test_sort(self):
        for _ in range(100):
            a = [random.randint(1, 100000) for _ in range(random.randint(1, 100))]
            b = sorted(a)
            self.assertEqual(sort_elements(a), b)

    def test_find(self):
        for _ in range(10000):
            a = self.randomYoung()
            val = random.randint(0, 100)
            i, j = find(a, val)
            if i == -1 and j == -1:
                for lst in a:
                    self.assertTrue(val not in lst)
            else:
                self.assertEqual(a[i][j], val)


if __name__ == '__main__':
    unittest.main()
