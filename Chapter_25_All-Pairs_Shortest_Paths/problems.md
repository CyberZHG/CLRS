## Problems

### 25-1 Transitive closure of a dynamic graph

> Suppose that we wish to maintain the transitive closure of a directed graph $G = (V, E)$ as we insert edges into $E$. That is, after each edge has been inserted, we want to update the transitive closure of the edges inserted so far. Assume that the graph $G$ has no edges initially and that we represent the transitive closure as a boolean matrix.

> __*a*__. Show how to update the transitive closure $G^* = (V, E^*)$ of a graph $G = (V, E)$ in $O(V^2)$ time when a new edge is added to $G$.

Suppose the inverted edge is $(u, v)$, then if $(a, u)$ is true and $(v, b)$ is true, then $(a, b)$ is true.

> __*b*__. Give an example of a graph $G$ and an edge $e$ such that $\Omega(V^2)$ time is required to update the transitive closure after the insertion of $e$ into $G$, no matter what algorithm is used.

Two connected components.

> __*c*__. Describe an efficient algorithm for updating the transitive closure as edges are inserted into the graph. For any sequence of $n$ insertions, your algorithm should run in total time $\sum_{i=1}^n t_i = O(V^3)$, where $t_i$ is the time to update the transitive closure upon inserting the $i$th edge. Prove that your algorithm attains this time bound.

If $(a, u)$ is true, $(a, v)$ is not true and $(v, b)$ is true, then $(a, b)$ is true.

### 25-2 Shortest paths in $\epsilon$-dense graphs

> A graph $G = (V, E)$ is __*$\epsilon$-dense*__ if $|E| = \Theta(V^{1 + \epsilon})$ for some constant $\epsilon$ in the range $0 < \epsilon \le 1$. By using $d$-ary min-heaps (see Problem 6-2) in shortest-paths algorithms on $\epsilon$-dense graphs, we can match the running times of Fibonacci-heap-based algorithms without using as complicated a data structure.

> __*a*__. What are the asymptotic running times for INSERT, EXTRACT-MIN, and DECREASE-KEY, as a function of $d$ and the number $n$ of elements in a $d$-ary min-heap? What are these running times if we choose $d = \Theta(n^\alpha)$ for some constant $0 < \alpha \le 1$? Compare these running times to the amortized costs of these operations for a Fibonacci heap.

* INSERT: $\Theta(\log_d n) = \Theta(1/\alpha)$.
* EXTRACT-MIN: $\Theta(d \log_d n) = \Theta(n^\alpha / \alpha)$.
* DECREASE-KEY: $\Theta(\log_d n) = \Theta(1/\alpha)$.

> __*b*__. Show how to compute shortest paths from a single source on an $\epsilon$-dense directed graph $G = (V, E)$ with no negative-weight edges in $O(E)$ time. (Hint: Pick $d$ as a function of $\epsilon$.)

Dijkstra, $O(d \log_d V \cdot V + \log_d V \cdot E)$, if $d = V^\epsilon$, then

$$
\begin{array}{ll}
& O(d \log_d V \cdot V + \log_d V \cdot E) \\
=& O(V^\epsilon \cdot V / \epsilon + E / \epsilon) \\
=& O((V^{1+\epsilon} + E) / \epsilon) \\
=& O((E + E) / \epsilon) \\
=& O(E)
\end{array}
$$

> __*c*__. Show how to solve the all-pairs shortest-paths problem on an $\epsilon$-dense directed graph $G = (V, E)$ with no negative-weight edges in $O(VE)$ time. 

Run $|V|$ times Dijkstra, since the algorithm is $O(E)$ based on __*b*__, the total time is $O(VE)$.

> __*d*__. Show how to solve the all-pairs shortest-paths problem in $O(VE)$ time on an $\epsilon$-dense directed graph $G = (V, E)$ that may have negative-weight edges but has no negative-weight cycles.

Johnson's reweight is $O(VE)$.
