import random
import unittest


def merge_sort_sub(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort_sub(arr, l, mid)
    merge_sort_sub(arr, mid+1, r)
    arr_l = [arr[i] for i in range(l, mid+1)]
    arr_r = [arr[j] for j in range(mid+1, r+1)]
    i, j = 0, 0
    for k in range(l, r+1):
        if j == len(arr_r) or (i != len(arr_l) and arr_l[i] <= arr_r[j]):
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1


def merge_sort(arr):
    merge_sort_sub(arr, 0, len(arr) - 1)


class MergeSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            merge_sort(arr)
            self.assertEqual(arr, sorted_arr)

if __name__ == '__main__':
    unittest.main()
