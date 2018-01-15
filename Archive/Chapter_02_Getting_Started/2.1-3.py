import random
import unittest


def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return None


class LinearSearchTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            a = self.random_array()
            v = random.randint(0, 100)
            ret = linear_search(a, v)
            if ret is None:
                for val in a:
                    self.assertNotEqual(val, v)
            else:
                self.assertEqual(a[ret], v)


if __name__ == '__main__':
    unittest.main()
