import unittest


def bellman_ford(vs, es, s):
    d = {v: 1e100 for v in vs}
    p = {v: None for v in vs}
    d[s] = 0
    for _ in xrange(len(vs) - 1):
        for (u, v, w) in es:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u
    return d, p


class ProblemTestCase(unittest.TestCase):

    def test_case_1(self):
        vs = ['s', 't', 'x', 'y', 'z']
        es = [('s', 't', 6), ('s', 'y', 7),
              ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
              ('x', 't', -2),
              ('y', 'x', -3), ('y', 'z', 9),
              ('z', 's', 2), ('z', 'x', 7)]
        d, p = bellman_ford(vs, es, 's')
        self.assertEqual(d, {'y': 7, 'x': 4, 's': 0, 'z': -2, 't': 2})
        self.assertEqual(p, {'y': 's', 'x': 'y', 's': None,
                             'z': 't', 't': 'x'})

    def test_case_2(self):
        vs = ['s', 't', 'x', 'y', 'z']
        es = [('s', 't', 6), ('s', 'y', 7),
              ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
              ('x', 't', -2),
              ('y', 'x', -3), ('y', 'z', 9),
              ('z', 's', 2), ('z', 'x', 7)]
        d, p = bellman_ford(vs, es, 'z')
        self.assertEqual(d, {'s': 2, 't': 4, 'x': 6, 'y': 9, 'z': 0})
        self.assertEqual(p, {'s': 'z', 't': 'x', 'x': 'y',
                             'y': 's', 'z': None})

    def test_case_3(self):
        vs = ['s', 't', 'x', 'y', 'z']
        es = [('s', 't', 6), ('s', 'y', 7),
              ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
              ('x', 't', -2),
              ('y', 'x', -3), ('y', 'z', 9),
              ('z', 's', 2), ('z', 'x', 4)]
        d, p = bellman_ford(vs, es, 's')
        self.assertEqual(d, {'s': 0, 't': 0, 'x': 2, 'y': 7, 'z': -2})
        self.assertEqual(p, {'s': None, 't': 'x', 'x': 'z',
                             'y': 's', 'z': 't'})


if __name__ == '__main__':
    unittest.main()
