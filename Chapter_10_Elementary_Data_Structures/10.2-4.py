import random
import unittest


class LinkListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, x):
        x = LinkListNode(x)
        x.next = self.nil.next
        x.prev = self.nil
        x.next.prev = x
        x.prev.next = x

    def search(self, k):
        self.nil.key = k
        x = self.nil.next
        while x.key != k:
            x = x.next
        if x == self.nil:
            return None
        return x


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        lst = LinkList()
        lst.insert(1)
        lst.insert(3)
        self.assertTrue(lst.search(2) is None)
        self.assertEqual(lst.search(1).key, 1)


if __name__ == '__main__':
    unittest.main()
