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
    a.append((1e100, None))
    heap_decrease_key(a, len(a) - 1, key)


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
    a.append((-1e100, None))
    heap_increase_key(a, len(a) - 1, key)


class Queue:
    def __init__(self):
        self.heap = []
        self.inc = 0

    def push(self, val):
        self.inc += 1
        min_heap_insert(self.heap, (self.inc, val))

    def front(self):
        return heap_minimum(self.heap)

    def pop(self):
        return heap_extract_min(self.heap)


class Stack:
    def __init__(self):
        self.heap = []
        self.inc = 0

    def push(self, val):
        self.inc += 1
        max_heap_insert(self.heap, (self.inc, val))

    def top(self):
        return heap_maximum(self.heap)

    def pop(self):
        return heap_extract_max(self.heap)


class QueueTestCase(unittest.TestCase):

    def test_random(self):
        a = []
        q = Queue()
        for _ in range(10000):
            op = random.randint(1, 5)
            if len(a) == 0:
                op = 3
            if op == 1:
                self.assertTrue(q.front(), a[0])
            elif op == 2:
                self.assertTrue(q.pop(), a[0])
                del a[0]
            else:
                val = random.randint(1, 100000)
                a.append(val)
                q.push(val)


class StackTestCase(unittest.TestCase):

    def test_random(self):
        a = []
        q = Stack()
        for _ in range(10000):
            op = random.randint(1, 5)
            if len(a) == 0:
                op = 3
            if op == 1:
                self.assertTrue(q.top(), a[-1])
            elif op == 2:
                self.assertTrue(q.pop(), a[-1])
                del a[-1]
            else:
                val = random.randint(1, 100000)
                a.append(val)
                q.push(val)


if __name__ == '__main__':
    unittest.main()
