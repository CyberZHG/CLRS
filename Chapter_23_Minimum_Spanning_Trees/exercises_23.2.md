## 23.2 The algorithms of Kruskal and Prim

### 23.2-1

> Kruskal's algorithm can return different spanning trees for the same input graph $$G$$, depending on how it breaks ties when the edges are sorted into order. Show that for each minimum spanning tree $$T$$ of $$G$$, there is a way to sort the edges of $$G$$ in Kruskal's algorithm so that the algorithm returns $$T$$.

### 23.2-2

> Suppose that we represent the graph $$G = (V, E)$$ as an adjacency matrix. Give a simple implementation of Prim’s algorithm for this case that runs in $$O(V^2)$$ time.

### 23.2-3

> For a sparse graph $$G = (V, E)$$, where $$|E| = \Theta(V)$$, is the implementation of Prim’s algorithm with a Fibonacci heap asymptotically faster than the binary-heap implementation? What about for a dense graph, where $$|E| = \Theta(V^2)$$? How must the sizes $$|E|$$ and $$|V|$$ be related for the Fibonacci-heap implementation to be asymptotically faster than the binary-heap implementation?

### 23.2-4

> Suppose that all edge weights in a graph are integers in the range from $$1$$ to $$|V|$$. How fast can you make Kruskal's algorithm run? What if the edge weights are integers in the range from $$1$$ to $$W$$ for some constant $$W$$?

### 23.2-5

> Suppose that all edge weights in a graph are integers in the range from $$1$$ to $$|V|$$. How fast can you make Prim's algorithm run? What if the edge weights are integers in the range from $$1$$ to $$W$$ for some constant $$W$$?

### 23.2-6 $$\star$$

> Suppose that the edge weights in a graph are uniformly distributed over the halfopen interval $$[0, 1)$$. Which algorithm, Kruskal's or Prim's, can you make run faster?

### 23.2-7 $$\star$$

> Suppose that a graph $$G$$ has a minimum spanning tree already computed. How quickly can we update the minimum spanning tree if we add a new vertex and incident edges to $$G$$?

### 23.2-8

> Professor Borden proposes a new divide-and-conquer algorithm for computing minimum spanning trees, which goes as follows. Given a graph $$G = (V, E)$$, partition the set $$V$$ of vertices into two sets $$V_1$$ and $$V_2$$ such that $$|V_1|$$ and $$|V_2|$$ differ by at most $$1$$. Let $$E_1$$ be the set of edges that are incident only on vertices in $$V_1$$, and let $$E_2$$ be the set of edges that are incident only on vertices in $$V_2$$. Recursively solve a minimum-spanning-tree problem on each of the two subgraphs $$G_1 = (V_1, E_1)$$ and $$G_2 = (V_2, E_2)$$. Finally, select the minimum-weight edge in E that crosses the cut $$(V_1, V_2)$$, and use this edge to unite the resulting two minimum spanning trees into a single spanning tree.
> 
> Either argue that the algorithm correctly computes a minimum spanning tree of $$G$$, or provide an example for which the algorithm fails.

