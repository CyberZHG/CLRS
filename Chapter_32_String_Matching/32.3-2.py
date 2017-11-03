import unittest


def compute_transition_function(p, s):
    m = len(p)
    d = {}
    for q in range(m + 1):
        for a in s:
            k = min(m + 1, q + 2)
            while k > 0:
                k -= 1
                if p[:k] == (p[:q] + a)[-k:]:
                    break
            d[(q, a)] = k
    return d


class ProblemTestCase(unittest.TestCase):

    def print_sorted(self, x, s):
        x = sorted(list(map(lambda (k, v): (k, v), x.items())))
        le = len(s)
        output = ''
        for i in xrange(len(x)):
            if i % le == 0:
                print(output)
                output = str(i / le)
            output += ' ' + str(x[i][1])
        print(output)

    def test_case(self):
        s = 'ab'
        self.print_sorted(compute_transition_function('aabab', s), s)
        self.print_sorted(compute_transition_function('ababbabbababbababbabb',
                                                      s), s)


if __name__ == '__main__':
    unittest.main()
