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


def tree_minimum(root):
    if root is None:
        return None
    if root.left is None:
        return root
    return tree_minimum(root.left)


def tree_maximum(root):
    if root is None:
        return None
    if root.right is None:
        return root
    return tree_maximum(root.right)


def tree_successor(root):
    if root is None:
        return None
    if root.right is not None:
        return tree_minimum(root.right)
    p = root.parent
    while p is not None and root == p.right:
        root = p
        p = p.parent
    return p


def get_parent(root, node):
    if node is None:
        return None
    a = tree_successor(tree_maximum(node))
    if a is None:
        a = root
    else:
        if a.left == node:
            return a
        a = a.left
    while a is not None and a.right != node:
        a = a.right
    return a


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        self.assertEqual(get_parent(root, root.left.left), root.left)
        self.assertEqual(get_parent(root, root.left), root)
        self.assertEqual(get_parent(root, root.left.right), root.left)
        self.assertEqual(get_parent(root, root), None)
        self.assertEqual(get_parent(root, root.right.left), root.right)
        self.assertEqual(get_parent(root, root.right), root)
        self.assertEqual(get_parent(root, root.right.right), root.right)


if __name__ == '__main__':
    unittest.main()
