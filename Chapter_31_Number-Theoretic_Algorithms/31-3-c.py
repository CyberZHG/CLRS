import unittest


class Matrix:
    def __init__(self, data):
        self.data = data

    def __mul__(self, x):
        a = self.data
        b = x.data
        c = [[0, 0], [0, 0]]
        for i in xrange(2):
            for j in xrange(2):
                for k in xrange(2):
                    c[i][j] += a[i][k] * b[k][j]
        return Matrix(c)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    m = Matrix([[1, 1], [1, 0]])
    r = Matrix([[1, 0], [0, 1]])
    i = 0
    n -= 1
    while (1 << i) <= n:
        if (n & (1 << i)) > 0:
            r *= m
        m *= m
        i += 1
    return r.data[0][0]


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
        for n in xrange(5000):
            self.assertEqual(fib(n), self.fib(n))


if __name__ == '__main__':
    unittest.main()
