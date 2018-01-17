import random
import unittest


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MergeableHeap:
    def __init__(self):
        self.head = None

    def to_list(self):
        values = []
        x = self.head
        while x is not None:
            values.append(x.value)
            x = x.next
        return values

    def insert(self, value):
        x = LinkedListNode(value)
        if self.head is None:
            self.head = x
        else:
            x.next = self.head
            self.head = x

    def minimum(self):
        if self.head is None:
            return None
        min_val = self.head.value
        x = self.head.next
        while x is not None:
            min_val = min(min_val, x.value)
            x = x.next
        return min_val

    def delete(self, value):
        prev = None
        x = self.head
        while x is not None:
            if x.value == value:
                if x == self.head:
                    self.head = self.head.next
                prev.next = x.next
            prev = x
            x = x.next

    def extract_min(self):
        x = self.minimum()
        self.delete(x)
        return x

    def union(self, other):
        if self.head is None:
            self.head = other.head
        else:
            x = self.head
            while x.next is not None:
                x = x.next
            x.next = other.head


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        heap1 = MergeableHeap()
        heap2 = MergeableHeap()
        heap1.insert(1)
        heap1.insert(3)
        heap1.insert(5)
        self.assertEqual(heap1.to_list(), [5, 3, 1])
        self.assertEqual(heap1.minimum(), 1)
        self.assertEqual(heap1.extract_min(), 1)
        self.assertEqual(heap1.to_list(), [5, 3])
        heap2.insert(2)
        heap2.insert(3)
        heap2.insert(4)
        self.assertEqual(heap2.to_list(), [4, 3, 2])
        heap1.union(heap2)
        self.assertEqual(heap1.to_list(), [5, 3, 4, 3, 2])
        self.assertEqual(heap1.extract_min(), 2)
        self.assertEqual(heap1.extract_min(), 3)
        self.assertEqual(heap1.extract_min(), 4)


if __name__ == '__main__':
    unittest.main()
