import random
import unittest


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b


def lcm_multi(lst):
    la = lst[0]
    for i in xrange(1, len(lst)):
        la = lcm(la, lst[i])
    return la


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            n = random.randint(1, 100)
            lst = [random.randint(1, 10000) for _ in xrange(n)]
            la = lcm_multi(lst)
            for val in lst:
                self.assertEqual(la % val, 0)


if __name__ == '__main__':
    unittest.main()
