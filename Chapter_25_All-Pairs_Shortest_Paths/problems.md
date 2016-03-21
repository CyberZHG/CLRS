## Problems

### 25-1 Transitive closure of a dynamic graph

> Suppose that we wish to maintain the transitive closure of a directed graph $$G = (V, E)$$ as we insert edges into $$E$$. That is, after each edge has been inserted, we want to update the transitive closure of the edges inserted so far. Assume that the graph $$G$$ has no edges initially and that we represent the transitive closure as a boolean matrix.

> __*a*__. Show how to update the transitive closure $$G^* = (V, E^*)$$ of a graph $$G = (V, E)$$ in $$O(V^2)$$ time when a new edge is added to $$G$$.

Suppose the inverted edge is $$(u, v)$$, then if $$(a, u)$$ is true and $$(v, b)$$ is true, then $$(a, b)$$ is true.

> __*b*__. Give an example of a graph $$G$$ and an edge $$e$$ such that $$\Omega(V^2)$$ time is required to update the transitive closure after the insertion of $$e$$ into $$G$$, no matter what algorithm is used.

Two connected components.

> __*c*__. Describe an efficient algorithm for updating the transitive closure as edges are inserted into the graph. For any sequence of $$n$$ insertions, your algorithm should run in total time $$\sum_{i=1}^n t_i = O(V^3)$$, where $$t_i$$ is the time to update the transitive closure upon inserting the $$i$$th edge. Prove that your algorithm attains this time bound.

If $$(a, u)$$ is true, $$(a, v)$$ is not true and $$(v, b)$$ is true, then $$(a, b)$$ is true.

### 25-2 Shortest paths in -dense graphs

A graph G D .V;E/ is -dense if jEj D ‚.V 1C/ for some constant  in the
range 0 <   1. By using d-ary min-heaps (see Problem 6-2) in shortest-paths
algorithms on -dense graphs, we can match the running times of Fibonacci-heapbased
algorithms without using as complicated a data structure.
a. What are the asymptotic running times for INSERT, EXTRACT-MIN, and
DECREASE-KEY, as a function of d and the number n of elements in a d-ary
min-heap? What are these running times if we choose d D ‚.n˛/ for some
constant 0 < ˛  1? Compare these running times to the amortized costs of
these operations for a Fibonacci heap.
b. Show how to compute shortest paths from a single source on an -dense directed
graph G D .V;E/ with no negative-weight edges in O.E/ time. (Hint: Pick d
as a function of .)
c. Show how to solve the all-pairs shortest-paths problem on an -dense directed
graph G D .V;E/ with no negative-weight edges in O.VE/ time.
d. Show how to solve the all-pairs shortest-paths problem in O.VE/ time on an
-dense directed graph G D .V;E/ that may have negative-weight edges but
has no negative-weight cycles.

