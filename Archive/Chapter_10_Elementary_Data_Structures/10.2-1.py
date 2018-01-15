import random
import unittest


class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_str(head):
    values = []
    head = head.next
    while head is not None:
        values.append(head.value)
        head = head.next
    return ' '.join(map(str, values))


def insert(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def delete(head, x):
    while head is not None:
        if head.next is not None and head.next.value == x:
            head.next = head.next.next
        else:
            head = head.next


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        head = LinkListNode(None)
        insert(head, 1)
        self.assertEqual(to_str(head), "1")
        insert(head, 2)
        insert(head, 3)
        self.assertEqual(to_str(head), "3 2 1")
        delete(head, 2)
        self.assertEqual(to_str(head), "3 1")
        delete(head, 1)
        self.assertEqual(to_str(head), "3")
        delete(head, 3)
        self.assertEqual(to_str(head), "")
        insert(head, 4)
        self.assertEqual(to_str(head), "4")

    def test_random(self):
        head = LinkListNode(None)
        lst = []
        for _ in range(10000):
            op = random.randint(1, 3)
            x = random.randint(0, 100)
            if op == 1:
                delete(head, x)
                lst = filter(lambda v: v != x, lst)
            else:
                insert(head, x)
                lst.append(x)
            self.assertEqual(to_str(head), ' '.join(map(str, reversed(lst))))


if __name__ == '__main__':
    unittest.main()
