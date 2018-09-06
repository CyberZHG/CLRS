## 24.1 The Bellman-Ford algorithm

### 24.1-1

> Run the Bellman-Ford algorithm on the directed graph of Figure 24.4, using vertex $z$ as the source. In each pass, relax edges in the same order as in the figure, and show the $d$ and $\pi$ values after each pass. Now, change the weight of edge $(z,x)$ to 4 and run the algorithm again, using $s$ as the source.

| \ | $s$ | $t$ | $x$ | $y$ | $z$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
|$d$|2|4|6|9|0|
|$\pi$|$z$|$x$|$y$|$s$|NIL|

| \ | $s$ | $t$ | $x$ | $y$ | $z$ |
|:-:|:-:|:-:|:-:|:-:|:-:|
|$d$|0|0|2|7|-2|
|$\pi$|NIL|$x$|$z$|$s$|$t$|

### 24.1-2

> Prove Corollary 24.3.

No path property.

### 24.1-3

> Given a weighted, directed graph $G = (V, E)$ with no negative-weight cycles, let $m$ be the maximum over all vertices $v \in V$ of the minimum number of edges in a shortest path from the source $s$ to $v$. (Here, the shortest path is by weight, not the number of edges.) Suggest a simple change to the Bellman-Ford algorithm that allows it to terminate in $m + 1$ passes, even if $m$ is not known in advance.

Stop when no vertex is relaxed in a single loop.

### 24.1-4

> Modify the Bellman-Ford algorithm so that it sets $v.d$ to $-\infty$ for all vertices $v$ for which there is a negative-weight cycle on some path from the source to $v$.

```
if v.d > u.d + w(u, v)
     v.d = -inf
```

### 24.1-5 $\star$

> Let $G = (V, E)$ be a weighted, directed graph with weight function $w : E \rightarrow \mathbb{R}$. Give an $O(VE)$-time algorithm to find, for each vertex $v \in V$, the value $\delta^\*(v)=\min\_{u \in V} \{ \delta(u, v) \}$.

```
RELAX(u, v, w)
1 if v.d > min(w(u, v), w(u, v) + u.d)
2      v.d > min(w(u, v), w(u, v) + u.d)
3      v.pi = u.pi
```

### 24.1-6 $\star$

> Suppose that a weighted, directed graph $G = (V, E)$ has a negative-weight cycle. Give an efficient algorithm to list the vertices of one such cycle. Prove that your algorithm is correct.

Based on exercise 24.1-4, DFS from a vertex $u$ that $u.d = -\infty$, if the weight sum on the search path is negative and the next vertex is BLACK, then the search path forms a negative-weight cycle.
