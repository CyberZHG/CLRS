import random
import unittest


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(node):
    if node is not None:
        print(node.value)
        print_tree(node.left)
        print_tree(node.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        head = TreeNode(3, TreeNode(1), TreeNode(2))
        print_tree(head)


if __name__ == '__main__':
    unittest.main()
