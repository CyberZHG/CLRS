import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.size = 1
        self.left = left
        self.right = right
        if self.left is not None:
            self.size += self.left.size
        if self.right is not None:
            self.size += self.right.size


def os_select(x, i):
    while True:
        if x.left is None:
            r = 1
        else:
            r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            x = x.left
        else:
            x = x.right
            i -= r


def print_tree(root):
    def print_tree_rec(node, space):
        if node is not None:
            print_tree_rec(node.right, space + 2)
            print(' ' * space + str(node.key) + '[' + str(node.size) + ']')
            print_tree_rec(node.left, space + 2)
    print_tree_rec(root, 0)
    print('')


class ProblemTestCase(unittest.TestCase):

    def random_tree(self, a):
        if len(a) == 0:
            return None
        i = random.randint(0, len(a) - 1)
        left, right = None, None
        if i > 0:
            left = self.random_tree(a[:i])
        if i < len(a) - 1:
            right = self.random_tree(a[i+1:])
        return TreeNode(a[i], left, right)

    def test_case(self):
        for _ in range(1000):
            a = sorted(random.sample(range(1000000), 1000))
            root = self.random_tree(a)
            for i in range(len(a)):
                self.assertEqual(os_select(root, i + 1).key, a[i])


if __name__ == '__main__':
    unittest.main()
