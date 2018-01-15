import random
import unittest
from heap_util import random_min_heap, check_min_heap


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


class MinHeapifyTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10000):
            heap = random_min_heap()
            idx = random.randint(0, len(heap) - 1)
            if idx == 0:
                heap[0] = random.randint(1, 100)
            else:
                heap[idx] = heap[parent(idx)] + random.randint(0, 10)
            min_heapify(heap, idx)
            self.assertTrue(check_min_heap(heap))


if __name__ == '__main__':
    unittest.main()
