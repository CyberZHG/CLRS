import unittest


class TreeNode:
    def __init__(self):
        self.d = 0
        self.p = self
        self.rank = 0


def find_depth(v):
    if v == v.p:
        return (v.d, v)
    (pd, p) = find_depth(v.p)
    d = v.d + pd
    v.d = d - p.d
    v.p = p
    return (d, p)


def graft(r, v):
    (vd, vp) = find_depth(v)
    if r.rank <= vp.rank:
        r.d = vd + 1
        r.p = vp
        if r.rank == vp.rank:
            vp.rank += 1
    else:
        r.d = vd + 1
        vp.d = vp.d - r.d
        vp.p = r


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        nodes = [TreeNode() for _ in xrange(6)]
        graft(nodes[0], nodes[1])
        self.assertEqual(find_depth(nodes[0]), (1, nodes[1]))
        self.assertEqual(find_depth(nodes[1]), (0, nodes[1]))
        graft(nodes[2], nodes[3])
        self.assertEqual(nodes[2].rank, 0)
        self.assertEqual(nodes[3].rank, 1)
        graft(nodes[1], nodes[3])
        self.assertEqual(find_depth(nodes[0]), (2, nodes[3]))
        self.assertEqual(find_depth(nodes[1]), (1, nodes[3]))
        self.assertEqual(find_depth(nodes[2]), (1, nodes[3]))
        self.assertEqual(find_depth(nodes[3]), (0, nodes[3]))
        self.assertEqual(nodes[3].rank, 2)
        graft(nodes[4], nodes[5])
        graft(nodes[3], nodes[4])
        self.assertEqual(find_depth(nodes[0]), (4, nodes[3]))
        self.assertEqual(find_depth(nodes[1]), (3, nodes[3]))
        self.assertEqual(find_depth(nodes[2]), (3, nodes[3]))
        self.assertEqual(find_depth(nodes[3]), (2, nodes[3]))
        self.assertEqual(find_depth(nodes[4]), (1, nodes[3]))
        self.assertEqual(find_depth(nodes[5]), (0, nodes[3]))
        self.assertEqual(nodes[3].rank, 2)
        self.assertEqual(nodes[5].rank, 1)


if __name__ == '__main__':
    unittest.main()
