import unittest


m = 11


class LinearProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class QuadraticProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i + 3 * i * i) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class DoubleHashing:
    def __init__(self):
        global m
        self.slots = [None for _ in xrange(m)]

    def insert(self, key):
        global m
        i = 0
        h2 = 1 + (key % (m - 1))
        while True:
            pos = (key + i * h2) % m
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        a = [10, 22, 31, 4, 15, 28, 17, 88, 59]
        li = LinearProbing()
        qu = QuadraticProbing()
        do = DoubleHashing()
        for v in a:
            li.insert(v)
            qu.insert(v)
            do.insert(v)
        self.assertEqual(li.slots, [22, 88, None, None, 4, 15, 28, 17, 59, 31, 10])
        self.assertEqual(qu.slots, [22, None, 88, 17, 4, None, 28, 59, 15, 31, 10])
        self.assertEqual(do.slots, [22, None, 59, 17, 4, 15, 28, 88, None, 31, 10])


if __name__ == '__main__':
    unittest.main()
