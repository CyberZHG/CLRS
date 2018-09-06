## 23.1 Growing a minimum spanning tree

### 23.1-1

> Let $(u, v)$ be a minimum-weight edge in a connected graph $G$. Show that $(u, v)$ belongs to some minimum spanning tree of $G$.

$S = {u}$.

### 23.1-2

> Professor Sabatier conjectures the following converse of Theorem 23.1. Let $G = (V, E)$ be a connected, undirected graph with a real-valued weight function $w$ defined on $E$. Let $A$ be a subset of $E$ that is included in some minimum spanning tree for $G$, let $(S, V - S)$ be any cut of $G$ that respects $A$, and let $(u, v)$ be a safe edge for $A$ crossing $(S, V - S)$. Then, $(u, v)$ is a light edge for the cut. Show that the professor's conjecture is incorrect by giving a counterexample.

Not light.

### 23.1-3

> Show that if an edge $(u, v)$ is contained in some minimum spanning tree, then it is a light edge crossing some cut of the graph.

$(u, v)$ is a bridge in the minimum spanning tree, thus $V$ can be divided into two components.

### 23.1-4

> Give a simple example of a connected graph such that the set of edges $\\{(u, v):$ there exists a cut $(S, V - S)$ such that $(u, v)$ is a light edge crossing $(S, V - S)\\}$ does not form a minimum spanning tree.

$E = \\{(u, v), (v, w), (w, u)\\}$ with the same weight.

### 23.1-5

> Let $e$ be a maximum-weight edge on some cycle of connected graph $G = (V, E)$. Prove that there is a minimum spanning tree of $G' = (V, E - \\{e\\})$ that is also a minimum spanning tree of $G$. That is, there is a minimum spanning tree of $G$ that does not include $e$.

The edges in the cycle are lighter than the maximum-weight edge.

### 23.1-6

> Show that a graph has a unique minimum spanning tree if, for every cut of the graph, there is a unique light edge crossing the cut. Show that the converse is not true by giving a counterexample.

Counterexample: $E = \\{(u, v), (u, w)\\}$ with the same weight.

### 23.1-7

> Argue that if all edge weights of a graph are positive, then any subset of edges that connects all vertices and has minimum total weight must be a tree. Give an example to show that the same conclusion does not follow if we allow some weights to be nonpositive.

Not a tree: remove one edge from the cycle.

Nonpositive: $E = \\{(u, v), (v, w), (w, u)\\}$ with the same weight -1.

### 23.1-8

> Let $T$ be a minimum spanning tree of a graph $G$, and let $L$ be the sorted list of the edge weights of $T$. Show that for any other minimum spanning tree $T'$ of $G$, the list $L$ is also the sorted list of edge weights of $T'$.

$\dots$

### 23.1-9

> Let $T$ be a minimum spanning tree of a graph $G = (V, E)$, and let $V'$ be a subset of $V$. Let $T'$ be the subgraph of $T$ induced by $V'$, and let $G'$ be the subgraph of $G$ induced by $V'$. Show that if $T'$ is connected, then $T'$ is a minimum spanning tree of $G'$.

Cut $V'$.

### 23.1-10

> Given a graph $G$ and a minimum spanning tree $T$, suppose that we decrease the weight of one of the edges in $T$. Show that $T$ is still a minimum spanning tree for $G$. More formally, let $T$ be a minimum spanning tree for $G$ with edge weights given by weight function $w$. Choose one edge $(x, y) \in T$ and a positive number $k$, and define the weight function $w'$ by

> $$
w'(u, v) = \left \\{
\begin{array}{ll}
w(u, v) & \text{if}\~(u, v) \ne (x, y), \\\\
w(x, y) - k & \text{if}\~(u, v) = (x, y).
\end{array}
\right .
$$

> Show that $T$ is a minimum spanning tree for $G$ with edge weights given by $w'$.

Lighter.

### 23.1-11 $\star$

> Given a graph $G$ and a minimum spanning tree $T$, suppose that we decrease the weight of one of the edges not in $T$. Give an algorithm for finding the minimum spanning tree in the modified graph.

If the edge $(u, v)$ is not in $T$ and its weight is less than some edge in the path from $u$ to $v$, then replace the edge with maximum weight in the path with $(u, v)$.
