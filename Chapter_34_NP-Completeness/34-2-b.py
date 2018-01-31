import copy
import random
import unittest


def divide_b(nums):
    """
    :param nums: nums[i] means there are nums[i] coins with value 2^i
    """
    n = len(nums)
    nums = copy.copy(nums)
    powers = [2 ** i for i in range(n)]
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    sum_a, sum_b = 0, 0
    i = n - 1
    while i >= 0:
        if nums[i] == 0:
            i -= 1
            continue
        if sum_a == sum_b:
            if nums[i] > 1:
                num = nums[i] // 2
                a[i] += num
                b[i] += num
                sum_a += num * powers[i]
                sum_b = sum_a
                nums[i] %= 2
            else:
                a[i] += 1
                sum_a += powers[i]
                nums[i] -= 1
        else:
            num = min(nums[i], (sum_a - sum_b) // powers[i])
            b[i] += num
            sum_b += num * powers[i]
            nums[i] -= num
    if sum_a == sum_b:
        return a, b
    return None, None


class DivideBTestCase(unittest.TestCase):

    def gen_rand_case(self, bound):
        n = random.randint(1, bound)
        return [random.randint(0, bound) for _ in range(n)]

    def generate_cands(self, nums, path, index):
        n = len(nums)
        if index == n:
            rev = [nums[i] - path[i] for i in range(n)]
            return [(copy.copy(path), rev)]
        cands = []
        for num in range(nums[index] + 1):
            path.append(num)
            cands += self.generate_cands(nums, path, index + 1)
            del path[-1]
        return cands

    def test_random_small(self):
        for _ in range(10000):
            nums = self.gen_rand_case(5)
            n = len(nums)
            a, b = divide_b(nums)
            if a is None:
                cands = self.generate_cands(nums, [], 0)
                for a, b in cands:
                    sum_a, sum_b = 0, 0
                    for i in range(n):
                        sum_a += a[i] * 2 ** i
                        sum_b += b[i] * 2 ** i
                    self.assertNotEqual(sum_a, sum_b, (nums, a, b))
            else:
                sum_a, sum_b = 0, 0
                for i in range(n):
                    self.assertTrue(0 <= a[i] <= nums[i], (nums, a, b))
                    self.assertTrue(0 <= b[i] <= nums[i], (nums, a, b))
                    self.assertEqual(a[i] + b[i], nums[i], (nums, a, b))
                    sum_a += a[i] * 2 ** i
                    sum_b += b[i] * 2 ** i
                self.assertEqual(sum_a, sum_b, (nums, a, b))

    def test_random_large(self):
        for _ in range(1000):
            nums = self.gen_rand_case(1000)
            n = len(nums)
            a, b = divide_b(nums)
            if a is not None:
                sum_a, sum_b = 0, 0
                for i in range(n):
                    self.assertTrue(0 <= a[i] <= nums[i])
                    self.assertTrue(0 <= b[i] <= nums[i])
                    self.assertEqual(a[i] + b[i], nums[i])
                    sum_a += a[i] * 2 ** i
                    sum_b += b[i] * 2 ** i
                self.assertEqual(sum_a, sum_b)


if __name__ == '__main__':
    unittest.main()
