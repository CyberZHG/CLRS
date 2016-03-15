## Problems

### 23-1 Second-best minimum spanning tree

> Let $$G = (V, E)$$ be an undirected, connected graph whose weight function is $$w: E \rightarrow \mathbb{R}$$, and suppose that $$|E| \ge |V|$$ and all edge weights are distinct.

> We define a second-best minimum spanning tree as follows. Let $$\mathcal{T}$$ be the set of all spanning trees of $$G$$, and let $$T'$$ be a minimum spanning tree of $$G$$. Then a __*second-best minimum spanning tree*__ is a spanning tree $$T$$ such that $$W(T) = \min_{T'' \in \mathcal{T}-\{T'\}}\{w(T'')\}$$.

> __*a*__. Show that the minimum spanning tree is unique, but that the second-best minimum spanning tree need not be unique.

> __*b*__. Let $$T$$ be the minimum spanning tree of $$G$$. Prove that $$G$$ contains edges $$(u, v) \in T$$ and $$(x, y) \notin T$$ such that $$T - \{(u, v)\} \cup \{(x, y)\}$$ is a second-best minimum spanning tree of $$G$$.

> __*c*__. Let $$T$$ be a spanning tree of $$G$$ and, for any two verticces $$u, v \in V$$, let $$max[u,v]$$ denote an edge of maximum weight on the unique simple path between $$u$$ and $$v$$ in $$T$$. Describe an $$O(V^2)$$-time algorithm that, given $$T$$, computes $$max[u, v]$$ for all $$u, v \in V$$.

> __*d*__. Give an efficient algorithm to compute the second-best minimum spanning tree of $$G$$.

### 23-2 Minimum spanning tree in sparse graphs

> For a very sparse connected graph $$G = (V, E)$$, we can further improve upon the $$O(E + V \lg V)$$ running time of Prim's algorithm with Fibonacci heaps by preprocessing $$G$$ to decrease the number of vertices before running Prim's algorithm. In particular, we choose, for each vertex $$u$$, the minimum-weight edge $$(u, v)$$ incident on $$u$$, and we put $$(u, v)$$ into the minimum spanning tree under construction. We then contract all chosen edges (see Section B.4). Rather than contracting these edges one at a time, we first identify sets of vertices that are united into the same new vertex. Then we create the graph that would have resulted from contracting these edges one at a time, but we do so by "renaming" edges according to the sets into which their endpoints were placed. Several edges from the original graph may be renamed the same as each other. In such a case, only one edge results, and its weight is the minimum of the weights of the corresponding original edges.

> Initially, we set the minimum spanning tree $$T$$ being constructed to be empty, and for each edge $$(u, v) \in E$$, we initialize the attributes $$(u, v).orig = (u, v)$$ and $$(u, v).c = w(u, v)$$. We use the orig attribute to reference the edge from the initial graph that is associated with an edge in the contracted graph. The $$c$$ attribute holds the weight of an edge, and as edges are contracted, we update it according to the above scheme for choosing edge weights. The procedure MST-REDUCE takes inputs $$G$$ and $$T$$, and it returns a contracted graph $$G'$$ with updated attributes $$orig'$$ and $$c'$$. The procedure also accumulates edges of $$G$$ into the minimum spanning tree $$T$$.

> ```
MST-REDUCE(G, T)
1  for each v in G.V
2       v.mark = FALSE
3       MAKE-SET(v)
4  for each u in G.V
5       if u.mark == FALSE
6            choose v in G.Adj[u] such that (u, v).c is minimized
7            UNION(u, v)
8            T = T [ f(u, v).origg
9            u.mark = v.mark = TRUE
10  G'.V = {FIND-SET(v) : v in G.V}
11  G'.E = empty
12  for each (x, y) in G.E
13       u = FIND-SET(x)
14       v = FIND-SET(y)
15       if (u, v) not in G'.E
16            G'.E = G'.E union {(u, v)}
17            (u, v).orig' = (x, y).orig
18            (u, v).c' = (x, y).c
19       else if (x, y).c < (u,v).c'
20            (u, v).orig' = (x, y).orig
21            (u, v).c' = (x, y).c
22  construct adjacency lists G'.Adj for G'
23  return G' and T
```

> __*a*__. Let $$T$$ be the set of edges returned by MST-REDUCE, and let $$A$$ be the minimum spanning tree of the graph $$G'$$ formed by the call MST-PRIM$$(G', c', r)$$, where $$c'$$ is the weight attribute on the edges of $$G'.E$$ and $$r$$ is any vertex in $$G'.V$$. Prove that $$T \cup \{(x,y).orig':(x, y) \in A \}$$ is a minimum spanning tree of $$G$$.

> __*b*__. Argue that $$|G'.V| \le |V| / 2$$.

> __*c*__. Show how to implement MST-REDUCE so that it runs in $$O(E)$$ time. (Hint: Use simple data structures.)

> __*d*__. Suppose that we run $$k$$ phases of MST-REDUCE, using the output $$G'$$ produced by one phase as the input $$G$$ to the next phase and accumulating edges in $$T$$. Argue that the overall running time of the $$k$$ phases is $$O(kE)$$.

> __*e*__. Suppose that after running $$k$$ phases of MST-REDUCE, as in part (d), we run Prim's algorithm by calling MST-PRIM$$(G', c', r)$$, where $$G'$$, with weight attribute $$c'$$, is returned by the last phase and $$r$$ is any vertex in $$G'.V$$. Show how to pick $$k$$ so that the overall running time is $$O(E\lg \lg V)$$. Argue that your choice of $$k$$ minimizes the overall asymptotic running time.

> __*f*__. For what values of $$|E|$$ (in terms of $$|V|$$) does Prim's algorithm with preprocessing asymptotically beat Prim's algorithm without preprocessing?

