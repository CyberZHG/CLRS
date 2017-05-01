import random
import unittest


def matrix_chain_order(p):
    n = len(p)
    m = [[0 for _ in xrange(n)] for _ in xrange(n)]
    s = [[0 for _ in xrange(n)] for _ in xrange(n)]
    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l
            m[i][j] = 1e300
            for k in range(i + 1, j):
                q = m[i][k] + m[k][j] + p[i] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def optimal_parens(s, p, i, j):
    if i + 1 == j:
        return 'A_{}'.format(i)
    r = '('
    r += optimal_parens(s, p, i, s[i][j])
    r += ' X '
    r += optimal_parens(s, p, s[i][j], j)
    r += ')'
    return r


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        p = [30, 35, 15, 5, 10, 20, 25]
        m, s = matrix_chain_order(p)
        s = optimal_parens(s, p, 0, len(p) - 1)
        self.assertEqual(m[0][len(p) - 1], 15125)
        self.assertEqual(s, '((A_0 X (A_1 X A_2)) X ((A_3 X A_4) X A_5))')
        p = [5, 10, 3, 12, 5, 50, 6]
        m, s = matrix_chain_order(p)
        s = optimal_parens(s, p, 0, len(p) - 1)
        self.assertEqual(m[0][len(p) - 1], 2010)
        self.assertEqual(s, '((A_0 X A_1) X ((A_2 X A_3) X (A_4 X A_5)))')


if __name__ == '__main__':
    unittest.main()
