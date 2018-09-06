## 26.2 The Ford-Fulkerson method

### 26.2-1

> Prove that the summations in equation (26.6) equal the summations in equation (26.7).

$\sum\_{v \in V\_2} f(s, v) = 0$, $\sum\_{v \in V\_1} f(v, s)$.

### 26.2-2

> In Figure 26.1(b), what is the flow across the cut $(\\{s, v\_2, v\_4\\}, \\{v\_1, v\_3, t\\})$? What is the capacity of this cut?

$f(S, T) = f(s, v\_1) + f(v\_2, v\_1) + f(v\_4, v\_3) + f(v\_4, t) - f(v\_3, v\_2) = 11 + 1 + 7 + 4 - 4 = 19$.

$c(S, T) = c(s, v\_1) + c(v\_2, v\_1) + c(v\_4, v\_3) + c(v\_4, t) = 16 + 4 + 7 + 4 = 31$.

### 26.2-3

> Show the execution of the Edmonds-Karp algorithm on the flow network of Figure 26.1(a).

### 26.2-4

> In the example of Figure 26.6, what is the minimum cut corresponding to the maximum flow shown? Of the augmenting paths appearing in the example, which one cancels flow?

### 26.2-5

> Recall that the construction in Section 26.1 that converts a flow network with multiple sources and sinks into a single-source, single-sink network adds edges with infinite capacity. Prove that any flow in the resulting network has a finite value if the edges of the original network with multiple sources and sinks have finite capacity.

Flow in equals flow out.

### 26.2-6

> Suppose that each source $s\_i$ in a flow network with multiple sources and sinks produces exactly $p\_i$ units of flow, so that $\sum\_{v \in V} f(s\_i, v) = p\_i$. Suppose also that each sink $t\_j$ consumes exactly $q\_j$ units, so that $\sum\_{v \in V} f(v, t\_j) = q\_j$, where $\sum\_i p\_i = \sum\_j q\_j$. Show how to convert the problem of finding a flow $f$ that obeys these additional constraints into the problem of finding a maximum flow in a single-source, single-sink flow network.

$c(s, s\_i) = p\_i$, $c(t\_j, t) = q\_j$.

### 26.2-7

> Prove Lemma 26.2.

### 26.2-8

> Suppose that we redefine the residual network to disallow edges into $s$. Argue that the procedure FORD-FULKERSON still correctly computes a maximum flow.

Correct.

### 26.2-9

> Suppose that both $f$ and $f'$ are flows in a network $G$ and we compute flow $f \uparrow f'$. Does the augmented flow satisfy the flow conservation property? Does it satisfy the capacity constraint?

It satisfies the flow conservation property and doesn't satisfy the capacity constraint.

### 26.2-10

> Show how to find a maximum flow in a network $G = (V, E)$ by a sequence of at most $|E|$ augmenting paths. (Hint: Determine the paths after finding the maximum flow.)

Find the minimum cut.

### 26.2-11

> The __*edge connectivity*__ of an undirected graph is the minimum number $k$ of edges that must be removed to disconnect the graph. For example, the edge connectivity of a tree is 1, and the edge connectivity of a cyclic chain of vertices is 2. Show how to determine the edge connectivity of an undirected graph $G = (V, E)$ by running a maximum-flow algorithm on at most $|V|$ flow networks, each having $O(V)$ vertices and $O(E)$ edges.

Use each $v$ as the source, find the minimum minimum cut.

### 26.2-12

> Suppose that you are given a flow network $G$, and $G$ has edges entering the source $s$. Let $f$ be a flow in $G$ in which one of the edges $(v, s)$ entering the source has $f(v, s) = 1$. Prove that there must exist another flow $f'$ with $f'(v, s) = 0$ such that $|f|=|f'|$. Give an $O(E)$-time algorithm to compute $f'$, given $f$, and assuming that all edge capacities are integers.

### 26.2-13

> Suppose that you wish to find, among all minimum cuts in a flow network $G$ with integral capacities, one that contains the smallest number of edges. Show how to modify the capacities of $G$ to create a new flow network $G'$ in which any minimum cut in $G'$ is a minimum cut with the smallest number of edges in $G$.
