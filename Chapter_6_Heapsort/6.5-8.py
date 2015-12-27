import random
import unittest
from heap_util import random_max_heap, check_max_heap


def parent(i):
    return (i - 1) >> 1


def left(i):
    return (i << 1) + 1


def right(i):
    return (i << 1) + 2


def max_heapify(a, i):
    max_idx = i
    l, r = left(i), right(i)
    if l < len(a) and a[l] > a[max_idx]:
        max_idx = l
    if r < len(a) and a[r] > a[max_idx]:
        max_idx = r
    if max_idx != i:
        a[i], a[max_idx] = a[max_idx], a[i]
        max_heapify(a, max_idx)


def heap_increase_key(a, i, key):
    assert(key >= a[i])
    while i > 0 and key > a[parent(i)]:
        a[i] = a[parent(i)]
        i = parent(i)
    a[i] = key


def heap_delete(a, i):
    if i == len(a) - 1:
        del a[-1]
    else:
        a[i] = a[-1]
        del a[-1]
        max_heapify(a, i)
        heap_increase_key(a, i, a[i])


class HeapDeleteTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10000):
            heap = random_max_heap()
            a = heap[:]
            i = random.randint(0, len(heap) - 1)
            heap_delete(heap, i)
            del a[i]
            self.assertEqual(sorted(heap), sorted(a))


if __name__ == '__main__':
    unittest.main()
