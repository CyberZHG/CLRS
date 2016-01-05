import random
import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.parent = None
        self.left = left
        self.right = right
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self


def tree_maximum(root):
    if root is None:
        return None
    if root.right is None:
        return root
    return tree_maximum(root.right)


def tree_predecessor(root):
    if root is None:
        return None
    if root.left is not None:
        return tree_maximum(root.left)
    p = root.parent
    while p is not None and root == p.left:
        root = p
        p = p.parent
    return p


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        self.assertEqual(tree_predecessor(root.left.left), None)
        self.assertEqual(tree_predecessor(root.left), root.left.left)
        self.assertEqual(tree_predecessor(root.left.right), root.left)
        self.assertEqual(tree_predecessor(root), root.left.right)
        self.assertEqual(tree_predecessor(root.right.left), root)
        self.assertEqual(tree_predecessor(root.right), root.right.left)
        self.assertEqual(tree_predecessor(root.right.right), root.right)


if __name__ == '__main__':
    unittest.main()
