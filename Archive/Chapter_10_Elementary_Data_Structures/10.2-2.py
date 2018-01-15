import random
import unittest


class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def push(head, x):
    new_node = LinkListNode(x)
    new_node.next = head.next
    head.next = new_node


def pop(head):
    if head.next is None:
        return None
    x = head.next.value
    head.next = head.next.next
    return x


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            head = LinkListNode(None)
            stack = []
            for _ in range(10000):
                op = random.randint(1, 2)
                if op == 1:
                    x = pop(head)
                    if len(stack) == 0:
                        y = None
                    else:
                        y = stack[-1]
                        del stack[-1]
                    self.assertEqual(x, y)
                else:
                    x = random.randint(0, 100)
                    push(head, x)
                    stack.append(x)


if __name__ == '__main__':
    unittest.main()
