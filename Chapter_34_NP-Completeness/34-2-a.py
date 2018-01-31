import random
import unittest


def divide_a(nx, x, ny, y):
    s = nx * x + ny * y
    if s % 2 == 1:
        return -1, -1
    s //= 2

    def ext_gcd(x, y):
        if y == 0:
            return x, 1, 0
        g, b, a = ext_gcd(y, x % y)
        return g, a, b - (x // y) * a

    g, a, b = ext_gcd(x, y)
    if s % g != 0:
        return -1, -1
    x, y, s = x // g, y // g, s // g
    a, b = a * s, b * s
    lx, rx = (-a + (y - 1)) // y, (nx - a) // y
    ly, ry = (b - ny + (x - 1)) // x, b // x
    if max(lx, ly) > min(rx, ry):
        return -1, -1
    t = max(lx, ly)
    return a + y * t, b - x * t


class DivideATestCase(unittest.TestCase):

    def gen_rand_case(self, bound):
        nx = random.randint(0, bound)
        ny = random.randint(0, bound)
        x = random.randint(1, bound)
        y = random.randint(1, bound)
        return nx, x, ny, y

    def test_random_small(self):
        for _ in range(100000):
            nx, x, ny, y = self.gen_rand_case(20)
            a, b = divide_a(nx, x, ny, y)
            if a == -1 and b == -1:
                for a in range(nx + 1):
                    for b in range(ny + 1):
                        self.assertNotEqual(
                            a * x + b * y,
                            (nx - a) * x + (ny - b) * y,
                            (nx, x, ny, y, a, b)
                        )
            else:
                self.assertTrue(0 <= a <= nx, (nx, a))
                self.assertTrue(0 <= b <= ny, (ny, b))
                self.assertEqual(
                    a * x + b * y,
                    (nx - a) * x + (ny - b) * y,
                    (nx, x, ny, y)
                )

    def test_random_large(self):
        for _ in range(100000):
            nx, x, ny, y = self.gen_rand_case(10000000000000000000000000000000)
            a, b = divide_a(nx, x, ny, y)
            if a != -1:
                self.assertTrue(0 <= a <= nx)
                self.assertTrue(0 <= b <= ny)
                self.assertEqual(a * x + b * y, (nx - a) * x + (ny - b) * y)


if __name__ == '__main__':
    unittest.main()
