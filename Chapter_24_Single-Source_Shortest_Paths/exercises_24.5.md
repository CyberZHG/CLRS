## 24.5 Proofs of shortest-paths properties

### 24.5-1

> Give two shortest-paths trees for the directed graph of Figure 24.2 (on page 648) other than the two shown.

### 24.5-2

> Give an example of a weighted, directed graph $G = (V, E)$ with weight function $w: E \rightarrow \mathbb{R}$ and source vertex $s$ such that $G$ satisfies the following property: For every edge $(u, v) \in E$, there is a shortest-paths tree rooted at $s$ that contains $(u, v)$ and another shortest-paths tree rooted at $s$ that does not contain $(u, v)$.

### 24.5-3

> Embellish the proof of Lemma 24.10 to handle cases in which shortest-path weights are $\infty$ or $-\infty$.

### 24.5-4

> Let $G = (V, E)$ be a weighted, directed graph with source vertex $s$, and let $G$ be initialized by INITIALIZE-SINGLE-SOURCE$(G, s)$. Prove that if a sequence of relaxation steps sets $s.\pi$ to a non-NIL value, then $G$ contains a negative-weight cycle.

### 24.5-5

> Let $G = (V, E)$ be a weighted, directed graph with no negative-weight edges. Let $s \in V$ be the source vertex, and suppose that we allow $v.\pi$ to be the predecessor of $v$ on any shortest path to $v$ from source $s$ if $v \in V - \{s\}$ is reachable from $s$, and NIL otherwise. Give an example of such a graph $G$ and an assignment of $\pi$ values that produces a cycle in $G_\pi$. (By Lemma 24.16, such an assignment cannot be produced by a sequence of relaxation steps.)

### 24.5-6

> Let $G = (V, E)$ be a weighted, directed graph with weight function $w: E \rightarrow \mathbb{R}$ and no negative-weight cycles. Let $s \in V$ be the source vertex, and let $G$ be initialized by INITIALIZE-SINGLE-SOURCE$(G, s)$. Prove that for every vertex $v \in V_\pi$, there exists a path from $s$ to $v$ in $G_\pi$ and that this property is maintained as an invariant over any sequence of relaxations.

### 24.5-7

> Let $G = (V, E)$ be a weighted, directed graph that contains no negative-weight cycles. Let $s \in V$ be the source vertex, and let $G$ be initialized by INITIALIZESINGLE- SOURCE$(G, s)$. Prove that there exists a sequence of $|V| - 1$ relaxation steps that produces $v.d = \delta(s, v)$ for all $v \in V$.

### 24.5-8

> Let $G$ be an arbitrary weighted, directed graph with a negative-weight cycle reachable from the source vertex $s$. Show how to construct an infinite sequence of relaxations of the edges of $G$ such that every relaxation causes a shortest-path estimate to change.
