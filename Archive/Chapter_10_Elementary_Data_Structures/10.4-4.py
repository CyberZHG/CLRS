import random
import unittest


class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_sibling = right


def print_tree(node):
    if node is not None:
        while node.parent is not None:
            node = node.parent
        while node is not None:
            print(node.value)
            sibling = node.right_sibling
            while sibling is not None:
                print(sibling.value)
                sibling = sibling.right_sibling
            node = node.left_child


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3)
        head = TreeNode(1, root, None, TreeNode(2))
        root.left_child = head
        print_tree(head)


if __name__ == '__main__':
    unittest.main()
