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
    while True:
        max_idx = i
        l, r = left(i), right(i)
        if l < len(a) and a[l] > a[max_idx]:
            max_idx = l
        if r < len(a) and a[r] > a[max_idx]:
            max_idx = r
        if max_idx == i:
            break
        a[i], a[max_idx] = a[max_idx], a[i]
        i = max_idx


class MaxHeapifyTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10000):
            heap = random_max_heap()
            idx = random.randint(0, len(heap)-1)
            if idx == 0:
                heap[0] = random.randint(1, 100)
            else:
                heap[idx] = heap[parent(idx)] - random.randint(0, 10)
            max_heapify(heap, idx)
            self.assertTrue(check_max_heap(heap))


if __name__ == '__main__':
    unittest.main()
