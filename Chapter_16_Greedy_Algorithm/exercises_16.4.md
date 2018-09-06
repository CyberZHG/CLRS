## 16.4 Matroids and greedy methods

### 16.4-1

> Show that $(S, I\_k)$ is a matroid, where $S$ is any finite set and $I\_k$ is the set of all subsets of $S$ of size at most $k$, where $k \le |S|$.

### 16.4-2 $\star$

> Given an $m \times n$ matrix $T$ over some field (such as the reals), show that $(S, I)$ is a matroid, where $S$ is the set of columns of $T$ and $A \in I$ if and only if the columns in $A$ are linearly independent.

### 16.4-3 $\star$

> Show that if $(S, I)$ is a matroid, then $(S, I')$ is a matroid, where

> $I' = \{ A': S - A'$ contains some maximal $A \in I \}$.

> That is, the maximal independent sets of $(S, I')$ are just the complements of the maximal independent sets of $(S, I)$.

### 16.4-4 $\star$

> Let $S$ be a finite set and let $S\_1, S\_2, \dots, S\_k$ be a partition of $S$ into nonempty disjoint subsets. Define the structure $(S, I)$ by the condition that $I = \{ A : | A \cap S\_i | \le 1$ for $i = 1, 2, \dots, k \}$. Show that $(S, I)$ is a matroid. That is, the set of all sets $A$ that contain at most one member of each subset in the partition determines the independent sets of a matroid.

### 16.4-5

> Show how to transform the weight function of a weighted matroid problem, where the desired optimal solution is a _minimum-weight_ maximal independent subset, to make it a standard weighted-matroid problem. Argue carefully that your transformation is correct.
