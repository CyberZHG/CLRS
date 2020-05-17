import random
import unittest


class VanEmdeBoasTree:
    def __init__(self, u):
        self.u = u
        temp = u
        bit_num = -1
        while temp > 0:
            temp >>= 1
            bit_num += 1
        self.sqrt_h = 1 << ((bit_num + 1) // 2)
        self.sqrt_l = 1 << (bit_num // 2)
        self.min = None
        self.max = None
        self.summary = None
        self.cluster = [None] * self.sqrt_h

    def is_leaf(self):
        return self.u == 2

    def high(self, x):
        return x // self.sqrt_l

    def low(self, x):
        return x % self.sqrt_l

    def index(self, x, y):
        return x * self.sqrt_l + y

    def minimum(self):
        return self.min

    def maximum(self):
        return self.max

    def get_cluster(self, x):
        if self.cluster[x] is None:
            self.cluster[x] = VanEmdeBoasTree(self.sqrt_l)
        return self.cluster[x]

    def get_summary(self):
        if self.summary is None:
            self.summary = VanEmdeBoasTree(self.sqrt_h)
        return self.summary

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        if self.is_leaf():
            return False
        return self.member(self.get_cluster(self.high(x)), self.low(x))

    def successor(self, x):
        if self.is_leaf():
            if x == 0 and self.max == 1:
                return 1
            return None
        if self.min is not None and x < self.min:
            return self.min
        max_low = self.get_cluster(self.high(x)).maximum()
        if max_low is not None and self.low(x) < max_low:
            offset = self.get_cluster(self.high(x)).successor(self.low(x))
            return self.index(self.high(x), offset)
        succ_cluster = self.get_summary().successor(self.high(x))
        if succ_cluster is None:
            return None
        offset = self.cluster[succ_cluster].minimum()
        return self.index(succ_cluster, offset)

    def predecessor(self, x):
        if self.is_leaf():
            if x == 1 and self.min == 0:
                return 0
            return None
        if self.max is not None and x > self.max:
            return self.max
        min_low = self.get_cluster(self.high(x)).minimum()
        if min_low is not None and self.low(x) > min_low:
            offset = self.get_cluster(self.high(x)).predecessor(self.low(x))
            return self.index(self.high(x), offset)
        pred_cluster = self.get_summary().predecessor(self.high(x))
        if pred_cluster is None:
            if self.min is not None and x > self.min:
                return self.min
            return None
        offset = self.cluster[pred_cluster].maximum()
        return self.index(pred_cluster, offset)

    def insert_empty(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min is None:
            self.insert_empty(x)
        else:
            if x < self.min:
                x, self.min = self.min, x
            if not self.is_leaf():
                if self.get_cluster(self.high(x)).minimum() is None:
                    self.get_summary().insert(self.high(x))
                    self.get_cluster(self.high(x)).insert_empty(self.low(x))
                else:
                    self.get_cluster(self.high(x)).insert(self.low(x))
            if x > self.max:
                self.max = x

    def delete(self, x):
        if self.min == self.max:
            self.min = self.max = None
        elif self.is_leaf():
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.get_summary().minimum()
                x = self.index(first_cluster,
                               self.cluster[first_cluster].minimum())
                self.min = x
            self.get_cluster(self.high(x)).delete(self.low(x))
            if self.get_cluster(self.high(x)).minimum() is None:
                self.get_summary().delete(self.high(x))
                if x == self.max:
                    sum_max = self.get_summary().maximum()
                    if sum_max is None:
                        self.max = self.min
                    else:
                        self.max = self.index(sum_max,
                                              self.cluster[sum_max].maximum())
            elif x == self.max:
                self.max = self.index(self.high(x),
                                      self.get_cluster(self.high(x)).maximum())


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        veb = VanEmdeBoasTree(16)
        a = [2, 3, 4, 5, 7, 14, 15]
        self.assertEqual(veb.minimum(), None)
        self.assertEqual(veb.maximum(), None)
        for v in a:
            veb.insert(v)
        self.assertEqual(veb.minimum(), 2)
        self.assertEqual(veb.maximum(), 15)
        for i in range(16):
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
        for _ in range(1000):
            veb = VanEmdeBoasTree(256)
            a = random.sample(range(256), random.randint(2, 256))
            b = random.sample(a, random.randint(1, len(a) - 1))
            for v in a:
                veb.insert(v)
            for v in b:
                veb.delete(v)
            c = []
            for i in range(256):
                if i in a and i not in b:
                    c.append(i)
            self.assertEqual(veb.minimum(), c[0])
            self.assertEqual(veb.maximum(), c[-1])
            for i in range(256):
                succ = veb.successor(i)
                expect = None
                for v in c:
                    if v > i:
                        expect = v
                        break
                self.assertEqual(succ, expect)
                pred = veb.predecessor(i)
                expect = None
                for v in reversed(c):
                    if v < i:
                        expect = v
                        break
                self.assertEqual(pred, expect)


if __name__ == '__main__':
    unittest.main()
