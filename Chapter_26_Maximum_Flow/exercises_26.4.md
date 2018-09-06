## 26.4 Push-relabel algorithms

### 26.4-1

> Prove that, after the procedure INITIALIZE-PREFLOW$(G, S)$ terminates, we have $s.e \le -|f^*|$, where $f^*$ is a maximum flow for $G$.

### 26.4-2

> Show how to implement the generic push-relabel algorithm using $O(V)$ time per relabel operation, $O(1)$ time per push, and $O(1)$ time to select an applicable operation, for a total time of $O(V^2E)$.

### 26.4-3

> Prove that the generic push-relabel algorithm spends a total of only $O(VE)$ time in performing all the $O(V^2)$ relabel operations.

### 26.4-4

> Suppose that we have found a maximum flow in a flow network $G = (V, E)$ using a push-relabel algorithm. Give a fast algorithm to find a minimum cut in $G$.

### 26.4-5

> Give an efficient push-relabel algorithm to find a maximum matching in a bipartite graph. Analyze your algorithm.

### 26.4-6

> Suppose that all edge capacities in a flow network $G = (V, E)$ are in the set $\{ 1, 2, \dots, k \}$. Analyze the running time of the generic push-relabel algorithm in terms of $|V|$, $|E|$, and $k$. (Hint: How many times can each edge support a nonsaturating push before it becomes saturated?)

### 26.4-7

> Show that we could change line 6 of INITIALIZE-PREFLOW to 
> 
> `6  s.h = |G.V| - 2` 
> 
> without affecting the correctness or asymptotic performance of the generic pushrelabel algorithm.

### 26.4-8

> Let $\delta_f(u, v)$ be the distance (number of edges) from $u$ to $v$ in the residual network $G_f$. Show that the GENERIC-PUSH-RELABEL procedure maintains the properties that $u.h < |V|$ implies $u.h \le \delta_f(u, t)$ and that $u.h \ge |V|$ implies $u.h - |V| \le \delta_f(u, s)$.

### 26.4-9 $\star$

> As in the previous exercise, let $\delta_f(u, v)$ be the distance from $u$ to $v$ in the residual network $G_f$. Show how to modify the generic push-relabel algorithm to maintain the property that $u.h < |V|$ implies $u.h = \delta_f(u, t)$ and that $u.h \ge |V|$ implies $u.h - |V| = \delta_f(u, s)$. The total time that your implementation dedicates to maintaining this property should be $O(VE)$.

### 26.4-10

> Show that the number of nonsaturating pushes executed by the GENERIC-PUSH-RELABEL procedure on a flow network $G = (V, E)$ is at most $4|V|^2|E|$ for $|V| \ge 4$.
