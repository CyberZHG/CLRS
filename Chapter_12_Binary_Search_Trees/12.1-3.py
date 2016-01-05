import random
import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_tree_walk(root):
    stack = []
    while len(stack) > 0 or root is not None:
        if root is None:
            root = stack[-1]
            del stack[-1]
            print(root.val)
            root = root.right
        else:
            stack.append(root)
            root = root.left


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        inorder_tree_walk(root)


if __name__ == '__main__':
    unittest.main()
