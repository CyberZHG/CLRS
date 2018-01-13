import random
import unittest


class DisjointSetForest:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        self.p[x] = y

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def display(self):
        print('Parent: ' + str(self.p))


def off_line_minimum(q, n):
    pos = [-1] * (n + 1)
    m = 0
    for v in q:
        if v == 'E':
            m += 1
        else:
            pos[v] = im = m
    ds = DisjointSetForest(m + 1)
    extracted = [None] * m
    for i in xrange(1, n + 1):
        j = ds.find_set(pos[i])
        if j < m:
            extracted[j] = i
            ds.link(j, j + 1)
    return extracted


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        q = [4, 8, 'E', 3, 'E', 9, 2, 6, 'E', 'E', 'E', 1, 7, 'E', 5]
        n = 9
        e = off_line_minimum(q, n)
        self.assertEqual(e, [4, 3, 2, 6, 8, 1])

    def test_random(self):
        for _ in xrange(1000):
            n = random.randint(10, 1000)
            q = list(range(1, n + 1))
            random.shuffle(q)
            m = random.randint(10, 1000)
            for _ in xrange(m):
                p = random.randint(0, len(q))
                if p == len(q):
                    q.append('E')
                elif p == 0:
                    q = ['E'] + q
                else:
                    q = q[:p] + ['E'] + q[p:]
            expect = [None] * m
            j = 0
            nums = []
            for v in q:
                if v == 'E':
                    if len(nums) > 0:
                        nums.sort()
                        expect[j] = nums[0]
                        del nums[0]
                    j += 1
                else:
                    nums.append(v)
            self.assertEqual(off_line_minimum(q, n), expect)


if __name__ == '__main__':
    unittest.main()
