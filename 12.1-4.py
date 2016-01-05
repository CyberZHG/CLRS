import random
import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_tree_walk(root):
    if root is not None:
        print(root.val)
        preorder_tree_walk(root.left)
        preorder_tree_walk(root.right)


def postorder_tree_walk(root):
    if root is not None:
        postorder_tree_walk(root.left)
        postorder_tree_walk(root.right)
        print(root.val)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        preorder_tree_walk(root)
        postorder_tree_walk(root)


if __name__ == '__main__':
    unittest.main()
