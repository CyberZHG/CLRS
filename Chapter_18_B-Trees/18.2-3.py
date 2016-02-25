import random
import unittest


class BTreeNode:
    def __init__(self, t):
        self.n = 0
        self.key = [None] * (2 * t - 1)
        self.c = [None] * (2 * t)
        self.leaf = True


class BTree:
    def __init__(self, degree):
        self.t = degree
        self.root = BTreeNode(degree)

    def disk_read(self, x):
        pass

    def disk_write(self, x):
        pass

    def split_child(self, x, i):
        t = self.t
        z = BTreeNode(t)
        y = x.c[i]
        z.leaf = y.leaf
        z.n = t - 1
        for j in range(t - 1):
            z.key[j] = y.key[j + t]
        if not y.leaf:
            for j in range(t):
                z.c[j] = y.c[j + t]
        y.n = t - 1
        for j in range(x.n, i - 1, -1):
            x.c[j + 1] = x.c[j]
        x.c[i + 1] = z
        for j in range(x.n - 1, i - 2, -1):
            x.key[j + 1] = x.key[j]
        x.key[i] = y.key[t - 1]
        x.n += 1
        self.disk_write(y)
        self.disk_write(z)
        self.disk_write(x)

    def insert(self, k):
        t = self.t
        r = self.root
        if r.n == 2 * t - 1:
            s = BTreeNode(t)
            self.root = s
            s.leaf = False
            s.n = 0
            s.c[0] = r
            self.split_child(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)

    def insert_nonfull(self, x, k):
        t = self.t
        i = x.n - 1
        if x.leaf:
            while i >= 0 and k < x.key[i]:
                x.key[i + 1] = x.key[i]
                i -= 1
            x.key[i + 1] = k
            x.n += 1
            self.disk_write(x)
        else:
            while i >= 0 and k < x.key[i]:
                i -= 1
            i += 1
            self.disk_read(x.c[i])
            if x.c[i].n == 2 * t - 1:
                self.split_child(x, i)
                if k > x.key[i]:
                    i += 1
            self.insert_nonfull(x.c[i], k)

    def minimum(self):
        def minimum_sub(x):
            if x is None:
                return None
            if x.n > 0 and x.c[0] is not None:
                return minimum_sub(x.c[0])
            return x.key[0]
        if self.root.n == 0:
            return None
        return minimum_sub(self.root)

    def predecessor(self, k):
        def predecessor_sub(x):
            if x is None:
                return None
            for i in xrange(x.n - 1, -1, -1):
                if k > x.key[i]:
                    c = predecessor_sub(x.c[i + 1])
                    if c is None:
                        return x.key[i]
                    return max(c, x.key[i])
            return predecessor_sub(x.c[0])
        if self.root.n == 0:
            return None
        return predecessor_sub(self.root)

    def successor(self, k):
        def successor_sub(x):
            if x is None:
                return None
            for i in xrange(x.n):
                if k < x.key[i]:
                    c = successor_sub(x.c[i])
                    if c is None:
                        return x.key[i]
                    return min(c, x.key[i])
            return successor_sub(x.c[x.n])
        if self.root.n == 0:
            return None
        return successor_sub(self.root)

    def display(self):
        def display_sub(x, space):
            if x is None:
                return
            print(' ' * space + '[' + ' '.join(map(str, x.key[:x.n])) + ']')
            for c in x.c[:x.n + 1]:
                display_sub(c, space + 4)
        display_sub(self.root, 0)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        v = ['F', 'S', 'Q', 'K', 'C', 'L', 'H', 'T', 'V', 'W', 'M', 'R',
             'N', 'P', 'A', 'B', 'X', 'Y', 'D', 'Z', 'E']
        tree = BTree(2)
        self.assertEqual(tree.minimum(), None)
        for c in v:
            tree.insert(c)
        tree.display()
        self.assertEqual(tree.minimum(), 'A')
        v = sorted(v)
        for i in xrange(1, len(v)):
            self.assertEqual(tree.predecessor(v[i]), v[i - 1])
        self.assertEqual(tree.predecessor(v[0]), None)
        for i in xrange(len(v) - 1):
            self.assertEqual(tree.successor(v[i]), v[i + 1])
        self.assertEqual(tree.successor(v[len(v) - 1]), None)

    def test_random(self):
        for _ in xrange(1000):
            v = random.sample(xrange(100000), 1000)
            t = random.randint(2, 5)
            tree = BTree(t)
            for c in v:
                tree.insert(c)
            v = sorted(v)
            self.assertEqual(tree.minimum(), v[0])
            for i in xrange(1, len(v)):
                self.assertEqual(tree.predecessor(v[i]), v[i - 1])
            self.assertEqual(tree.predecessor(v[0]), None)
            for i in xrange(len(v) - 1):
                self.assertEqual(tree.successor(v[i]), v[i + 1])
            self.assertEqual(tree.successor(v[len(v) - 1]), None)


if __name__ == '__main__':
    unittest.main()
