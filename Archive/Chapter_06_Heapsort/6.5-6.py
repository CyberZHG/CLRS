import random
import unittest
from heap_util import check_max_heap


def parent(i):
    return (i - 1) >> 1


def left(i):
    return (i << 1) + 1


def right(i):
    return (i << 1) + 2


def max_heapify(a, i):
    max_idx = i
    lt, rt = left(i), right(i)
    if lt < len(a) and a[lt] > a[max_idx]:
        max_idx = lt
    if rt < len(a) and a[rt] > a[max_idx]:
        max_idx = rt
    if max_idx != i:
        a[i], a[max_idx] = a[max_idx], a[i]
        max_heapify(a, max_idx)


def heap_maximum(a):
    assert(len(a) > 0)
    return a[0]


def heap_extract_max(a):
    assert(len(a) > 0)
    val = a[0]
    a[0] = a[-1]
    del a[-1]
    max_heapify(a, 0)
    return val


def heap_increase_key(a, i, key):
    assert(key >= a[i])
    while i > 0 and key > a[parent(i)]:
        a[i] = a[parent(i)]
        i = parent(i)
    a[i] = key


def max_heap_insert(a, key):
    a.append(-1e100)
    heap_increase_key(a, len(a) - 1, key)


class PriorityQueueTestCase(unittest.TestCase):

    def test_random(self):
        heap = []
        for _ in range(10000):
            op = random.randint(1, 5)
            if op == 1:
                if len(heap) == 0:
                    continue
                r = heap_maximum(heap)
                for a in heap:
                    self.assertTrue(r >= a)
            elif op == 2:
                if len(heap) == 0:
                    continue
                le = len(heap)
                m = heap_maximum(heap)
                r = heap_extract_max(heap)
                self.assertEqual(m, r)
                self.assertEqual(len(heap), le - 1)
                self.assertTrue(check_max_heap(heap))
            else:
                le = len(heap)
                max_heap_insert(heap, random.randint(1, 10000))
                self.assertEqual(len(heap), le + 1)
                self.assertTrue(check_max_heap(heap))


if __name__ == '__main__':
    unittest.main()
