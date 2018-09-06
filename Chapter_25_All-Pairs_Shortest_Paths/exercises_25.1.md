## 25.1 Shortest paths and matrix multiplication

### 25.1-1

> Run SLOW-ALL-PAIRS-SHORTEST-PATHS on the weighted, directed graph of Figure 25.2, showing the matrices that result for each iteration of the loop. Then do the same for FASTER-ALL-PAIRS-SHORTEST-PATHS.

Initial:

$$
\left \{ \begin{matrix}
0 & \infty & \infty & \infty & -1 & \infty\\\\
1 & 0 & \infty & 2 & \infty & \infty\\\\
\infty & 2 & 0 & \infty & \infty & -8\\\\
-4 & \infty & \infty & 0 & 3 & \infty\\\\
\infty & 7 & \infty & \infty & 0 & \infty\\\\
\infty & 5 & 10 & \infty & \infty & 0\\\\
\end{matrix} \right \}
$$
Slow:

$m=2$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & \infty & -1 & \infty\\\\
-2 & 0 & \infty & 2 & 0 & \infty\\\\
3 & -3 & 0 & 4 & \infty & -8\\\\
-4 & 10 & \infty & 0 & -5 & \infty\\\\
8 & 7 & \infty & 9 & 0 & \infty\\\\
6 & 5 & 10 & 7 & \infty & 0\\\\
\end{matrix} \right \}
$$
$m=3$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & 8 & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
-2 & -3 & 0 & -1 & 2 & -8\\\\
-4 & 2 & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 5 & 0\\\\
\end{matrix} \right \}
$$
$m=4$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & 8 & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
-5 & -3 & 0 & -1 & -3 & -8\\\\
-4 & 2 & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 2 & 0\\\\
\end{matrix} \right \}
$$
$m=5$:
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
Fast:

$m=2$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & \infty & -1 & \infty\\\\
-2 & 0 & \infty & 2 & 0 & \infty\\\\
3 & -3 & 0 & 4 & \infty & -8\\\\
-4 & 10 & \infty & 0 & -5 & \infty\\\\
8 & 7 & \infty & 9 & 0 & \infty\\\\
6 & 5 & 10 & 7 & \infty & 0\\\\
\end{matrix} \right \}
$$

$m=4$:
$$
\left \{ \begin{matrix}
0 & 6 & \infty & 8 & -1 & \infty\\\\
-2 & 0 & \infty & 2 & -3 & \infty\\\\
-5 & -3 & 0 & -1 & -3 & -8\\\\
-4 & 2 & \infty & 0 & -5 & \infty\\\\
5 & 7 & \infty & 9 & 0 & \infty\\\\
3 & 5 & 10 & 7 & 2 & 0\\\\
\end{matrix} \right \}
$$

$m=8$:
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
### 25.1-2

> Why do we require that $w\_{ii}=0$ for all $1 \le i \le n$?

To simplify (25.2).

### 25.1-3

> What does the matrix

> $$
L^{(0)} = \left ( \begin{matrix}
0 & \infty & \infty & \cdots & \infty \\\\
\infty & 0 & \infty & \cdots & \infty \\\\
\infty & \infty & 0 & \cdots & \infty \\\\
\vdots & \vdots & \vdots & \ddots & \vdots \\\\
\infty & \infty & \infty & \cdots & 0 \\\\
\end{matrix} \right )
$$

> used in the shortest-paths algorithms correspond to in regular matrix multiplication?

Unit.

### 25.1-4

> Show that matrix multiplication defined by EXTEND-SHORTEST-PATHS is associative.

### 25.1-5

> Show how to express the single-source shortest-paths problem as a product of matrices and a vector. Describe how evaluating this product corresponds to a Bellman-Ford-like algorithm (see Section 24.1).

A vector filled with 0 except that the source is 1.

### 25.1-6

> Suppose we also wish to compute the vertices on shortest paths in the algorithms of this section. Show how to compute the predecessor matrix $\prod$ from the completed matrix $L$ of shortest-path weights in $O(n^3)$ time.

If $l\_{ik} + w\_{kj} = l\_{ij}$, then $\pi\_{ij} = k$.

### 25.1-7

> We can also compute the vertices on shortest paths as we compute the shortestpath weights. Define $\pi\_{ij}^{(m)}$ as the predecessor of vertex $j$ on any minimum-weight path from $i$ to $j$ that contains at most $m$ edges. Modify the EXTEND-SHORTESTPATHS and SLOW-ALL-PAIRS-SHORTEST-PATHS procedures to compute the matrices$\prod^{(1)}, \prod^{(2)}, \dots, \prod^{(n-1)}$ as the matrices $L^{(1)}, L^{(2)}, \dots, L^{(n-1)}$ are computed.

If $l\_{ik}^{(m-1)} + w\_{kj} < l\_{ij}^{(m)}$, then $\pi\_{ij}^{(m)} = k$.

### 25.1-8

> The FASTER-ALL-PAIRS-SHORTEST-PATHS procedure, as written, requires us to store $\lceil \lg (n - 1) \rceil$ matrices, each with $n^2$ elements, for a total space requirement of $\Theta(n^2 \lg n)$. Modify the procedure to require only $\Theta(n^2)$ space by using only two $n \times n$ matrices.

```python
def fast_all_pairs_shortest_paths(w):
    n = len(w)
    m = 1
    while m < n - 1:
        w = extend_shortest_paths(w, w)
        m *= 2
    return w
```

### 25.1-9

> Modify FASTER-ALL-PAIRS-SHORTEST-PATHS so that it can determine whether
the graph contains a negative-weight cycle.

If $l\_{ii} < 0$, then there is a negative-weight cycle.

### 25.1-10

> Give an efficient algorithm to find the length (number of edges) of a minimum-length negative-weight cycle in a graph.

If $l\_{ii}^{(m)} < 0$ and $l\_{ii}^{(m-1)} = 0$, then the minimum-length is $m$.
