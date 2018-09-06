## 22.3 Depth-first search

### 22.3-1

> Make a 3-by-3 chart with row and column labels WHITE, GRAY, and BLACK. In each cell $(i, j)$, indicate whether, at any point during a depth-first search of a directed graph, there can be an edge from a vertex of color $i$ to a vertex of color $j$. For each possible edge, indicate what edge types it can be. Make a second such chart for depth-first search of an undirected graph.

Directed:

| $i$ \ $j$ | WHITE | GRAY | BLACK |
| :---: | :---: | :---: | :---: |
| WHITE | TBFC | BC | C |
| GRAY | TF | TBF | TFC |
| BLACK |  | BC | TBFC |

Undirected:

| $i$ \ $j$ | WHITE | GRAY | BLACK |
| :---: | :---: | :---: | :---: |
| WHITE | TB | TB |  |
| GRAY | TB | TB | TB |
| BLACK |  | TB | TB |

### 22.3-2

> Show how depth-first search works on the graph of Figure 22.6. Assume that the _**for**_ loop of lines 5–7 of the DFS procedure considers the vertices in alphabetical order, and assume that each adjacency list is ordered alphabetically. Show the discovery and finishing times for each vertex, and show the classification of each edge.

![](./img/22.3-2_1.png)

* Tree edges: \(q, s\) \(s, v\) \(v, w\) \(q, t\) \(t, x\) \(x, z\) \(t, y\) \(r, u\)
* Back edges: \(w, s\) \(z, x\), \(y, q\)
* Forward edges: \(q, w\)
* Cross edges: \(r, y\) \(u, y\)

### 22.3-3

> Show the parenthesis structure of the depth-first search of Figure 22.4.

![](./img/22.3-3_1.png)

### 22.3-4

> Show that using a single bit to store each vertex color suffices by arguing that the DFS procedure would produce the same result if line 3 of DFS-VISIT was removed.

Line 3: color = BLACK

### 22.3-5

> Show that edge $(u, v)$ is
>
> _**a**_. a tree edge or forward edge if and only if $u.d < v.d < v.f < u.f$,

$u$ is an ancestor of $v$.

> _**b**_. a back edge if and only if $v.d \le u.d < u.f \le v.f$, and

$u$ is a descendant of $v$.

> _**c**_. a cross edge if and only if $v.d < v.f < u.d < u.f$.

$v$ is visited before $u$.

### 22.3-6

> Show that in an undirected graph, classifying an edge $(u, v)$ as a tree edge or a back edge according to whether $(u, v)$ or $(v, u)$ is encountered first during the depth-first search is equivalent to classifying it according to the ordering of the four types in the classification scheme.

By changing an undirected graph into a directed graph with two-way edges, an equivalent result is produced.

### 22.3-7

> Rewrite the procedure DFS, using a stack to eliminate recursion.

Goto.

### 22.3-8

> Give a counterexample to the conjecture that if a directed graph $G$ contains a path from $u$ to $v$, and if $u.d < v.d$ in a depth-first search of $G$, then $v$ is a descendant of $u$ in the depth-first forest produced.

$E = \\{(w, u), (w, v), (u, w)\\}$, search $w$ first.

### 22.3-9

> Give a counterexample to the conjecture that if a directed graph $G$ contains a path  
> from $u$ to $v$, then any depth-first search must result in $v.d \le u.f$.

$E = \\{(w, u), (w, v), (u, w)\\}$, search $w$ first.

### 22.3-10

> Modify the pseudocode for depth-first search so that it prints out every edge in the directed graph $G$, together with its type. Show what modifications, if any, you need to make if $G$ is undirected.

See exercises 22.3-5.

### 22.3-11

> Explain how a vertex $u$ of a directed graph can end up in a depth-first tree containing only $u$, even though $u$ has both incoming and outgoing edges in $G$.

$E = \\{(w, u), (u, v)\\}$, search $v$ then search $u$.

### 22.3-12

> Show that we can use a depth-first search of an undirected graph $G$ to identify the connected components of $G$, and that the depth-first forest contains as many trees as $G$ has connected components. More precisely, show how to modify depth-first search so that it assigns to each vertex $v$ an integer label $v.cc$ between $1$ and $k$, where $k$ is the number of connected components of $G$, such that $u.cc = v.cc$ if and only if $u$ and $v$ are in the same connected component.

```
DFS(G)
1  for each vertex u in G.V
2      u.color = WHITE
3      u:pi = NIL
4  time = 0
5  cc = 0
6  for each vertex u in G.V
7      if u.color == WHITE
8          cc = cc + 1
9          DFS-VISIT(G, u)
```

```
DFS-VISIT(G, u)
1  u.cc = cc
...
```

### 22.3-13 $\star$

> A directed graph $G = (V, E)$ is _**singly connected**_ if $u \leadsto v$ implies that $G$ contains at most one simple path from $u$ to $v$ for all vertices $u, v \in V$. Give an efficient algorithm to determine whether or not a directed graph is singly connected.

Run DFS for every vertex, if $v.color$ is BLACK, then the graph is not singly connected, $O(V\cdot(V+E))$.
