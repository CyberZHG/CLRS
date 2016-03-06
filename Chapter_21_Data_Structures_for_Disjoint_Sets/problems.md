## Problems

### 21-1 Off-line minimum

> The __*off-line minimum problem*__ asks us to maintain a dynamic set $$T$$ of elements from the domain $$\{1, 2, \dots, n\}$$ under the operations INSERT and EXTRACT-MIN. We are given a sequence $$S$$ of $$n$$ INSERT and $$m$$ EXTRACT-MIN calls, where each key in $$\{1, 2, \dots, n\}$$ is inserted exactly once. We wish to determine which key is returned by each EXTRACT-MIN call. Specifically, we wish to fill in an array $$extracted[1 \dots m]$$, where for $$i = 1, 2, \dots, m$$, $$extracted[i]$$ is the key returned by the $$i$$th EXTRACT-MIN call. The problem is "off-line" in the sense that we are allowed to process the entire sequence $$S$$ before determining any of the returned keys.

> __*a*__. In the following instance of the off-line minimum problem, each operation INSERT$$(i)$$ is represented by the value of $$i$$ and each EXTRACT-MIN is represented by the letter E:

> 4, 8, E, 3, E, 9, 2, 6, E, E, E, 1, 7, E, 5.

> Fill in the correct values in the _extracted_ array.

4, 3, 2, 6, 8, 1.

> To develop an algorithm for this problem, we break the sequence $$S$$ into homogeneous subsequences. That is, we represent $$S$$ by

> $$I_1, E, I_2, E, I_3, \dots, I_m, E, I_{m+1}$$

> where each $$E$$ represents a single EXTRACT-MIN call and each $$\text{I}_j$$ represents a (possibly empty) sequence of INSERT calls. For each subsequence $$\text{I}_j$$ , we initially place the keys inserted by these operations into a set $$K_j$$ , which is empty if $$\text{I}_j$$ is empty. We then do the following:

> ```
OFF-LINE-MINIMUM(m, n)
1  for i = 1 to n
2       determine j such that i \in K_j
3       if j \ne m + 1
4            extracted[j] = i
5            let l be the smallest value greater than j
                   for which set K_l exists
6            K_l = K_j \cup K_l , destroying K_j
7  return extracted 
```

> __*b*__. Argue that the array extracted returned by OFF-LINE-MINIMUM is correct.

Greedy.

> __*c*__. Describe how to implement OFF-LINE-MINIMUM efficiently with a disjoint-set data structure. Give a tight bound on the worst-case running time of your implementation.

```python
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


def off_line_minimum(q, n):
    m = len([0 for v in q if v == 'E'])
    ds = DisjointSetForest(m + 1)
    pos = [-1] * (n + 1)
    i = 0
    for v in q:
        if v == 'E':
            i += 1
        else:
            pos[v] = i
    extracted = [None] * m
    for i in xrange(1, n + 1):
        j = ds.find_set(pos[i])
        if j < m:
            extracted[j] = i
            ds.link(j, j + 1)
    return extracted
```

### 21-2 Depth determination

> In the __*depth-determination problem*__, we maintain a forest $$\mathcal{F} = \{T_i\}$$ of rooted trees under three operations:

> MAKE-TREE$$(v)$$ creates a tree whose only node is $$v$$.

> FIND-DEPTH$$(v)$$ returns the depth of node $$v$$ within its tree.

> GRAFT$$(r, v)$$ makes node $$r$$, which is assumed to be the root of a tree, become the child of node $$v$$, which is assumed to be in a different tree than $$r$$ but may or may not itself be a root.

> __*a*__. Suppose that we use a tree representation similar to a disjoint-set forest: $$v.p$$ is the parent of node $$v$$, except that $$v.p = v$$ if $$v$$ is a root. Suppose further that we implement GRAFT$$(r, v)$$ by setting $$r.p = v$$ and FIND-DEPTH$$(v)$$ by following the find path up to the root, returning a count of all nodes other than $$v$$ encountered. Show that the worst-case running time of a sequence of $$m$$ MAKE-TREE, FIND-DEPTH, and GRAFT operations is $$\Theta(m^2)$$.

$$m/3$$ MAKE-TREE, $$m/3$$ GRAFT to make a chain, $$m/3$$ FIND-DEPTH.

> By using the union-by-rank and path-compression heuristics, we can reduce the worst-case running time. We use the disjoint-set forest $$\mathcal{S} = \{S_i\}$$, where each set $$S_i$$ (which is itself a tree) corresponds to a tree $$T_i$$ in the forest $$\mathcal{F}$$. The tree structure within a set $$S_i$$, however, does not necessarily correspond to that of $$T_i$$. In fact, the implementation of $$S_i$$ does not record the exact parent-child relationships but nevertheless allows us to determine any node's depth in $$T_i$$.

> The key idea is to maintain in each node $$v$$ a "pseudodistance" $$v.d$$, which is defined so that the sum of the pseudodistances along the simple path from $$v$$ to the root of its set $$S_i$$ equals the depth of $$v$$ in $$T_i$$. That is, if the simple path from $$v$$ to its root in $$S_i$$ is $$v_0, v_1, \dots, v_k$$, where $$v_0 = v$$ and $$v_k$$ is $$S_i$$'s root, then the depth of $$v$$ in $$T_i$$ is $$\sum_{j=0}^k v_j.d$$.

> __*b*__. Give an implementation of MAKE-TREE.

```python
class TreeNode:
    def __init__(self):
        self.d = 0
        self.p = self
        self.rank = 0
```

> __*c*__. Show how to modify FIND-SET to implement FIND-DEPTH. Your implementation should perform path compression, and its running time should be linear in the length of the find path. Make sure that your implementation updates pseudodistances correctly.

```python
def find_depth(v):
    if v == v.p:
        return (v.d, v)
    (pd, p) = find_depth(v.p)
    d = v.d + pd
    v.d = d - p.d
    v.p = p
    return (d, p)
```

> __*d*__. Show how to implement GRAFT$$(r, v)$$, which combines the sets containing $$r$$ and $$v$$, by modifying the UNION and LINK procedures. Make sure that your implementation updates pseudodistances correctly. Note that the root of a set $$S_i$$ is not necessarily the root of the corresponding tree $$T_i$$.

```python
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
```

> __*e*__. Give a tight bound on the worst-case running time of a sequence of $$m$$ MAKE-TREE, FIND-DEPTH, and GRAFT operations, $$n$$ of which are MAKE-TREE operations.

$$O(m\alpha(n))$$.

### 21-3 Tarjan's off-line least-common-ancestors algorithm

> The least common ancestor of two nodes $$u$$ and $$v$$ in a rooted tree $$T$$ is the node $$w$$ that is an ancestor of both $$u$$ and $$v$$ and that has the greatest depth in $$T$$. In the off-line least-common-ancestors problem, we are given a rooted tree $$T$$ and an arbitrary set $$P = \{\{u, v\}\}$$ of unordered pairs of nodes in $$T$$, and we wish to determine the least common ancestor of each pair in $$P$$.

> To solve the off-line least-common-ancestors problem, the following procedure performs a tree walk of $$T$$ with the initial call LCA$$(T.root)$$. We assume that each node is colored WHITE prior to the walk.

> ```
LCA(u)
 1  MAKE-SET(u)
 2  FIND-SET(u).ancestor = u
 3  for each child v of u in T
 4       LCA(v)
 5       UNION(u, v)
 6       FIND-SET(u).ancestor = u
 7  u.color = BLACK
 8  for each node v such that {u, v} \in P
 9       if v.color == BLACK
10            print "The least common ancestor of"
                    u "and" v "is" FIND-SET(v).ancestor
```

> __*a*__. Argue that line 10 executes exactly once for each pair $$\{u, v\} \in P$$.

> __*b*__. Argue that at the time of the call LCA$$(u)$$, the number of sets in the disjoint-set data structure equals the depth of $$u$$ in $$T$$.

> __*c*__. Prove that LCA correctly prints the least common ancestor of $$u$$ and $$v$$ for each pair $$\{u, v\} \in P$$.

> __*d*__. Analyze the running time of LCA, assuming that we use the implementation of the disjoint-set data structure in Section 21.3.

