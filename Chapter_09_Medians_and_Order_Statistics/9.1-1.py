import random
import unittest


def find_second_smallest(a, lt, rt):
    if lt + 1 == rt:
        return a[lt], []
    mid = (lt + rt + 1) // 2
    min_l, lst_l = find_second_smallest(a, lt, mid)
    min_r, lst_r = find_second_smallest(a, mid, rt)
    if min_l <= min_r:
        min_val, lst = min_l, lst_l + [min_r]
    else:
        min_val, lst = min_r, lst_r + [min_l]
    if lt == 0 and rt == len(a):
        idx = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[idx]:
                idx = i
        return lst[idx]
    return min_val, lst


class SecondSmallestTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            a = [random.randint(1, 1000000) for _ in range(random.randint(2, 5))]
            b = sorted(a)
            self.assertTrue(find_second_smallest(a, 0, len(a)), b[1])
        for _ in range(1000):
            a = [random.randint(1, 1000000) for _ in range(random.randint(2, 10000))]
            b = sorted(a)
            self.assertTrue(find_second_smallest(a, 0, len(a)), b[1])


if __name__ == '__main__':
    unittest.main()
