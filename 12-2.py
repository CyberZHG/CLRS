import random
import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RadixTree:
    def __init__(self):
        self.root = None

    def insert(self, a):
        self.root = self.insert_rec(self.root, a, 0)

    def insert_rec(self, root, a, idx):
        if idx == len(a):
            if root is None:
                return TreeNode(a)
            root.val = a
            return root
        if root is None:
            root = TreeNode(None)
        if a[idx] == '0':
            root.left = self.insert_rec(root.left, a, idx+1)
        else:
            root.right = self.insert_rec(root.right, a, idx+1)
        return root

    def sorted(self):
        self.sorted_list = []
        self.sorted_rec(self.root)
        return self.sorted_list

    def sorted_rec(self, root):
        if root is None:
            return
        if root.val is not None:
            self.sorted_list.append(root.val)
        self.sorted_rec(root.left)
        self.sorted_rec(root.right)


def sort_strings(strs):
    radix_tree = RadixTree()
    for s in strs:
        radix_tree.insert(s)
    return radix_tree.sorted()


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        strs = ['1011', '10', '011', '100', '0']
        self.assertEqual(sort_strings(strs), ['0', '011', '10', '100', '1011'])


if __name__ == '__main__':
    unittest.main()
