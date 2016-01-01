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
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            if value < self.head.value:
                new_node.next = self.head
                self.head = new_node
            else:
                x = self.head
                while x.next is not None and x.next.value < value:
                    x = x.next
                if x.next is None or x.next < value:
                    new_node.next = x.next
                    x.next = new_node

    def minimum(self):
        if self.head is None:
            return None
        return self.head.value

    def extract_min(self):
        if self.head is None:
            return None
        x = self.head.value
        self.head = self.head.next
        return x

    def union(self, other):
        head = LinkedListNode(None)
        x = head
        while self.head is not None or other.head is not None:
            if other.head is None:
                x.next = self.head
                self.head = self.head.next
            elif self.head is None:
                x.next = other.head
                other.head = other.head.next
            elif self.head.value <= other.head.value:
                x.next = self.head
                self.head = self.head.next
            else:
                x.next = other.head
                other.head = other.head.next
            if x.next.value != x.value:
                x = x.next
        x.next = None
        self.head = head.next


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        heap1 = MergeableHeap()
        heap2 = MergeableHeap()
        heap1.insert(1)
        heap1.insert(3)
        heap1.insert(5)
        self.assertEqual(heap1.to_list(), [1, 3, 5])
        self.assertEqual(heap1.minimum(), 1)
        self.assertEqual(heap1.extract_min(), 1)
        self.assertEqual(heap1.to_list(), [3, 5])
        heap2.insert(2)
        heap2.insert(3)
        heap2.insert(4)
        self.assertEqual(heap2.to_list(), [2, 3, 4])
        heap1.union(heap2)
        self.assertEqual(heap1.to_list(), [2, 3, 4, 5])
        self.assertEqual(heap1.extract_min(), 2)
        self.assertEqual(heap1.extract_min(), 3)
        self.assertEqual(heap1.extract_min(), 4)


if __name__ == '__main__':
    unittest.main()
