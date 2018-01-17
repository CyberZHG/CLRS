import random
import unittest


class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = LinkListNode(None)

    def enqueue(self, x):
        new_node = LinkListNode(x)
        if self.tail.next is None:
            self.head = new_node
            self.tail.next = self.head
        else:
            self.head.next = new_node
            self.head = new_node

    def dequeue(self):
        if self.tail.next is None:
            return None
        x = self.tail.next.value
        self.tail = self.tail.next
        return x


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            q = Queue()
            queue = []
            for _ in range(10000):
                op = random.randint(1, 2)
                if op == 1:
                    x = q.dequeue()
                    if len(queue) == 0:
                        y = None
                    else:
                        y = queue[0]
                        del queue[0]
                    self.assertEqual(x, y)
                else:
                    x = random.randint(0, 100)
                    q.enqueue(x)
                    queue.append(x)


if __name__ == '__main__':
    unittest.main()
