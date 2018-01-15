import random
import unittest


def bin2dec(s):
    n = len(s)
    if n == 1:
        return ord(s) - ord('0')
    m = n // 2
    h = bin2dec(s[:m])
    r = bin2dec(s[m:])
    return (h << (n - m)) + r


class ProblemTestCase(unittest.TestCase):

    def test_random(self):
        for _ in xrange(10000):
            n = random.randint(1, 1000)
            b = [random.randint(0, 1) for _ in xrange(n)]
            num = 0
            for c in b:
                num = (num << 1) + c
            s = ''.join(map(lambda x: chr(ord('0') + x), b))
            self.assertEqual(bin2dec(s), num)


if __name__ == '__main__':
    unittest.main()
