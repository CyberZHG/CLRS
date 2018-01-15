import random
import unittest


class CountInterval:
    def __init__(self, a):
        k = max(a)
        self.c = [0 for _ in range(k + 1)]
        for v in a:
            self.c[v] += 1
        for i in range(1, k + 1):
            self.c[i] += self.c[i - 1]

    def count(self, a, b):
        if a == 0:
            return self.c[b]
        return self.c[b] - self.c[a - 1]


class CountTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(1000):
            arr = [random.randint(0, 1000) for _ in range(random.randint(1, 1000))]
            c = CountInterval(arr)
            k = max(arr)
            for _ in range(100):
                a = random.randint(0, k)
                b = random.randint(0, k)
                if a > b:
                    continue
                num = c.count(a, b)
                self.assertEqual(num, len(filter(lambda x: a <= x <= b, arr)))


if __name__ == '__main__':
    unittest.main()
