import random
import unittest


class BlackBoxQueue:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return len(self.s) == 0

    def enqueue(self, x):
        self.s.append(x)

    def dequeue(self):
        x = self.s[0]
        del self.s[0]
        return x


class Stack:
    def __init__(self):
        self.queue_in = BlackBoxQueue()
        self.queue_out = BlackBoxQueue()

    def is_empty(self):
        return self.queue_in.is_empty()

    def push(self, x):
        self.queue_in.enqueue(x)

    def pop(self):
        if self.queue_in.is_empty():
            raise Exception('underflow')
        while True:
            x = self.queue_in.dequeue()
            if self.queue_in.is_empty():
                break
            self.queue_out.enqueue(x)
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return x


class ProblemTestCase(unittest.TestCase):

    def test_underflow(self):
        s = Stack()
        with self.assertRaises(Exception) as context:
            s.pop()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_random(self):
        s = Stack()
        test_s = []
        for _ in range(10000):
            op = random.randint(1, 3)
            if op >= 2:
                x = random.randint(1, 100000)
                s.push(x)
                test_s.append(x)
            else:
                if len(test_s) == 0:
                    with self.assertRaises(Exception) as context:
                        s.pop()
                    self.assertTrue(context.exception.args[0], 'underflow')
                else:
                    x = s.pop()
                    y = test_s[-1]
                    del test_s[-1]
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
