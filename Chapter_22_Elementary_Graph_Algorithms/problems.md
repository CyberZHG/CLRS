## Problems

### 22-1 Classifying edges by breadth-first search

> A depth-first forest classifies the edges of a graph into tree, back, forward, and cross edges. A breadth-first tree can also be used to classify the edges reachable from the source of the search into the same four categories.

> __*a*__. Prove that in a breadth-first search of an undirected graph, the following properties hold:
> 1. There are no back edges and no forward edges.
> 2. For each tree edge $$(u, v)$$, we have $$v.d = u.d + 1$$.
> 3. For each cross edge $$(u, v)$$, we have $$v.d = u.d$$ or $$v.d = u.d + 1$$. 

> __*b*__. Prove that in a breadth-first search of a directed graph, the following properties hold:
> 1. There are no forward edges.
> 2. For each tree edge $$(u, v)$$, we have $$v.d = u.d + 1$$.
> 3. For each cross edge $$(u, v)$$, we have $$v.d \le u.d + 1$$.
> 4. For each back edge $$(u, v)$$, we have $$0 \le v.d \le u.d$$.

### 22-2 Articulation points, bridges, and biconnected components

> Let $$G = (V, E)$$ be a connected, undirected graph. An articulation point of $$G$$ is a vertex whose removal disconnects $$G$$. A bridge of $$G$$ is an edge whose removal disconnects $$G$$. A biconnected component of $$G$$ is a maximal set of edges such that any two edges in the set lie on a common simple cycle. Figure 22.10 illustrates these definitions. We can determine articulation points, bridges, and biconnected components using depth-first search. Let $$G_\pi = (V, E_\pi)$$ be a depth-first tree of $$G$$.

> __*a*__. Prove that the root of $$G_\pi$$ is an articulation point of $$G$$ if and only if it has at least two children in $$G_\pi$$.

At least two children => at least two components that are not connected.

> __*b*__. Let $$v$$ be a nonroot vertex of $$G_\pi$$. Prove that $$v$$ is an articulation point of $$G$$ if and only if $$v$$ has a child $$s$$ such that there is no back edge from $$s$$ or any descendant of $$s$$ to a proper ancestor of $$v$$.

Connect to ancestor => loop.

> __*c*__. Let
> 
> $$v.low = \min \left \{ 
\begin{array}{l}
v.d,\\
w.d: (u, w) ~\text{is a back edge for some descendant}~u~\text{of}~v
\end{array}
\right .$$.

> Show how to computer $$v.low$$ for all vertices $$v \in V$$ in $$O(E)$$ time.

In DFS, for each edge, $$v.low = min(v.low, w.d)$$.

> __*d*__. Show how to compute all articulation points in $$O(E)$$ time.

(1) Root and have at least two children.

(2) Nonroot $$u$$ and there exist an edge $$(u, v) \in E$$ that $$v.low >= u.d$$.

> __*e*__. Prove that an edge of $$G$$ is a bridge if and only if it does not lie on any simple cycle of $$G$$.

No cycle => two components that are connected only by one edge.

> __*f*__. Show how to compute all the bridges of $$G$$ in $$O(E)$$ time.

$$v.low > u.d$$.

> __*g*__. Prove that the biconnected components of $$G$$ partition the nonbridge edges of $$G$$.

> __*h*__. Give an $$O(E)$$-time algorithm to label each edge $$e$$ of $$G$$ with a positive integer $$e.bcc$$ such that $$e.bcc = e'.bcc$$ if and only if $$e$$ and $$e'$$ are in the same biconnected component.

Delete bridges then DFS/BFS.

### 22-3 Euler tour

> An Euler tour of a strongly connected, directed graph $$G = (V, E)$$ is a cycle that traverses each edge of $$G$$ exactly once, although it may visit a vertex more than once.

> __*a*__. Show that $$G$$ has an Euler tour if and only if in-degree$$(v)=$$out-degree$$(v)$$ for each vertex $$v \in V$$.

> __*b*__. Describe an $$O(E)$$-time algorithm to find an Euler tour of $$G$$ if one exists. (Hint: Merge edge-disjoint cycles.)

### 22-4 Reachability

> Let $$G = (V, E)$$ be a directed graph in which each vertex $$u \in V$$ is labeled with a unique integer $$L(U)$$ from the set $$\{1, 2, \dots, |V|\}$$. For each vertex $$u \in V$$, let $$R(u) = \{v \in V: u \leadsto v \}$$ be the set of vertices that are reachable from $$u$$. Define $$\min(u)$$ to be the vertex in $$R(u)$$ whose label is minimum, i.e., $$\min(u)$$ is the vertex $$v$$ such that $$L(v) = \min \{L(w): w \in R(u) \}$$. Give an $$O(V + E)$$-time algorithm that computes $$\min(u)$$ for all vertices $$u \in V$$.

