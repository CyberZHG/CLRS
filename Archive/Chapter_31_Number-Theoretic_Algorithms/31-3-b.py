import unittest


def fib(n):
    fibs = [0, 1] + [-1] * (n - 1)

    def fib_sub(n):
        if fibs[n] == -1:
            fibs[n] = fib_sub(n - 1) + fib_sub(n - 2)
        return fibs[n]
    return fib_sub(n)


class ProblemTestCase(unittest.TestCase):

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for i in range(1, n):
            c = a + b
            a, b = b, c
        return c

    def test_random(self):
        for n in xrange(500):
            self.assertEqual(fib(n), self.fib(n))


if __name__ == '__main__':
    unittest.main()
