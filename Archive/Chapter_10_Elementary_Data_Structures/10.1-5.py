import random
import unittest


class Deque:
    def __init__(self, size):
        self.q = [-1 for _ in xrange(size)]
        self.front = 0
        self.back = 0

    def push_front(self, x):
        if (self.back + 1) % len(self.q) == self.front:
            raise Exception('overflow')
        self.front -= 1
        if self.front == -1:
            self.front = len(self.q) - 1
        self.q[self.front] = x

    def push_back(self, x):
        if (self.back + 1) % len(self.q) == self.front:
            raise Exception('overflow')
        self.q[self.back] = x
        self.back += 1
        if self.back == len(self.q):
            self.back = 0

    def pop_front(self):
        if self.front == self.back:
            raise Exception('underflow')
        x = self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = 0
        return x

    def pop_back(self):
        if self.front == self.back:
            raise Exception('underflow')
        self.back -= 1
        if self.back == -1:
            self.back = len(self.q) - 1
        return self.q[self.back]


class ProblemTestCase(unittest.TestCase):

    def test_underflow(self):
        q = Deque(1)
        with self.assertRaises(Exception) as context:
            q.pop_front()
        self.assertTrue(context.exception.args[0], 'underflow')
        q = Deque(1)
        with self.assertRaises(Exception) as context:
            q.pop_back()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_overflow(self):
        q = Deque(10)
        for i in range(9):
            q.push_front(0)
        with self.assertRaises(Exception) as context:
            q.push_front(0)
        self.assertTrue(context.exception.args[0], 'overflow')
        q = Deque(10)
        for i in range(9):
            q.push_back(0)
        with self.assertRaises(Exception) as context:
            q.push_back(0)
        self.assertTrue(context.exception.args[0], 'overflow')

    def test_random(self):
        q = Deque(11)
        test_q = []
        for _ in range(100000):
            x = random.randint(1, 100000)
            op = random.randint(1, 4)
            if op == 1:
                if len(test_q) == 10:
                    with self.assertRaises(Exception) as context:
                        q.push_front(x)
                    self.assertTrue(context.exception.args[0], 'overflow')
                else:
                    test_q = [x] + test_q
                    q.push_front(x)
            elif op == 2:
                if len(test_q) == 10:
                    with self.assertRaises(Exception) as context:
                        q.push_back(x)
                    self.assertTrue(context.exception.args[0], 'overflow')
                else:
                    test_q.append(x)
                    q.push_back(x)
            elif op == 3:
                if len(test_q) == 0:
                    with self.assertRaises(Exception) as context:
                        q.pop_front()
                    self.assertTrue(context.exception.args[0], 'underflow')
                else:
                    x = test_q[0]
                    del test_q[0]
                    y = q.pop_front()
                    self.assertEqual(x, y)
            else:
                if len(test_q) == 0:
                    with self.assertRaises(Exception) as context:
                        q.pop_back()
                    self.assertTrue(context.exception.args[0], 'underflow')
                else:
                    x = test_q[-1]
                    del test_q[-1]
                    y = q.pop_back()
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
