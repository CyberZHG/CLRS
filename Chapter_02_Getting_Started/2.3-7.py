import random
import unittest


def two_sum(a, x):
    lt, rt = 0, len(a) - 1
    while lt < rt:
        if a[lt] + a[rt] == x:
            return True
        elif a[lt] + a[rt] < x:
            lt += 1
        else:
            rt -= 1
    return False


class BinarySearchTestCase(unittest.TestCase):
    def brute_force(self, a, x):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == x:
                    return True
        return False

    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            a = sorted(self.random_array())
            x = random.randint(0, 200)
            self.assertEqual(two_sum(a, x), self.brute_force(a, x))


if __name__ == '__main__':
    unittest.main()
