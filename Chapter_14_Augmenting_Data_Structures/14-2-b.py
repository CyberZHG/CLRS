import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.size = 1
        self.p = None
        self.left = left
        self.right = right
        if left is not None:
            left.p = self
            self.size += left.size
        if right is not None:
            right.p = self
            self.size += right.size


class BinarySearchTree:
    def __init__(self, a):
        self.root = self.build(a, 0, len(a))

    def build(self, a, lt, rt):
        if lt >= rt:
            return None
        mid = (lt + rt) // 2
        return TreeNode(a[mid], self.build(a, lt, mid), self.build(a, mid + 1, rt))

    def get_size(self, x):
        if x is None:
            return 0
        return x.size

    def update_size(self, x):
        if x is not None:
            x.size = 1 + self.get_size(x.left) + self.get_size(x.right)

    def select(self, x, i):
        r = self.get_size(x.left) + 1
        if i == r:
            return x
        elif i < r:
            return self.select(x.left, i)
        else:
            return self.select(x.right, i - r)

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            p = y.p
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            while p != z and p != y:
                self.update_size(p)
                p = p.p
            self.update_size(y)
        while z.p is not None:
            z = z.p
            self.update_size(z)


def josephus_permutation(n, m):
    tree = BinarySearchTree(range(1, n + 1))
    perm = []
    rank = 0
    while n > 0:
        rank = (rank + m - 1) % n
        x = tree.select(tree.root, rank + 1)
        perm.append(x.key)
        tree.delete(x)
        n -= 1
    return perm


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        a = josephus_permutation(7, 3)
        self.assertEqual(a, [3, 6, 2, 7, 5, 1, 4])

    def test_random(self):
        for _ in xrange(1000):
            n = random.randint(1, 1000)
            m = random.randint(1, 1000)
            p = josephus_permutation(n, m)
            a = [i for i in xrange(1, n + 1)]
            b = []
            idx = 0
            while len(a) > 0:
                idx = (idx + m - 1) % len(a)
                b.append(a[idx])
                del a[idx]
            self.assertEqual(p, b)


if __name__ == '__main__':
    unittest.main()
