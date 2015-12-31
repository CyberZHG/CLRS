import random
import unittest


class Queue:
    def __init__(self, size):
        self.q = [-1 for _ in xrange(size)]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.tail + 1) % len(self.q) == self.head:
            raise Exception('overflow')
        self.q[self.tail] = x
        self.tail += 1
        if self.tail == len(self.q):
            self.tail = 0

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('underflow')
        x = self.q[self.head]
        self.head += 1
        if self.head == len(self.q):
            self.head = 0
        return x


class ProblemTestCase(unittest.TestCase):

    def test_underflow(self):
        q = Queue(1)
        with self.assertRaises(Exception) as context:
            q.dequeue()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_overflow(self):
        q = Queue(10)
        for i in range(9):
            q.enqueue(0)
        with self.assertRaises(Exception) as context:
            q.enqueue(0)
        self.assertTrue(context.exception.args[0], 'overflow')


if __name__ == '__main__':
    unittest.main()
