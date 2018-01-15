import random
import unittest


class BlackBoxStack:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return len(self.s) == 0

    def push(self, x):
        self.s.append(x)

    def pop(self):
        x = self.s[-1]
        del self.s[-1]
        return x


class Queue:
    def __init__(self):
        self.stack_in = BlackBoxStack()
        self.stack_out = BlackBoxStack()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def enqueue(self, x):
        self.stack_in.push(x)

    def dequeue(self):
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise Exception('underflow')
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()


class ProblemTestCase(unittest.TestCase):

    def test_underflow(self):
        q = Queue()
        with self.assertRaises(Exception) as context:
            q.dequeue()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_random(self):
        q = Queue()
        test_q = []
        for _ in range(100000):
            op = random.randint(1, 3)
            if op >= 2:
                x = random.randint(1, 100000)
                q.enqueue(x)
                test_q.append(x)
            else:
                if len(test_q) == 0:
                    with self.assertRaises(Exception) as context:
                        q.dequeue()
                    self.assertTrue(context.exception.args[0], 'underflow')
                else:
                    x = q.dequeue()
                    y = test_q[0]
                    del test_q[0]
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
