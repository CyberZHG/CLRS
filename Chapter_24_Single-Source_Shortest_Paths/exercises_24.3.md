## 24.3 Dijkstra's algorithm

### 24.3-1

> Run Dijkstra's algorithm on the directed graph of Figure 24.2, first using vertex $s$ as the source and then using vertex $z$ as the source. In the style of Figure 24.6, show the $d$ and $\pi$ values and the vertices in set $S$ after each iteration of the __while__ loop.

### 24.3-2

> Give a simple example of a directed graph with negative-weight edges for which Dijkstra's algorithm produces incorrect answers. Why doesn't the proof of Theorem 24.6 go through when negative-weight edges are allowed?

### 24.3-3

> Suppose we change line 4 of Dijkstra's algorithm to the following. 
> 
> 4  __while__ $|Q| > 1$
> 
> This change causes the __while__ loop to execute $|V| - 1$ times instead of $|V|$ times. Is this proposed algorithm correct?

Correct.

### 24.3-4

> Professor Gaedel has written a program that he claims implements Dijkstra's algorithm. The program produces $v.d$ and $v.\pi$ for each vertex $v \in V$. Give an $O(V + E)$-time algorithm to check the output of the professor's program. It should determine whether the $d$ and $\pi$ attributes match those of some shortest-paths tree. You may assume that all edge weights are nonnegative.

Relax on the shortest path tree.

### 24.3-5

> Professor Newman thinks that he has worked out a simpler proof of correctness for Dijkstra's algorithm. He claims that Dijkstra's algorithm relaxes the edges of every shortest path in the graph in the order in which they appear on the path, and therefore the path-relaxation property applies to every vertex reachable from the source. Show that the professor is mistaken by constructing a directed graph for which Dijkstra's algorithm could relax the edges of a shortest path out of order.

### 24.3-6

> We are given a directed graph $G = (V, E)$ on which each edge $(u, v) \in E$ has an associated value $r(u, v)$, which is a real number in the range $0 \le r(u, v) \le 1$ that represents the reliability of a communication channel from vertex $u$ to vertex $v$. We interpret $r(u, v)$ as the probability that the channel from $u$ to $v$ will not fail, and we assume that these probabilities are independent. Give an efficient algorithm to find the most reliable path between two given vertices.

$w(u, v) = \lg r(u, v)$.

### 24.3-7

> Let $G = (V, E)$ be a weighted, directed graph with positive weight function $w: E \rightarrow \{ 1, 2, \dots, W \}$ for some positive integer $W$, and assume that no two vertices have the same shortest-path weights from source vertex $s$. Now suppose that we define an unweighted, directed graph $G' = (V \cup V', E')$ by replacing each edge $(u, v) \in E$ with $w(u, v)$ unit-weight edges in series. How many vertices does $G'$ have? Now suppose that we run a breadth-first search on $G'$. Show that the order in which the breadth-first search of $G'$ colors vertices in $V$ black is the same as the order in which Dijkstra's algorithm extracts the vertices of $V$ from the priority queue when it runs on $G$.

$V + \sum\_{(u, v) \in E} w(u, v) - E$.

### 24.3-8

> Let $G = (V, E)$ be a weighted, directed graph with nonnegative weight function $w: E \rightarrow \{ 0, 1, \dots, W \}$ for some nonnegative integer $W$. Modify Dijkstra's algorithm to compute the shortest paths from a given source vertex s in $O(WV + E)$ time.

Use array to store vertices.

### 24.3-9

> Modify your algorithm from Exercise 24.3-8 to run in $O((V + E) \lg W)$ time. (Hint: How many distinct shortest-path estimates can there be in $V - S$ at any point in time?)

Heap.

### 24.3-10

> Suppose that we are given a weighted, directed graph $G = (V, E)$ in which edges that leave the source vertex $s$ may have negative weights, all other edge weights are nonnegative, and there are no negative-weight cycles. Argue that Dijkstra's algorithm correctly finds shortest paths from $s$ in this graph.
