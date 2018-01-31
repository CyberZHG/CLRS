import random
import unittest


def isp_in_deg_2(graph):
    n = len(graph)
    color = [0 for _ in range(n)]

    def search(u):
        if color[u] != 0:
            return
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1:
                color[u] = -1
                break
        for v in graph[u]:
            search(v)

    for u in range(n):
        if len(graph[u]) == 1:
            search(u)
    for u in range(n):
        if color[u] == 0:
            search(u)

    return len(filter(lambda x: x == 1, color))


class IspInDeg2TestCase(unittest.TestCase):

    def random_deg_2_graph(self):
        n = random.randint(0, 16)
        m = random.randint(0, n * 4)
        graph = {}
        for i in range(n):
            graph[i] = []
        for i in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u == v or (v in graph[u]):
                continue
            if len(graph[u]) >= 2 or len(graph[v]) >= 2:
                continue
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def check_isp(self, graph, isp):
        for i in range(len(isp)):
            u = isp[i]
            for j in range(i + 1, len(isp)):
                v = isp[j]
                if v in graph[u]:
                    return False
        return True

    def brute_force(self, graph):
        n = len(graph)
        k = 0
        for i in range(1 << n):
            cand = []
            for j in range(n):
                if i & (1 << j):
                    cand.append(j)
            if self.check_isp(graph, cand):
                k = max(k, len(cand))
        return k

    def test_random(self):
        for _ in range(300):
            graph = self.random_deg_2_graph()
            expect = self.brute_force(graph)
            actual = isp_in_deg_2(graph)
            self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main()
