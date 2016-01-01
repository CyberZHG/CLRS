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

    def insert(self, key):
        x = LinkListNode(key)
        x.next = self.nil.next
        x.prev = self.nil
        x.next.prev = x
        x.prev.next = x

    def values(self):
        values = []
        x = self.nil.next
        while x != self.nil:
            values.append(x.key)
            x = x.next
        return values


def union(list_1, list_2):
    list_1.nil.next.prev = list_2.nil.prev
    list_2.nil.prev.next = list_1.nil.next
    list_1.nil.next = list_2.nil.next
    list_2.nil.next.prev = list_1.nil
    return list_1


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        list_1 = LinkList()
        list_1.insert(1)
        list_1.insert(3)
        list_1.insert(4)
        list_2 = LinkList()
        list_2.insert(2)
        list_2.insert(4)
        list_2.insert(6)
        union_list = union(list_1, list_2)
        self.assertTrue(sorted(union_list.values()), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
