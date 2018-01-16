import random
import unittest


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def random_heap(op):
    n = random.randint(1, 100)
    a = [0 for _ in range(n)]

    def random_heap_rec(p, i):
        a[i] = op(p, random.randint(1, 10))
        l, r = left(i), right(i)
        if l < n:
            random_heap_rec(a[i], l)
        if r < n:
            random_heap_rec(a[i], r)

    random_heap_rec(random.randint(1, 100), 0)
    return a


def random_max_heap():
    return random_heap(lambda x, y: x - y)


def random_min_heap():
    return random_heap(lambda x, y: x + y)


def check_heap(a, op):
    n = len(a)

    def check_heap_rec(i):
        l, r = left(i), right(i)
        if l < n:
            if not op(a[i], a[l]):
                return False
            return check_heap_rec(l)
        if r < n:
            if not op(a[i], r[r]):
                return False
            return check_heap_rec(r)
        return True

    return check_heap_rec(0)


def check_max_heap(a):
    return check_heap(a, lambda x, y: x >= y)


def check_min_heap(a):
    return check_heap(a, lambda x, y: x <= y)


class HeapUtilTestCase(unittest.TestCase):

    def test_random_max_heap(self):
        for _ in range(1000):
            heap = random_max_heap()
            self.assertTrue(check_max_heap(heap))

    def test_random_min_heap(self):
        for _ in range(1000):
            heap = random_min_heap()
            self.assertTrue(check_min_heap(heap))


if __name__ == '__main__':
    unittest.main()
