import random
import unittest


class TreapNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.priority = random.random()
        self.p = None
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.p = self
        if self.right is not None:
            self.right.p = self


class Treap:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y

    def insert(self, x):
        self.root = self.insert_rec(self.root, x)

    def insert_rec(self, root, x):
        if root is None:
            return TreapNode(x)
        if root.key > x:
            root.left = self.insert_rec(root.left, x)
            root.left.p = root
            if root.left.priority < root.priority:
                self.right_rotate(root)
                root = root.p
        else:
            root.right = self.insert_rec(root.right, x)
            root.right.p = root
            if root.right.priority < root.priority:
                self.left_rotate(root)
                root = root.p
        return root

    def to_list(self):
        def to_list_rec(node):
            if node is None:
                return []
            return to_list_rec(node.left)+[node.key]+to_list_rec(node.right)
        return to_list_rec(self.root)

    def print_tree(self):
        def print_tree_rec(node, space):
            if node is not None:
                print_tree_rec(node.right, space + 2)
                print(' ' * space + str(node.key) +
                      '[' + str(node.priority) + ']')
                print_tree_rec(node.left, space + 2)
        print_tree_rec(self.root, 0)
        print('')


class ProblemTestCase(unittest.TestCase):

    def check_treap_rec(self, T, node, priority):
        if node is None:
            return
        self.assertTrue(node.priority >= priority)
        self.check_treap_rec(T, node.left, node.priority)
        self.check_treap_rec(T, node.right, node.priority)

    def check_trep(self, T):
        self.check_treap_rec(T, T.root, 0.0)

    def test_case(self):
        T = Treap()
        T.insert(41)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [41])
        T.insert(38)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [38, 41])
        T.insert(31)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [31, 38, 41])
        T.insert(12)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [12, 31, 38, 41])
        T.insert(19)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [12, 19, 31, 38, 41])
        T.insert(8)
        self.check_trep(T)
        self.assertEqual(T.to_list(), [8, 12, 19, 31, 38, 41])

    def test_random(self):
        for _ in xrange(1000):
            T = Treap()
            a = random.sample(xrange(100000000), 1000)
            for v in a:
                T.insert(v)
            self.check_trep(T)
            self.assertEqual(T.to_list(), sorted(a))


if __name__ == '__main__':
    unittest.main()
