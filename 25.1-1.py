import unittest


def print_matrix(l):
    s = '\\left \\{ \\begin{matrix}\n'
    n = len(l)
    for i in xrange(n):
        for j in xrange(n):
            if j > 0:
                s += ' & '
            if l[i][j] > 1e50:
                s += '\infty'
            else:
                s += str(int(l[i][j]))
        s += '\\\\\n'
    s += '\\end{matrix} \\right \\}\n'
    print s


def extend_shortest_paths(l, w):
    n = len(l)
    ll = [[1e100 for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                ll[i][j] = min(ll[i][j], l[i][k] + w[k][j])
    return ll


def slow_all_pairs_shortest_paths(w):
    n = len(w)
    l = w
    for m in xrange(n - 2):
        l = extend_shortest_paths(l, w)
    return l


def fast_all_pairs_shortest_paths(w):
    n = len(w)
    l = w
    m = 1
    while m < n - 1:
        l = extend_shortest_paths(l, l)
        m *= 2
    return l


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        inf = 1e100
        w = [[0, inf, inf, inf, -1, inf],
             [1, 0, inf, 2, inf, inf],
             [inf, 2, 0, inf, inf, -8],
             [-4, inf, inf, 0, 3, inf],
             [inf, 7, inf, inf, 0, inf],
             [inf, 5, 10, inf, inf, 0]]
        self.assertEqual(slow_all_pairs_shortest_paths(w),
                         fast_all_pairs_shortest_paths(w))


if __name__ == '__main__':
    unittest.main()
