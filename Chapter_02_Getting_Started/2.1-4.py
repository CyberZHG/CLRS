import unittest


def add_binary(a, b):
    n = len(a)
    c = [0 for _ in range(n + 1)]
    carry = 0
    for i in range(n):
        c[i] = a[i] + b[i] + carry
        if c[i] > 1:
            c[i] -= 2
            carry = 1
        else:
            carry = 0
    c[n] = carry
    return c


class AddBinaryTestCase(unittest.TestCase):
    def test_carry(self):
        a = [1, 0, 1]
        b = [1, 1, 1]
        self.assertEqual(add_binary(a, b), [0, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()
