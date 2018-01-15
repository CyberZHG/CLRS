import random
import unittest


def k_sort(a, k):
    for i in range(k):
        a[i:len(a):k] = sorted(a[i:len(a):k])


class KSortCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 1000) for _ in range(random.randint(1, 1000))]
            k = random.randint(1, len(a))
            k_sort(a, k)
            for i in range(len(a) - k):
                self.assertTrue(a[i] <= a[i + k])


if __name__ == '__main__':
    unittest.main()
