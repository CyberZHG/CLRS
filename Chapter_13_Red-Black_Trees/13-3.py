import random
import unittest


class AVLTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.h = 0
        self.p = None
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.p = self
        if self.right is not None:
            self.right.p = self


class AVL:
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

    def get_height(self, node):
        if node is None:
            return -1
        return node.h

    def update_height(self, node):
        if node is None:
            return
        node.h = max(self.get_height(node.left), self.get_height(node.right))+1

    def balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def avl_insert(self, x):
        self.root = self.avl_insert_rec(self.root, x)

    def avl_insert_rec(self, root, x):
        if root is None:
            return AVLTreeNode(x)
        if root.key > x:
            root.left = self.avl_insert_rec(root.left, x)
            root.left.p = root
        else:
            root.right = self.avl_insert_rec(root.right, x)
            root.right.p = root
        if self.balance_factor(root) == 2:
            if self.balance_factor(root.left) == -1:
                self.left_rotate(root.left)
            self.right_rotate(root)
            root = root.p
            self.update_height(root.left)
            self.update_height(root.right)
            self.update_height(root)
        elif self.balance_factor(root) == -2:
            if self.balance_factor(root.right) == 1:
                self.right_rotate(root.right)
            self.left_rotate(root)
            root = root.p
            self.update_height(root.left)
            self.update_height(root.right)
            self.update_height(root)
        else:
            self.update_height(root)
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
                print(' ' * space + str(node.key) + '[' + str(node.h) + ']')
                print_tree_rec(node.left, space + 2)
        print_tree_rec(self.root, 0)
        print('')


class ProblemTestCase(unittest.TestCase):

    def check_avl_rec(self, T, node):
        if node is None:
            return
        diff = abs(T.get_height(node.left) - T.get_height(node.right))
        self.assertTrue(diff <= 1)
        self.check_avl_rec(T, node.left)
        self.check_avl_rec(T, node.right)

    def check_avl(self, T):
        self.check_avl_rec(T, T.root)

    def test_case(self):
        T = AVL()
        T.avl_insert(41)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [41])
        T.avl_insert(38)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [38, 41])
        T.avl_insert(31)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [31, 38, 41])
        T.avl_insert(12)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [12, 31, 38, 41])
        T.avl_insert(19)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [12, 19, 31, 38, 41])
        T.avl_insert(8)
        self.check_avl(T)
        self.assertEqual(T.to_list(), [8, 12, 19, 31, 38, 41])

    def test_random(self):
        for _ in xrange(1000):
            T = AVL()
            a = random.sample(xrange(100000000), 1000)
            for v in a:
                T.avl_insert(v)
            self.check_avl(T)
            self.assertEqual(T.to_list(), sorted(a))


if __name__ == '__main__':
    unittest.main()
