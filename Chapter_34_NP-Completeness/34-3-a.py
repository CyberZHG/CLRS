import random
import unittest


def graph_coloring_2(graph):
    n = len(graph)
    color = [-1 for _ in range(n)]

    def search(u, c):
        if color[u] != -1:
            return
        color[u] = c
        for v in graph[u]:
            if color[v] == -1:
                if not search(v, 1 - c):
                    return False
            elif color[v] == c:
                return False
        return True

    for u in range(n):
        if color[u] == -1:
            if not search(u, 0):
                return False

    return color


class GraphColoring2TestCase(unittest.TestCase):

    def random_graph(self, bound):
        n = random.randint(1, bound)
        m = random.randint(0, n * n)
        graph = {}
        for i in range(n):
            graph[i] = []
        for i in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u == v or (v in graph[u]):
                continue
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def test_random_small(self):
        for _ in range(10000):
            graph = self.random_graph(10)
            n = len(graph)
            color = graph_coloring_2(graph)
            if color:
                for c in color:
                    self.assertTrue(c == 0 or c == 1, (graph, color))
                for u in range(n):
                    for v in graph[u]:
                        self.assertNotEqual(color[u], color[v], (graph, color))
            else:
                color = [0 for _ in range(n)]
                for i in range(1 << n):
                    for j in range(n):
                        if i & (1 << j):
                            color[j] = 1
                        else:
                            color[j] = 0
                flag = True
                for u in range(n):
                    for v in graph[u]:
                        if color[u] == color[v]:
                            flag = False
                self.assertFalse(flag, (graph, color))

    def test_random_medium(self):
        for _ in range(100):
            graph = self.random_graph(100)
            n = len(graph)
            color = graph_coloring_2(graph)
            if color:
                for c in color:
                    self.assertTrue(c == 0 or c == 1)
                for u in range(n):
                    for v in graph[u]:
                        self.assertNotEqual(color[u], color[v])

    def test_random_large(self):
        for _ in range(5):
            graph = self.random_graph(1000)
            n = len(graph)
            color = graph_coloring_2(graph)
            if color:
                for c in color:
                    self.assertTrue(c == 0 or c == 1)
                for u in range(n):
                    for v in graph[u]:
                        self.assertNotEqual(color[u], color[v])


if __name__ == '__main__':
    unittest.main()
