import random
import unittest


def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -1e100
    sum = 0
    for i in range(mid - 1, low - 1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1e100
    sum = 0
    for j in range(mid, high):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(arr, low, high):
    if low >= high:
        return -1, -1, -1e100
    if low + 1 == high:
        return low, low, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum


class FindMaximumSubarryTestCase(unittest.TestCase):

    def brute_force(self, arr):
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

    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(-100, 100))]

    def test_all_negative(self):
        self.assertEqual(find_maximum_subarray([-2, -1, -3, -4], 0, 4), (1, 1, -1))

    def test_cross(self):
        self.assertEqual(find_maximum_subarray([3, -1, 6, -4], 0, 4), (0, 2, 8))

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            _, _, sub1 = find_maximum_subarray(arr, 0, len(arr))
            _, _, sub2 = self.brute_force(arr)
            self.assertEqual(sub1, sub2)


if __name__ == '__main__':
    unittest.main()
