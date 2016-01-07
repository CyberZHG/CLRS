import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.size = 1
        self.left = left
        self.right = right
        if left is not None:
            self.size += left.size
        if right is not None:
            self.size += right.size


def os_key_rank(x, k, i=0):
    r = 1
    if x.left is not None:
        r += x.left.size
    if k == x.key:
        return i + r
    if k < x.key:
        return os_key_rank(x.left, k, i)
    if k > x.key:
        return os_key_rank(x.right, k, i + r)


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
                self.assertEqual(os_key_rank(root, a[i]), i + 1)


if __name__ == '__main__':
    unittest.main()
