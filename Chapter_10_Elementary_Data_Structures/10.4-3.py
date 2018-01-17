import random
import unittest


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(node):
    stack = [node]
    while len(stack) > 0:
        node = stack[-1]
        del stack[-1]
        if node is not None:
            print(node.value)
            stack.append(node.left)
            stack.append(node.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        head = TreeNode(3, TreeNode(1), TreeNode(2))
        print_tree(head)


if __name__ == '__main__':
    unittest.main()
