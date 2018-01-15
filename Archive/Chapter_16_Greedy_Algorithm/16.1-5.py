import random
import unittest


def activity_selection(s, f, v):
    dp = {}
    n = len(s)
    last = None
    for i in sorted(list(set(s + f))):
        if last is None:
            dp[i] = 0
        else:
            dp[i] = last
            for j in range(n):
                if f[j] <= i:
                    dp[i] = max(dp[i], dp[s[j]] + v[j])
        last = dp[i]
    return last


class ProblemTestCase(unittest.TestCase):

    def random_activity(self):
        n = random.randint(1, 16)
        s = [random.randint(1, 100) for _ in xrange(n)]
        f = [s[i] + random.randint(1, 100) for i in xrange(n)]
        v = [random.randint(1, 100) for _ in xrange(n)]
        return s, f, v

    def brute_force(self, s, f, v):
        max_val = 0
        n = len(s)
        for i in range(1 << n):
            flag = True
            for j in range(n):
                if (i & (1 << j)) > 0:
                    for k in range(j + 1, n):
                        if (i & (1 << k)) > 0:
                            if s[j] >= s[k] and s[j] < f[k]:
                                flag = False
                                break
                            if s[k] >= s[j] and s[k] < f[j]:
                                flag = False
                                break
            if flag:
                val = 0
                for j in range(n):
                    if (i & (1 << j)) > 0:
                        val += v[j]
                max_val = max(max_val, val)
        return max_val

    def test_random(self):
        for _ in xrange(1000):
            s, f, v = self.random_activity()
            self.assertEqual(activity_selection(s, f, v), self.brute_force(s, f, v))


if __name__ == '__main__':
    unittest.main()
