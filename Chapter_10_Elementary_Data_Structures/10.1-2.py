import random
import unittest


n = 100
a = [-1 for _ in xrange(n)]


class Stack1:
    def __init__(self):
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, x):
        global a
        self.top += 1
        a[self.top] = x

    def pop(self):
        global a
        self.top -= 1
        return a[self.top + 1]


class Stack2:
    def __init__(self):
        self.top = n

    def is_empty(self):
        return self.top == n

    def push(self, x):
        global a
        self.top -= 1
        a[self.top] = x

    def pop(self):
        global a
        self.top += 1
        return a[self.top - 1]


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        stack_1 = Stack1()
        stack_2 = Stack2()
        test_stack_1 = []
        test_stack_2 = []
        for _ in range(1000000):
            stk = stack_1
            test_stk = test_stack_1
            if random.randint(0, 1) == 0:
                stk = stack_2
                test_stk = test_stack_2
            if random.randint(0, 1) == 0:
                if len(test_stk) > 0:
                    x = stk.pop()
                    y = test_stk[-1]
                    del test_stk[-1]
                    self.assertEqual(x, y)
            else:
                if len(test_stack_1) + len(test_stack_2) < n:
                    x = random.randint(0, 1000000)
                    stk.push(x)
                    test_stk.append(x)
            self.assertEqual(stk.is_empty(), len(test_stk) == 0)


if __name__ == '__main__':
    unittest.main()
