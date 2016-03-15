## Problems

### 23-1 Second-best minimum spanning tree

> Let $$G = (V, E)$$ be an undirected, connected graph whose weight function is $$w: E \rightarrow \mathbb{R}$$, and suppose that $$|E| \ge |V|$$ and all edge weights are distinct.

> We define a second-best minimum spanning tree as follows. Let $$\mathcal{T}$$ be the set of all spanning trees of $$G$$, and let $$T'$$ be a minimum spanning tree of $$G$$. Then a __*second-best minimum spanning tree*__ is a spanning tree $$T$$ such that $$W(T) = \min_{T'' \in \mathcal{T}-\{T'\}}\{w(T'')\}$$.

> __*a*__. Show that the minimum spanning tree is unique, but that the second-best minimum spanning tree need not be unique.

> __*b*__. Let $$T$$ be the minimum spanning tree of $$G$$. Prove that $$G$$ contains edges $$(u, v) \in T$$ and $$(x, y) \notin T$$ such that $$T - \{(u, v)\} \cup \{(x, y)\}$$ is a second-best minimum spanning tree of $$G$$.

> __*c*__. Let $$T$$ be a spanning tree of $$G$$ and, for any two verticces $$u, v \in V$$, let $$max[u,v]$$ denote an edge of maximum weight on the unique simple path between $$u$$ and $$v$$ in $$T$$. Describe an $$O(V^2)$$-time algorithm that, given $$T$$, computes $$max[u, v]$$ for all $$u, v \in V$$.

> __*d*__. Give an efficient algorithm to compute the second-best minimum spanning tree of $$G$$.


