## 25.2 The Floyd-Warshall algorithm

### 25.2-1

> Run the Floyd-Warshall algorithm on the weighted, directed graph of Figure 25.2. Show the matrix $D^{(k)}$ that results for each iteration of the outer loop.

$k=1$:
$$
\left \{ \begin{matrix}
0 & \infty & \infty & \infty & -1 & \infty\\\\
1 & 0 & \infty & 2 & 0 & \infty\\\\
\infty & 2 & 0 & \infty & \infty & -8\\\\
-4 & \infty & \infty & 0 & -5 & \infty\\\\
\infty & 7 & \infty & \infty & 0 & \infty\\\\
\infty & 5 & 10 & \infty & \infty & 0\\\\
\end{matrix} \right \}
$$

$k=2$:
$$
\left \{ \begin{matrix}
0 & \infty & \infty & \infty & -1 & \infty\\\\
1 & 0 & \infty & 2 & 0 & \infty\\\\
3 & 2 & 0 & 4 & 2 & -8\\\\
-4 & \infty & \infty & 0 & -5 & \infty\\\\
8 & 7 & \infty & 9 & 0 & \infty\\\\
6 & 5 & 10 & 7 & 5 & 0\\\\
\end{matrix} \right \}
$$
$k=3$:
$$
\left \{ \begin{matrix}
0 & \infty & \infty & \infty & -1 & \infty\\\\
1 & 0 & \infty & 2 & 0 & \infty\\\\
3 & 2 & 0 & 4 & 2 & -8\\\\
-4 & \infty & \infty & 0 & -5 & \infty\\\\
8 & 7 & \infty & 9 & 0 & \infty\\\\
6 & 5 & 10 & 7 & 5 & 0\\\\
\end{matrix} \right \}
$$

$k=4$:
$$
\left \{ \begin{matrix}
0 & \infty & \infty & \infty & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
0 & 2 & 0 & 4 & -1 & -8\\\\
-4 & \infty & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 2 & 0\\\\
\end{matrix} \right \}
$$

$k=5$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & 8 & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
0 & 2 & 0 & 4 & -1 & -8\\\\
-4 & 2 & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 2 & 0\\\\
\end{matrix} \right \}
$$

$k=6$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & 8 & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
-5 & -3 & 0 & -1 & -6 & -8\\\\
-4 & 2 & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 2 & 0\\\\
\end{matrix} \right \}
$$

### 25.2-2

> Show how to compute the transitive closure using the technique of Section 25.1.

### 25.2-3

> Modify the FLOYD-WARSHALL procedure to compute the $\prod^{(k)}$ matrices according to equations (25.6) and (25.7). Prove rigorously that for all $i \in V$, the predecessor subgraph $G\_{\pi, i}$ is a shortest-paths tree with root $i$.

### 25.2-4

> As it appears above, the Floyd-Warshall algorithm requires $\Theta(n^3)$ space, since we compute $d\_{ij}^{(k)}$ for $i, j, k = 1, 2, \dots, n$. Show that the following procedure, which simply drops all the superscripts, is correct, and thus only $\Theta(n^2)$ space is required.

### 25.2-5

> Suppose that we modify the way in which equation (25.7) handles equality:

> $$
\pi\_{ij}^{(k)} = \left \{ 
\begin{array}{ll}
\pi\_{ij}^{(k-1)} & \~\text{if}\~ d\_{ij}^{(k-1)} < d\_{ik}^{(k-1)} + d\_{kj}^{(k-1)}, \\\\
\pi\_{kj}^{(k-1)} & \~\text{if}\~ d\_{ij}^{(k-1)} \ge d\_{ik}^{(k-1)} + d\_{kj}^{(k-1)}.
\end{array}
\right .
$$

> Is this alternative definition of the predecessor matrix $\prod$ correct?

Correct.

### 25.2-6

> How can we use the output of the Floyd-Warshall algorithm to detect the presence of a negative-weight cycle?

If $D^{(n+1)} \ne D^{(n)}$, then the graph contains negative-weight cycle.

### 25.2-7

> Another way to reconstruct shortest paths in the Floyd-Warshall algorithm uses values $\phi\_{ij}^{(k)}$ for $i, j, k = 1, 2, \dots, n$, where $\phi\_{ij}^{(k)}$ is the highest-numbered intermediate vertex of a shortest path from $i$ to $j$ in which all intermediate vertices are in the set $\{1, 2, \dots, k \}$. Give a recursive formulation for $\phi\_{ij}^{(k)}$, modify the FLOYD-WARSHALL procedure to compute the $\phi\_{ij}^{(k)}$ values, and rewrite the PRINT-ALLPAIRS- SHORTEST-PATH procedure to take the matrix $\Phi = (\phi\_{ij}^{(n)})$ as an input. How is the matrix $\Phi$ like the $s$ table in the matrix-chain multiplication problem of Section 15.2?

### 25.2-8

> Give an $O(VE)$-time algorithm for computing the transitive closure of a directed
graph $G = (V, E)$.

DFS from each vertex.

### 25.2-9

> Suppose that we can compute the transitive closure of a directed acyclic graph in $f(|V|, |E|)$ time, where $f$ is a monotonically increasing function of $|V|$ and $|E|$. Show that the time to compute the transitive closure $G^\* = (V, E^\*)$ of a general directed graph $G = (V, E)$ is then $f(|V|, |E|) + O(V + E^\*)$.

All the pairs of vertices in one SCC are connected, and the SCCs forms a directed acyclic graph.
