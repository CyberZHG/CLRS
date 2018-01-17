import random
import unittest


def zero_one_knapsack(v, w, W):
    n = len(v)
    dp = [0] * (W + 1)
    for i in range(n):
        for j in range(W, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[W]


class ProblemTestCase(unittest.TestCase):

    def random_case(self):
        n = random.randint(1, 16)
        v = [random.randint(1, 100) for _ in xrange(n)]
        w = [random.randint(1, 100) for _ in xrange(n)]
        W = random.randint(1, 1000)
        return v, w, W

    def brute_force(self, v, w, W):
        max_val = 0
        n = len(v)
        for i in range(1 << n):
            val = 0
            wei = 0
            for j in range(n):
                if (i & (1 << j)) > 0:
                    val += v[j]
                    wei += w[j]
            if wei <= W:
                max_val = max(max_val, val)
        return max_val

    def test_random(self):
        for _ in xrange(1000):
            v, w, W = self.random_case()
            self.assertEqual(zero_one_knapsack(v, w, W), self.brute_force(v, w, W))


if __name__ == '__main__':
    unittest.main()
