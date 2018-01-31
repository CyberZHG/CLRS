import random
import unittest
import itertools


def schedule(t, p, d):
    k, n = 0, len(t)
    d, p, t = tuple(zip(*sorted(zip(d, p, t))))
    dp = [[0 for _ in range(n * n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n * n, 0, -1):
            dp[i][j] = dp[i - 1][j]
            if j - t[i - 1] >= 0:
                if j <= d[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]] + p[i - 1])
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]])
            k = max(k, dp[i][j])
    return k


class ScheduleTestCase(unittest.TestCase):

    def brute_force(self, t, p, d):
        k, n = 0, len(t)
        for s in itertools.permutations(list(range(n))):
            profits, time = 0, 0
            for i in s:
                if time + t[i] <= d[i]:
                    profits += p[i]
                time += t[i]
            k = max(k, profits)
        return k

    def test_random(self):
        for _ in range(10000):
            n = random.randint(1, 7)
            t = [random.randint(1, n) for _ in range(n)]
            p = [random.randint(0, 10000) for _ in range(n)]
            d = [random.randint(0, n * n) for _ in range(n)]
            actual = schedule(t, p, d)
            expect = self.brute_force(t, p, d)
            self.assertEqual(actual, expect, (actual, expect, t, p, d))


if __name__ == '__main__':
    unittest.main()
