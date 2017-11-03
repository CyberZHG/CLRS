import random
import unittest


def parent(d, i):
    return (i - 1) / d


def child(d, i, k):
    return (i * d) + k


def max_heapify(d, a, i):
    max_idx = i
    for k in range(1, d + 1):
        c = child(d, i, k)
        if c < len(a) and a[c] > a[max_idx]:
            max_idx = c
    if max_idx != i:
        a[i], a[max_idx] = a[max_idx], a[i]
        max_heapify(d, a, max_idx)


def extract_max(d, a):
    assert(len(a) > 0)
    val = a[0]
    a[0] = a[-1]
    del a[-1]
    max_heapify(d, a, 0)
    return val


def increase_key(d, a, i, key):
    assert(key >= a[i])
    while i > 0 and key > a[parent(d, i)]:
        a[i] = a[parent(d, i)]
        i = parent(d, i)
    a[i] = key


def insert(d, a, key):
    a.append(-1e100)
    increase_key(d, a, len(a) - 1, key)


class DaryHeapTestCase(unittest.TestCase):

    def check_max_heap(self, d, a):
        def check_heap_rec(i):
            for k in range(1, d + 1):
                c = child(d, i, k)
                if c < len(a):
                    if a[i] < a[c]:
                        print d, a, i
                        return False
                    if not check_heap_rec(c):
                        return False
            return True
        return check_heap_rec(0)

    def test_random(self):
        for _ in range(100):
            d = random.randint(1, 10)
            heap = []
            for _ in range(1000):
                op = random.randint(1, 5)
                if len(heap) == 0:
                    op = 2
                if op == 1:
                    le = len(heap)
                    m = heap[0]
                    r = extract_max(d, heap)
                    self.assertEqual(m, r)
                    self.assertEqual(len(heap), le - 1)
                    self.assertTrue(self.check_max_heap(d, heap))
                else:
                    le = len(heap)
                    insert(d, heap, random.randint(1, 10000))
                    self.assertEqual(len(heap), le + 1)
                    self.assertTrue(self.check_max_heap(d, heap))


if __name__ == '__main__':
    unittest.main()
