import random
import unittest


def count_inversion_sub(arr, lt, rt):
    if lt >= rt:
        return 0
    mid = (lt + rt) // 2
    cnt = count_inversion_sub(arr, lt, mid) + count_inversion_sub(arr, mid + 1, rt)
    arr_l = [arr[i] for i in range(lt, mid + 1)]
    arr_l.append(1e100)
    arr_r = [arr[j] for j in range(mid + 1, rt + 1)]
    arr_r.append(1e100)
    i, j = 0, 0
    for k in range(lt, rt + 1):
        if arr_l[i] <= arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
            cnt += len(arr_l) - i - 1
    return cnt


def count_inversion(arr):
    return count_inversion_sub(arr, 0, len(arr) - 1)


class CountInversionTestCase(unittest.TestCase):
    def brute_force(self, arr):
        cnt = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    cnt += 1
        return cnt

    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_empty(self):
        self.assertEqual(count_inversion([]), 0)

    def test_no_inversion(self):
        self.assertEqual(count_inversion([1, 2, 3, 4, 5]), 0)

    def test_all_inversion(self):
        self.assertEqual(count_inversion([5, 4, 3, 2, 1]), 10)

    def test_example(self):
        self.assertEqual(count_inversion([2, 3, 8, 6, 1]), 5)

    def test_equal(self):
        self.assertEqual(count_inversion([2, 4, 3, 3, 4, 2]), 6)

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            cnt = self.brute_force(arr)
            self.assertEqual(count_inversion(arr), cnt)


if __name__ == '__main__':
    unittest.main()
