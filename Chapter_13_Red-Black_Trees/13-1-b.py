import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insert(root, x):
    if root is None:
        return TreeNode(x)
    new_root = TreeNode(root.key)
    if root.key <= x:
        new_root.left = root.left
        new_root.right = insert(root.right, x)
    else:
        new_root.left = insert(root.left, x)
        new_root.right = root.right
    return new_root


def to_list(node):
    if node is None:
        return []
    return to_list(node.left) + [node.key] + to_list(node.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        t1 = insert(None, 41)
        t2 = insert(t1, 38)
        t3 = insert(t2, 31)
        t4 = insert(t3, 12)
        t5 = insert(t4, 19)
        t6 = insert(t5, 8)
        self.assertEqual(to_list(t1), [41])
        self.assertEqual(to_list(t2), [38, 41])
        self.assertEqual(to_list(t3), [31, 38, 41])
        self.assertEqual(to_list(t4), [12, 31, 38, 41])
        self.assertEqual(to_list(t5), [12, 19, 31, 38, 41])
        self.assertEqual(to_list(t6), [8, 12, 19, 31, 38, 41])


if __name__ == '__main__':
    unittest.main()
