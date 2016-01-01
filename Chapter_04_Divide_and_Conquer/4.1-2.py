import unittest


def find_maximum_subarray(arr):
    sums = [0]
    for a in arr:
        sums.append(sums[-1] + a)
    max_sum = -1e100
    left_index = -1
    right_index = -1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sums[j + 1] - sums[i] > max_sum:
                max_sum = sums[j + 1] - sums[i]
                left_index = i
                right_index = j
    return left_index, right_index, max_sum


class FindMaximumSubarryTestCase(unittest.TestCase):

    def test_all_negative(self):
        self.assertEqual(find_maximum_subarray([-2, -1, -3, -4]), (1, 1, -1))

    def test_cross(self):
        self.assertEqual(find_maximum_subarray([3, -1, 6, -4]), (0, 2, 8))


if __name__ == '__main__':
    unittest.main()
