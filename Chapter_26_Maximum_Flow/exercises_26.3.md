## 26.3 Maximum bipartite matching

### 26.3-1

> Run the Ford-Fulkerson algorithm on the flow network in Figure 26.8(c) and show the residual network after each flow augmentation. Number the vertices in $L$ top to bottom from 1 to 5 and in $R$ top to bottom from 6 to 9. For each iteration, pick the augmenting path that is lexicographically smallest.

### 26.3-2

> Prove Theorem 26.10.

### 26.3-3

> Let $G = (V, E)$ be a bipartite graph with vertex partition $V = L \cup R$, and let $G'$ be its corresponding flow network. Give a good upper bound on the length of any augmenting path found in $G'$ during the execution of FORD-FULKERSON.

### 26.3-4 $\star$

> A __*perfect matching*__ is a matching in which every vertex is matched. Let $G = (V, E)$ be an undirected bipartite graph with vertex partition $V = L \cup R$, where $|L| = |R|$. For any $X \subseteq V$, define the __*neighborhood*__ of $X$ as
> 
> $N(X) = \{ y \in V: (x, y) \in E ~\text{for some}~ x \in X \}$,
> 
> that is, the set of vertices adjacent to some member of $X$. Prove __*Hall's theorem*__: there exists a perfect matching in $G$ if and only if $|A| \le |N(A)|$ for every subset $A \subseteq L$.

### 26.3-5 $\star$

> We say that a bipartite graph $G = (V, E)$, where $V = L \cup R$, is __*d-regular*__ if every vertex $v \in V$ has degree exactly $d$. Every $d$-regular bipartite graph has $|L| = |R|$. Prove that every $d$-regular bipartite graph has a matching of cardinality $|L|$ by arguing that a minimum cut of the corresponding flow network has capacity $|L|$.
