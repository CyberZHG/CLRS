## 22.1 Representations of graphs

### 22.1-1

> Given an adjacency-list representation of a directed graph, how long does it take to compute the out-degree of every vertex? How long does it take to compute the in-degrees?

* Out-degree: $O(V + E)$.
* In-degree: $O(V + E)$.

### 22.1-2

> Give an adjacency-list representation for a complete binary tree on 7 vertices. Give an equivalent adjacency-matrix representation. Assume that vertices are numbered from 1 to 7 as in a binary heap.

* Adjacency-list representation

$1 \rightarrow 2 \rightarrow 3$

$2 \rightarrow 1 \rightarrow 4 \rightarrow 5$

$3 \rightarrow 1 \rightarrow 6 \rightarrow 7$

$4 \rightarrow 2$

$5 \rightarrow 2$

$6 \rightarrow 3$

$7 \rightarrow 3$

* Adjacency-matrix representation

$\left \{ \begin{matrix}
0 & 1 & 1 & 0 & 0 & 0 & 0 \\\\
1 & 0 & 0 & 1 & 1 & 0 & 0 \\\\
1 & 0 & 0 & 0 & 0 & 1 & 1 \\\\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\
\end{matrix} \right \}$

### 22.1-3

> The __*transpose*__ of a directed graph $G = (V, E)$ is the graph $G^\text{T} = (V, E^\text{T})$, where $E^\text{T} = \{ (v, u) \in V \times V: (u, v) \in E \}$. Thus, $G^\text{T}$ is $G$ with all its edges reversed. Describe efficient algorithms for computing $G^\text{T}$ from $G$, for both the adjacency-list and adjacency-matrix representations of $G$. Analyze the running times of your algorithms.

* Adjacency-list representation

Reconstruct, $O(V + E)$.

* Adjacency-matrix representation

Transpose matrix, $O(V^2)$.

### 22.1-4

> Given an adjacency-list representation of a multigraph $G = (V, E)$, describe an $O(V + E)$-time algorithm to compute the adjacency-list representation of the "equivalent" undirected graph $G' = (V, E')$, where $E'$ consists of the edges in $E$ with all multiple edges between two vertices replaced by a single edge and with all self-loops removed.

Merge sort.

### 22.1-5

> The __*square*__ of a directed graph $G = (V, E)$ is the graph $G^2 = (V, E^2)$ such that $(u, v) \in E^2$ if and only $G$ contains a path with at most two edges between $u$ and $v$. Describe efficient algorithms for computing $G^2$ from $G$ for both the adjacency-list and adjacency-matrix representations of $G$. Analyze the running times of your algorithms.

* Adjacency-list representation

```
for i in Adj[u]
    Adj^2[u].append(i)
    for j in Adj[i]
        Adj^2[u].append(j)
```

The running time depends on the distribution of edges.

* Adjacency-matrix representation

```
for i = 1 to V
    for j = 1 to V
        if a_{ij} = 1
            a^2_{ij} = 1
        else
            for k = 1 to V
                if a_{ik} == 1 and a_{kj} == 1:
                    a^2_{ij} = 1
                    break
```

$O(V^3)$.

### 22.1-6

> Most graph algorithms that take an adjacency-matrix representation as input require time $\Omega(V^2)$, but there are some exceptions. Show how to determine whether a directed graph $G$ contains a __*universal sink*__ - a vertex with in-degree $|V| - 1$ and out-degree 0 - in time $O(V)$, given an adjacency matrix for $G$.

Starting from $a\_{11}$, if $a\_{ij} = 0$ then $j = j + 1$, otherwise $i = i + 1$.

### 22.1-7

> The __*incidence matrix*__ of a directed graph $G = (V, E)$ with no self-loops is a $|V| \times |E|$ matrix $B = (b\_{ij})$ such that

> $$
b\_{ij} = \left \{
\begin{array}{rl}
-1 & \text{if edge}~j~\text{leaves vertex}~i, \\\\
1 & \text{if edge}~j~\text{enters vertex}~i, \\\\
0 & \text{otherwise}. \\\\
\end{array}
\right .
$$
> Describe what the entries of the matrix product $BB^T$ represent, where $B^T$ is the transpose of $B$.

$(BB^T)\_{ij} = \sum\_{k \in E} b\_{ik} \cdot b\_{jk}$, the result of $b\_{ik} \cdot b\_{jk}$ could be 0, 1 and -1. 0 indicates $i$ and $j$ are not connected by edge $k$; 1 indicates $i = j$; -1 indicates there is an edge from $i$ to $j$ or from $j$ to $i$. Therefore, if $i=j$, $(BB^T)\_{ij}$ is the degree of vertex $i$; if $i \ne j$, $(BB^T)\_{ij}$ is the negative of number of edges connecting $i$ and $j$.

### 22.1-8

> Suppose that instead of a linked list, each array entry $Adj[u]$ is a hash table containing the vertices $v$ for which $(u, v) \in E$. If all edge lookups are equally likely, what is the expected time to determine whether an edge is in the graph? What disadvantages does this scheme have? Suggest an alternate data structure for each edge list that solves these problems. Does your alternative have disadvantages compared to the hash table?

* Expected time: $O(1)$.
* Disadvantages: More space.
* Alternative: BST, RB-Trees, ...
* Disadvantages: $O(\lg n)$.
