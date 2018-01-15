import math
import random
import unittest


class ProtoVEB:
    def __init__(self, u):
        self.u = u
        self.sqrt = int(math.sqrt(u))
        if self.is_leaf():
            self.a = [0, 0]
        else:
            self.summary = ProtoVEB(self.sqrt)
            self.cluster = []
            for _ in xrange(self.sqrt):
                self.cluster.append(ProtoVEB(self.sqrt))

    def is_leaf(self):
        return self.u == 2

    def high(self, x):
        return x / self.sqrt

    def low(self, x):
        return x % self.sqrt

    def index(self, x, y):
        return x * self.sqrt + y

    def member(self, x):
        if self.is_leaf():
            return self.a[x]
        return self.cluster[self.high(x)].member(self.low(x))

    def minimum(self):
        if self.is_leaf():
            if self.a[0] > 0:
                return 0
            if self.a[1] > 0:
                return 1
            return None
        min_idx = self.summary.minimum()
        if min_idx is None:
            return None
        offset = self.cluster[min_idx].minimum()
        return self.index(min_idx, offset)

    def maximum(self):
        if self.is_leaf():
            if self.a[1] > 0:
                return 1
            if self.a[0] > 0:
                return 0
            return None
        max_idx = self.summary.maximum()
        if max_idx is None:
            return None
        offset = self.cluster[max_idx].maximum()
        return self.index(max_idx, offset)

    def predecessor(self, x):
        if self.is_leaf():
            if self.a[0] == 1 and x == 1:
                return 0
            return None
        offset = self.cluster[self.high(x)].predecessor(self.low(x))
        if offset is not None:
            return self.index(self.high(x), offset)
        pred_idx = self.summary.predecessor(self.high(x))
        if pred_idx is None:
            return None
        offset = self.cluster[pred_idx].maximum()
        return self.index(pred_idx, offset)

    def successor(self, x):
        if self.is_leaf():
            if x == 0 and self.a[1] == 1:
                return 1
            return None
        offset = self.cluster[self.high(x)].successor(self.low(x))
        if offset is not None:
            return self.index(self.high(x), offset)
        succ_idx = self.summary.successor(self.high(x))
        if succ_idx is None:
            return None
        offset = self.cluster[succ_idx].minimum()
        return self.index(succ_idx, offset)

    def insert(self, x):
        if self.is_leaf():
            self.a[x] = 1
        else:
            self.summary.insert(self.high(x))
            self.cluster[self.high(x)].insert(self.low(x))

    def display(self, space=0, summary=False):
        if self.is_leaf():
            if summary:
                print(' ' * space + 'S ' + str(self.u) + ' ' + str(self.a))
            else:
                print(' ' * space + 'C ' + str(self.u) + ' ' + str(self.a))
        else:
            if summary:
                print(' ' * space + 'S ' + str(self.u))
            else:
                print(' ' * space + 'C ' + str(self.u))
            self.summary.display(space + 2, True)
            for c in self.cluster:
                c.display(space + 2)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        veb = ProtoVEB(16)
        a = [2, 3, 4, 5, 7, 14, 15]
        self.assertEqual(veb.minimum(), None)
        self.assertEqual(veb.maximum(), None)
        for v in a:
            veb.insert(v)
        self.assertEqual(veb.minimum(), 2)
        self.assertEqual(veb.maximum(), 15)
        for i in xrange(16):
            succ = veb.successor(i)
            expect = None
            for v in a:
                if v > i:
                    expect = v
                    break
            self.assertEqual(succ, expect)
            pred = veb.predecessor(i)
            expect = None
            for v in reversed(a):
                if v < i:
                    expect = v
                    break
            self.assertEqual(pred, expect)

    def test_random(self):
        for _ in xrange(1000):
            veb = ProtoVEB(256)
            a = random.sample(xrange(256), random.randint(1, 256))
            for v in a:
                veb.insert(v)
            a = sorted(a)
            self.assertEqual(veb.minimum(), a[0])
            self.assertEqual(veb.maximum(), a[-1])
            for i in xrange(256):
                succ = veb.successor(i)
                expect = None
                for v in a:
                    if v > i:
                        expect = v
                        break
                self.assertEqual(succ, expect)
                pred = veb.predecessor(i)
                expect = None
                for v in reversed(a):
                    if v < i:
                        expect = v
                        break
                self.assertEqual(pred, expect)


if __name__ == '__main__':
    unittest.main()
