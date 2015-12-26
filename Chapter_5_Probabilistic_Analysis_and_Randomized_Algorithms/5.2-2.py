import unittest
import random


def random_interval(a, b):
    while a < b:
        if random.randint(0, 1) == 0:
            b = (a + b) // 2
        else:
            a = (a + b) // 2 + 1
    return a


class RandomTestCase(unittest.TestCase):
    def test_random(self):
        for _ in range(10000):
            a = random.randint(0, 1000)
            b = a + random.randint(0, 1000)
            r = random_interval(a, b)
            self.assertTrue(a <= r <= b)


if __name__ == '__main__':
    unittest.main()
