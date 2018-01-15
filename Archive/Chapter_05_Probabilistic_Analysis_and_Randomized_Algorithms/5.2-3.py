import unittest
import random


def biased_random():
    if random.random() < 0.1:
        return 0
    return 1


def unbiased_random():
    while True:
        a = biased_random()
        b = biased_random()
        if a != b:
            return a


class UnbiasedRandomTestCase(unittest.TestCase):
    def test_random(self):
        cnt_0 = 0
        for _ in range(100000):
            if unbiased_random() == 0:
                cnt_0 += 1
        self.assertTrue(49000 <= cnt_0 <= 51000)


if __name__ == '__main__':
    unittest.main()
