import random
import unittest
from heap_util import check_min_heap


def parent(i):
    return (i - 1) >> 1


def left(i):
    return (i << 1) + 1


def right(i):
    return (i << 1) + 2


def min_heapify(a, i):
    min_idx = i
    lt, rt = left(i), right(i)
    if lt < len(a) and a[lt] < a[min_idx]:
        min_idx = lt
    if rt < len(a) and a[rt] < a[min_idx]:
        min_idx = rt
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        min_heapify(a, min_idx)


def heap_minimum(a):
    assert(len(a) > 0)
    return a[0]


def heap_extract_min(a):
    assert(len(a) > 0)
    val = a[0]
    a[0] = a[-1]
    del a[-1]
    min_heapify(a, 0)
    return val


def heap_decrease_key(a, i, key):
    assert(key <= a[i])
    a[i] = key
    while i > 0 and a[i] < a[parent(i)]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


def min_heap_insert(a, key):
    a.append(1e100)
    heap_decrease_key(a, len(a) - 1, key)


class PriorityQueueTestCase(unittest.TestCase):

    def test_random(self):
        heap = []
        for _ in range(10000):
            op = random.randint(1, 5)
            if op == 1:
                if len(heap) == 0:
                    continue
                r = heap_minimum(heap)
                for a in heap:
                    self.assertTrue(r <= a)
            elif op == 2:
                if len(heap) == 0:
                    continue
                le = len(heap)
                m = heap_minimum(heap)
                r = heap_extract_min(heap)
                self.assertEqual(m, r)
                self.assertEqual(len(heap), le - 1)
                self.assertTrue(check_min_heap(heap))
            else:
                le = len(heap)
                min_heap_insert(heap, random.randint(1, 10000))
                self.assertEqual(len(heap), le + 1)
                self.assertTrue(check_min_heap(heap))


if __name__ == '__main__':
    unittest.main()
