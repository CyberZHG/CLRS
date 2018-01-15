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


def insert(root, x):
    if root is None:
        return TreeNode(x)
    if root.val > x:
        root.left = insert(root.left, x)
        root.left.parent = root
    elif root.val < x:
        root.right = insert(root.right, x)
        root.right.parent = root
    return root


def to_list(root):
    if root is None:
        return []
    return to_list(root.left) + [root.val] + to_list(root.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = insert(None, 3)
        root = insert(root, 1)
        root = insert(root, 5)
        root = insert(root, 0)
        root = insert(root, 2)
        root = insert(root, 4)
        root = insert(root, 6)
        self.assertEqual(to_list(root), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
