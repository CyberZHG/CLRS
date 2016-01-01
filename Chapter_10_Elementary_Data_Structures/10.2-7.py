import random
import unittest


class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    values = []
    head = head.next
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def insert(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def reverse(head):
    prev = None
    node = head.next
    while node is not None:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    head.next = prev


class ProblemTestCase(unittest.TestCase):

    def test_empty(self):
        head = LinkListNode(None)
        reverse(head)
        self.assertEqual(to_list(head), [])

    def test_case(self):
        head = LinkListNode(None)
        insert(head, 1)
        insert(head, 2)
        insert(head, 3)
        self.assertEqual(to_list(head), [3, 2, 1])
        reverse(head)
        self.assertEqual(to_list(head), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
