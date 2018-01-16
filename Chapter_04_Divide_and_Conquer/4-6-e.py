import unittest


def get_min_index(arr):
    def get_min_index_rec(idx):
        if len(idx) == 1:
            min_idx = 0
            for j in range(1, len(arr[0])):
                if arr[idx[0]][j] < arr[idx[0]][min_idx]:
                    min_idx = j
            return [min_idx]
        sub_idx = [idx[i] for i in range(len(idx)) if i % 2 == 0]
        sub_min_idx = get_min_index_rec(sub_idx)
        sub_min_idx.append(len(arr[0]) - 1)
        min_idx = [sub_min_idx[i//2] for i in range(len(idx))]
        for i in range(1, len(idx), 2):
            for j in range(sub_min_idx[i//2] + 1, sub_min_idx[i//2 + 1] + 1):
                if arr[idx[i]][j] < arr[idx[i]][min_idx[i]]:
                    min_idx[i] = j
        return min_idx
    return get_min_index_rec([i for i in range(len(arr))])


class MongeArrayTestCase(unittest.TestCase):
    def test_example_1(self):
        arr = [[10, 17, 13, 28, 23],
               [17, 22, 16, 29, 23],
               [24, 28, 22, 34, 24],
               [11, 13, 6, 17, 7],
               [45, 44, 32, 37, 23],
               [36, 33, 19, 21, 6],
               [75, 66, 51, 53, 34]]
        self.assertEqual(get_min_index(arr), [0, 2, 2, 2, 4, 4, 4])

    def test_example_2(self):
        arr = [[37, 23, 24, 32],
               [21, 6, 7, 10],
               [53, 34, 30, 31],
               [32, 13, 9, 6],
               [43, 21, 15, 8]]
        self.assertEqual(get_min_index(arr), [1, 1, 2, 3, 3])


if __name__ == '__main__':
    unittest.main()
