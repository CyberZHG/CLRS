## 27.2 Multithreaded matrix multiplication

### 27.2-1

> Draw the computation dag for computing P-SQUARE-MATRIX-MULTIPLY on $2 \times 2$ matrices, labeling how the vertices in your diagram correspond to strands in the execution of the algorithm. Use the convention that spawn and call edges point downward, continuation edges point horizontally to the right, and return edges point upward. Assuming that each strand takes unit time, analyze the work, span, and parallelism of this computation.

### 27.2-2

> Repeat Exercise 27.2-1 for P-MATRIX-MULTIPLY-RECURSIVE.

### 27.2-3

> Give pseudocode for a multithreaded algorithm that multiplies two $n \times n$ matrices with work $\Theta(n^3)$ but span only $\Theta(\lg n)$. Analyze your algorithm.

Based on exercise 27.1-6, the product of two vectors is $\Theta(\lg n)$, thus $T\_\infty = \Theta(\lg n) + \Theta(\lg n) + \Theta(\lg n) = \Theta(\lg n)$.

### 27.2-4

> Give pseudocode for an efficient multithreaded algorithm that multiplies a $p \times q$ matrix by a $q \times r$ matrix. Your algorithm should be highly parallel even if any of $p$, $q$, and $r$ are 1. Analyze your algorithm.

$T\_\infty = \Theta(\min \{ \lg p, \lg q, \lg r \})$

### 27.2-5

> Give pseudocode for an efficient multithreaded algorithm that transposes an $n \times n$ matrix in place by using divide-and-conquer to divide the matrix recursively into four $n/2 \times n/2$ submatrices. Analyze your algorithm.

$M = \left ( \begin{matrix} A & B \\\\ C & D \end{matrix} \right )$, $M^T = \left ( \begin{matrix} A^T & C^T \\\\ B^T & D^T \end{matrix} \right )$, $T\_\infty(n) = T\_\infty(n / 2) + \Theta(1)$, $T\_\infty = \Theta(\lg n)$.


### 27.2-6

> Give pseudocode for an efficient multithreaded implementation of the Floyd-Warshall algorithm (see Section 25.2), which computes shortest paths between all pairs of vertices in an edge-weighted graph. Analyze your algorithm.

$i$ and $j$ can be paralleled, $T\_\infty = \Theta(n \lg n)$.
