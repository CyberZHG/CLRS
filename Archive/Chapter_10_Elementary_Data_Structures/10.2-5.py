import random
import unittest


class LinkListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Dict:
    def __init__(self):
        self.nil = LinkListNode(None, None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, key, value):
        x = self.search_node(key)
        if x is None:
            x = LinkListNode(key, value)
            x.next = self.nil.next
            x.prev = self.nil
            x.next.prev = x
            x.prev.next = x
        else:
            x.value = value

    def delete(self, key):
        x = self.search_node(key)
        if x is not None:
            x.next.prev = x.prev
            x.prev.next = x.next

    def search_node(self, key):
        self.nil.key = key
        x = self.nil.next
        while x.key != key:
            x = x.next
        if x == self.nil:
            return None
        return x

    def search(self, key):
        x = self.search_node(key)
        if x is None:
            return None
        return x.value


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10):
            d = Dict()
            test_dict = {}
            for _ in range(10000):
                op = random.randint(1, 3)
                key = random.randint(1, 100)
                if op == 1:
                    value = random.randint(1, 100000000)
                    d.insert(key, value)
                    test_dict[key] = value
                elif op == 2:
                    d.delete(key)
                    if key in test_dict.keys():
                        del test_dict[key]
                else:
                    x = d.search(key)
                    if key in test_dict.keys():
                        y = test_dict[key]
                    else:
                        y = None
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
