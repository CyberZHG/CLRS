## 22.1 Representations of graphs

### 22.1-1

> Given an adjacency-list representation of a directed graph, how long does it take to compute the out-degree of every vertex? How long does it take to compute the in-degrees?

* Out-degree: $$O(|V| + |E|)$$.
* In-degree: $$O(|V| + |E|)$$.

### 22.1-2

> Give an adjacency-list representation for a complete binary tree on 7 vertices. Give an equivalent adjacency-matrix representation. Assume that vertices are numbered from 1 to 7 as in a binary heap.

* Adjacency-list representation

$$1 \rightarrow 2 \rightarrow 3$$

$$2 \rightarrow 1 \rightarrow 4 \rightarrow 5$$

$$3 \rightarrow 1 \rightarrow 6 \rightarrow 7$$

$$4 \rightarrow 2$$

$$5 \rightarrow 2$$

$$6 \rightarrow 3$$

$$7 \rightarrow 3$$

* Adjacency-matrix representation

$$\left \{ \begin{matrix}
0 & 1 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 1 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
\end{matrix} \right \}$$

### 22.1-3

> The __*transpose*__ of a directed graph $$G = (V, E)$$ is the graph $$G^\text{T} = (V, E^\text{T})$$, where $$E^\text{T} = \{ (v, u) \in V \times V: (u, v) \in E \}$$. Thus, $$G^\text{T}$$ is $$G$$ with all its edges reversed. Describe efficient algorithms for computing $$G^\text{T}$$ from $$G$$, for both the adjacency-list and adjacency-matrix representations of $$G$$. Analyze the running times of your algorithms.

* Adjacency-list representation

Reconstruct, $$O(|V| + |E|)$$.

* Adjacency-matrix representation

Transpose matrix, $$O(|V|^2)$$.
