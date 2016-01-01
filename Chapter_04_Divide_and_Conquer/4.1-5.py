import random
import unittest


def find_maximum_subarray(arr):
    max_sum = -1e100
    max_left, max_right = -1, -1
    sum = 0
    last_left = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            max_left = last_left
            max_right = i
        if sum < 0:
            sum = 0
            last_left = i + 1
    return max_left, max_right, max_sum


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
        self.assertEqual(find_maximum_subarray([-2, -1, -3, -4]), (1, 1, -1))

    def test_cross(self):
        self.assertEqual(find_maximum_subarray([3, -1, 6, -4]), (0, 2, 8))

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            _, _, sub1 = find_maximum_subarray(arr)
            _, _, sub2 = self.brute_force(arr)
            self.assertEqual(sub1, sub2)


if __name__ == '__main__':
    unittest.main()
