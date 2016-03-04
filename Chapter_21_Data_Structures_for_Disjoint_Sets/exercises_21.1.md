## 21.1 Disjoint-set operations

### 21.1-1

> Suppose that CONNECTED-COMPONENTS is run on the undirected graph $$G = (V, E)$$, where $$V = \{a, b, c, d, e, f, g, h, i, j, k\}$$ and the edges of $$E$$ are processed in the order $$(d, i), (f, k), (g, i), (b, g), (a, h), (i, j), (d, k), (b, j), (d, f), (g, j), (a, e)$$. List the vertices in each connected component after each iteration of lines 3–5.

### 21.1-2

> Show that after all edges are processed by CONNECTED-COMPONENTS, two vertices are in the same connected component if and only if they are in the same set.

### 21.1-3

> During the execution of CONNECTED-COMPONENTS on an undirected graph $$G = (V, E)$$ with $$k$$ connected components, how many times is FIND-SET called? How many times is UNION called? Express your answers in terms of $$|V|$$, $$|E|$$, and $$k$$.
