import random
import unittest


def parent(i):
    return (i - 1) >> 1


def left(i):
    return (i << 1) + 1


def right(i):
    return (i << 1) + 2


def min_heapify(a, i):
    min_idx = i
    l, r = left(i), right(i)
    if l < len(a) and a[l] < a[min_idx]:
        min_idx = l
    if r < len(a) and a[r] < a[min_idx]:
        min_idx = r
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        min_heapify(a, min_idx)


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
    a.append((1e100, None))
    heap_decrease_key(a, len(a) - 1, key)


def merge_lists(lists):
    k = len(lists)
    heap = []
    for i in range(k):
        if len(lists[i]) > 0:
            min_heap_insert(heap, (lists[i][0], i))
    idx = [0 for lst in lists]
    a = []
    while len(heap) > 0:
        val, i = heap_extract_min(heap)
        a.append(val)
        idx[i] += 1
        if idx[i] < len(lists[i]):
            min_heap_insert(heap, (lists[i][idx[i]], i))
    return a


class MergeListTestCase(unittest.TestCase):

    def random_array(self):
        return [random.randint(0, 10000) for _ in range(random.randint(0, 100))]

    def test_random(self):
        for _ in range(1000):
            lists = []
            a = []
            for k in range(random.randint(0, 100)):
                lst = sorted(self.random_array())
                lists.append(lst)
                a += lst
            self.assertEqual(merge_lists(lists), sorted(a))


if __name__ == '__main__':
    unittest.main()
