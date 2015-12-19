import random
import unittest


def binary_search(a, v):
    l, r = 0, len(a)-1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == v:
            return mid
        elif a[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return None


class BinarySearchTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            a = sorted(self.random_array())
            v = random.randint(0, 100)
            ret = binary_search(a, v)
            if ret is None:
                for val in a:
                    self.assertNotEqual(val, v)
            else:
                self.assertEqual(a[ret], v)

if __name__ == '__main__':
    unittest.main()
