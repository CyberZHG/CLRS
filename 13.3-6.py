import random
import unittest


RED = 0
BLACK = 1


class Stack:
    def __init__(self):
        self.vals = []

    def push(self, x):
        self.vals.append(x)

    def pop(self):
        if len(self.vals) == 0:
            return None
        x = self.vals[-1]
        del self.vals[-1]
        return x


class RedBlackTreeNode:
    def __init__(self, key, left=None, right=None):
        self.color = BLACK
        self.key = key
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackTreeNode(None)
        self.nil.color = BLACK
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil


def left_rotate(T, x, p):
    y = x.right
    x.right = y.left
    if p == T.nil:
        T.root = y
    elif x == p.left:
        p.left = y
    else:
        p.right = y
    y.left = x


def right_rotate(T, x, p):
    y = x.left
    x.left = y.right
    if p == T.nil:
        T.root = y
    elif x == p.right:
        p.right = y
    else:
        p.left = y
    y.right = x


def rb_insert_fixup(T, z, stack):
    while True:
        p = stack.pop()
        if p.color == BLACK:
            break
        pp = stack.pop()
        if p == pp.left:
            y = pp.right
            if y.color == RED:
                p.color = BLACK
                y.color = BLACK
                pp.color = RED
                z = pp
            elif z == p.right:
                stack.push(pp)
                stack.push(z)
                z = p
                left_rotate(T, z, pp)
            else:
                ppp = stack.pop()
                stack.push(p)
                p.color = BLACK
                pp.color = RED
                right_rotate(T, pp, ppp)
        else:
            y = pp.left
            if y.color == RED:
                p.color = BLACK
                y.color = BLACK
                pp.color = RED
                z = pp
            elif z == p.left:
                stack.push(pp)
                stack.push(z)
                z = p
                right_rotate(T, z, pp)
            else:
                ppp = stack.pop()
                stack.push(p)
                p.color = BLACK
                pp.color = RED
                left_rotate(T, pp, ppp)
    T.root.color = BLACK


def rb_insert(T, z):
    stack = Stack()
    stack.push(T.nil)
    y = T.nil
    x = T.root
    while x != T.nil:
        stack.push(x)
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = RED
    rb_insert_fixup(T, z, stack)


def rb_to_list(T):
    def to_list_sub(node):
        if node.key is None:
            return []
        return to_list_sub(node.left) + [node.key] + to_list_sub(node.right)
    return to_list_sub(T.root)


def print_rb(T):
    def print_rb_sub(node, space):
        if node != T.nil:
            print_rb_sub(node.right, space + 2)
            print(' ' * space + '[' + str(node.color) + '] ' + str(node.key))
            print_rb_sub(node.left, space + 2)
    print_rb_sub(T.root, 0)


class ProblemTestCase(unittest.TestCase):

    def check_rb_rec(self, T, node, height):
        if node == T.nil:
            if self.height == -1:
                self.height = height
            else:
                self.assertEqual(height, self.height)
            return
        if node.color == RED:
            self.assertEqual(node.left.color, BLACK)
            self.assertEqual(node.right.color, BLACK)
        else:
            height += 1
        self.check_rb_rec(T, node.left, height)
        self.check_rb_rec(T, node.right, height)

    def check_rb(self, T):
        self.assertEqual(T.root.color, BLACK)
        self.height = -1
        self.check_rb_rec(T, T.root, 0)

    def test_case(self):
        T = RedBlackTree()
        rb_insert(T, RedBlackTreeNode(41))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [41])
        rb_insert(T, RedBlackTreeNode(38))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [38, 41])
        rb_insert(T, RedBlackTreeNode(31))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [31, 38, 41])
        rb_insert(T, RedBlackTreeNode(12))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [12, 31, 38, 41])
        rb_insert(T, RedBlackTreeNode(19))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [12, 19, 31, 38, 41])
        rb_insert(T, RedBlackTreeNode(8))
        self.check_rb(T)
        self.assertEqual(rb_to_list(T), [8, 12, 19, 31, 38, 41])

    def test_random(self):
        for _ in xrange(1000):
            T = RedBlackTree()
            a = random.sample(xrange(10000000), 1000)
            for v in a:
                rb_insert(T, RedBlackTreeNode(v))
            self.check_rb(T)
            self.assertEqual(rb_to_list(T), sorted(a))


if __name__ == '__main__':
    unittest.main()
