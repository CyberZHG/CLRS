## 21.4 Analysis of union by rank with path compression

### 21.4-1

> Prove Lemma 21.4.

Obviously.

### 21.4-2

> Prove that every node has rank at most $$\lfloor \lg n\rfloor$$.

The rank increases by 1 only when $$x.rank = y.rank$$, thus each time we need the twice number of elements to increase the rank by 1, therefore the rank is at most $$\lfloor \lg n \rfloor$$.

### 21.4-3

> In light of Exercise 21.4-2, how many bits are necessary to store $$x.rank$$ for each node $$x$$?

$$\lceil \lfloor \lg n \rfloor \rceil$$.

### 21.4-4

> Using Exercise 21.4-2, give a simple proof that operations on a disjoint-set forest with union by rank but without path compression run in $$O(m\lg n)$$ time.

$$O((m - x) \cdot \lfloor \lg n \rfloor) = O(m \lg n)$$.

### 21.4-5

> Professor Dante reasons that because node ranks increase strictly along a simple path to the root, node levels must monotonically increase along the path. In other words, if $$x.rank > 0$$ and $$x.p$$ is not a root, then level($$x$$) $$\le$$ level$$(x.p)$$. Is the professor correct?

No. Think about an extreme condition $$100 \rightarrow 99 \rightarrow 1$$, since level$$(99) = 0$$, level$$(1) \ge 1$$, we have level$$(x)$$ $$>$$ level$$(x.p)$$.

### 21.4-6 $$\star$$

> Consider the function $$\alpha'(n) = \min \{k: A_k(1) \ge \lg(n + 1)\}$$. Show that $$\alpha'(n) \le 3$$ for all practical values of $$n$$ and, using Exercise 21.4-2, show how to modify the potential-function argument to prove that we can perform a sequence of $$m$$ MAKESET, UNION, and FIND-SET operations, $$n$$ of which are MAKE-SET operations, on a disjoint-set forest with union by rank and path compression in worst-case time $$O(m \alpha'(n))$$.

