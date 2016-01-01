import random
import unittest


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.parent = None
        self.left = left
        self.right = right
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self


def print_tree(node):
    prev = None
    while node is not None:
        if node.parent == prev:
            print(node.value)
            prev = node
            if node.left is None:
                node = node.parent
            else:
                node = node.left
        elif node.left == prev:
            prev = node
            if node.right is None:
                node = node.parent
            else:
                node = node.right
        else:
            prev = node
            node = node.parent


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(1,
                        TreeNode(2, TreeNode(3), TreeNode(4)),
                        TreeNode(5, TreeNode(6), TreeNode(7)))
        print_tree(root)


if __name__ == '__main__':
    unittest.main()
