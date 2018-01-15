import random
import unittest


class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        x = LinkedListNode(key)
        if self.head is None:
            self.head = x
            x.next = x
            x.prev = x
        else:
            x.prev = self.head.prev
            x.next = self.head
            x.prev.next = x
            x.next.prev = x

    def remove(self):
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next

    def forward(self, step):
        while step > 0:
            step -= 1
            self.head = self.head.next


def josephus_permutation(n, m):
    lst = LinkedList()
    for i in xrange(1, n + 1):
        lst.insert(i)
    perm = []
    while lst.head is not None:
        lst.forward(m - 1)
        perm.append(lst.head.key)
        lst.remove()
    return perm


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        a = josephus_permutation(7, 3)
        self.assertEqual(a, [3, 6, 2, 7, 5, 1, 4])

    def test_random(self):
        for _ in xrange(1000):
            n = random.randint(1, 1000)
            m = random.randint(1, min(n, 10))
            p = josephus_permutation(n, m)
            a = [i for i in xrange(1, n + 1)]
            b = []
            idx = 0
            while len(a) > 0:
                idx = (idx + m - 1) % len(a)
                b.append(a[idx])
                del a[idx]
            self.assertEqual(p, b)


if __name__ == '__main__':
    unittest.main()
