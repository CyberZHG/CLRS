## 23.2 The algorithms of Kruskal and Prim

### 23.2-1

> Kruskal's algorithm can return different spanning trees for the same input graph $G$, depending on how it breaks ties when the edges are sorted into order. Show that for each minimum spanning tree $T$ of $G$, there is a way to sort the edges of $G$ in Kruskal's algorithm so that the algorithm returns $T$.

$\dots$

### 23.2-2

> Suppose that we represent the graph $G = (V, E)$ as an adjacency matrix. Give a simple implementation of Prim's algorithm for this case that runs in $O(V^2)$ time.

$\dots$

### 23.2-3

> For a sparse graph $G = (V, E)$, where $|E| = \Theta(V)$, is the implementation of Prim's algorithm with a Fibonacci heap asymptotically faster than the binary-heap implementation? What about for a dense graph, where $|E| = \Theta(V^2)$? How must the sizes $|E|$ and $|V|$ be related for the Fibonacci-heap implementation to be asymptotically faster than the binary-heap implementation?

Binary-heap: $O(E \lg V)$ 

Fibonacci-heap: $O(E + V\lg V)$

* $|E| = \Theta(V)$

Binary-heap: $O(V \lg V) = O(V \lg V)$ 

Fibonacci-heap: $O(E + V\lg V) = O(V \lg V)$

* $|E| = \Theta(V^2)$

Binary-heap: $O(V^2 \lg V) = O(V^2 \lg V)$ 

Fibonacci-heap: $O(V^2 + V\lg V) = O(V^2)$

### 23.2-4

> Suppose that all edge weights in a graph are integers in the range from $1$ to $|V|$. How fast can you make Kruskal's algorithm run? What if the edge weights are integers in the range from $1$ to $W$ for some constant $W$?

* $1$ to $|V|$

Use counting sort, $O(E \alpha(V))$.

* $1$ to $W$

$\min(O(W + E\alpha(V)),O(E\lg V))$.

### 23.2-5

> Suppose that all edge weights in a graph are integers in the range from $1$ to $|V|$. How fast can you make Prim's algorithm run? What if the edge weights are integers in the range from $1$ to $W$ for some constant $W$?

* $1$ to $|V|$

Use van Emde Boas trees, $O(E \lg \lg V)$.

* $1$ to $W$

$\min(O(E\lg \lg W), O(E + V \lg V)$.

### 23.2-6 $\star$

> Suppose that the edge weights in a graph are uniformly distributed over the halfopen interval $[0, 1)$. Which algorithm, Kruskal's or Prim's, can you make run faster?

$\dots$

### 23.2-7 $\star$

> Suppose that a graph $G$ has a minimum spanning tree already computed. How quickly can we update the minimum spanning tree if we add a new vertex and incident edges to $G$?

$\dots$

### 23.2-8

> Professor Borden proposes a new divide-and-conquer algorithm for computing minimum spanning trees, which goes as follows. Given a graph $G = (V, E)$, partition the set $V$ of vertices into two sets $V\_1$ and $V\_2$ such that $|V\_1|$ and $|V\_2|$ differ by at most $1$. Let $E\_1$ be the set of edges that are incident only on vertices in $V\_1$, and let $E\_2$ be the set of edges that are incident only on vertices in $V\_2$. Recursively solve a minimum-spanning-tree problem on each of the two subgraphs $G\_1 = (V\_1, E\_1)$ and $G\_2 = (V\_2, E\_2)$. Finally, select the minimum-weight edge in $E$ that crosses the cut $(V\_1, V\_2)$, and use this edge to unite the resulting two minimum spanning trees into a single spanning tree.
> 
> Either argue that the algorithm correctly computes a minimum spanning tree of $G$, or provide an example for which the algorithm fails.

The algorithm fails. Suppose $E = \\{ (u, v), (u, w), (v, w) \\}$, the weight of $(u, v)$ and $(u, w)$ is 1, and the weight of $(v, w)$ is 1000, partition the set into two sets $V\_1 = \\{u\\}$ and $V\_2 = \\{ v, w \\}$.
