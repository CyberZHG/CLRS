import unittest


def compute_prefix_function(p):
    m = len(p)
    p = ' ' + p
    pi = [0] * (m + 1)
    pi[1] = 0
    k = 0
    for q in xrange(2, m + 1):
        while k > 0 and p[k + 1] != p[q]:
            k = pi[k]
        if p[k + 1] == p[q]:
            k += 1
        pi[q] = k
    return pi[1:]


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        p = 'ababaca'
        pi = compute_prefix_function(p)
        self.assertEqual(pi, [0, 0, 1, 2, 3, 0, 1])
        p = 'ababbabbabbababbabb'
        pi = compute_prefix_function(p)
        self.assertEqual(pi, [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0,
                              1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
