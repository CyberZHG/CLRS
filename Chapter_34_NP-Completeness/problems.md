## Problems

### 34-1 Independent set

> An __*independent set*__ of a graph $G = (V, E)$ is a subset $V' \subseteq V$ of vertices such that each edge in $E$ is incident on at most one vertex in $V'$. The __*independent-set problem*__ is to find a maximum-size independent set in $G$.

> __*a*__. Formulate a related decision problem for the independent-set problem, and prove that it is NP-complete. (Hint: Reduce from the clique problem.)

__Decision problem:__

The independent set in $G$ is at most $k$.

__ISP $\in$ NP__:

The certificate is a set of vertices $V'$. To verify the certificate, for each $u, v \in V'$, we should verify that $(u, v) \notin E$.

__ISP is NP-hard to CLIQUE $\Rightarrow$ ISP $\in$ NPC:__

_Construction:_

Suppose the complement graph of $G$ is $G'$, then $G$ for CLIQUE is equivalent to $G'$ for ISP.

_CLIQUE $\Rightarrow$ ISP:_

Suppose there exists a clique $C$ of size $k$ in $G$, we know $\forall u, v \in C$, $(u, v) \in E$. Therefore in the complement graph $G'$, $\forall u, v \in C$, $(u, v) \notin E$.

_ISP $\Rightarrow$ CLIQUE:_

Suppose there exists an independent-set $C$ of size $k$ in $G'$, we know $\forall u, v \in C$, $(u, v) \notin E$. Therefore in the graph $G$, $\forall u, v \in C$, $(u, v) \in E$.

> __*b*__. Suppose that you are given a "black-box" subroutine to solve the decision problem you defined in part (a). Give an algorithm to find an independent set of maximum size. The running time of your algorithm should be polynomial in $|V|$ and $|E|$, counting queries to the black box as a single step.

```
FOR k = |V| .. 1
    IF ISP(G, k)
    THEN RETURN k
RETURN 0
```

> Although the independent-set decision problem is NP-complete, certain special cases are polynomial-time solvable.

> __*c*__. Give an efficient algorithm to solve the independent-set problem when each vertex in $G$ has degree 2. Analyze the running time, and prove that your algorithm works correctly.

The graph is a set of chains and simple cycles.

```python
def isp_in_deg_2(graph):
    n = len(graph)
    color = [0 for _ in range(n)]

    def search(u):
        if color[u] != 0:
            return
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1:
                color[u] = -1
                break
        for v in graph[u]:
            search(v)

    for u in range(n):
        if len(graph[u]) == 1:
            search(u)
    for u in range(n):
        if color[u] == 0:
            search(u)

    return len(filter(lambda x: x == 1, color))
```

Runs in $O(|V||E|)$ time.

> __*d*__. Give an efficient algorithm to solve the independent-set problem when $G$ is bipartite. Analyze the running time, and prove that your algorithm works correctly. (Hint: Use the results of Section 26.3.)

See Kőnig's theorem.

In bipartite graph, all nodes that are not in the minimum vertex cover can be included in maximum independent set, the number of edges in a maximum matching is equal to the number of vertices in a minimum vertex cover.

### 34-2 Bonnie and Clyde

> Bonnie and Clyde have just robbed a bank. They have a bag of money and want to divide it up. For each of the following scenarios, either give a polynomial-time algorithm, or prove that the problem is NP-complete. The input in each case is a list of the $n$ items in the bag, along with the value of each.

> __*a*__. The bag contains $n$ coins, but only 2 different denominations: some coins are worth $x$ dollars, and some are worth $y$ dollars. Bonnie and Clyde wish to divide the money exactly evenly.

Suppose the there are $n\_x$ coins with value $x$ and $n\_y$ coins with value $y$, then the total value $s = n\_x \cdot x + n\_y \cdot y$. We need to find $a$ and $b$ such that $ax + by = s / 2$, the equation has integer solutions when $s$ is even and $\text{gcd}(x, y) \~|\~ s / 2$. We can find a solution $a\_0$ and $b\_0$ with extended Euclidean algorithm in $O(\log n)$ (with a compact encoding, the running time is linear to the input). Then we need to solve the inequations and find a valid integer $t$:

$$
\left \\{
\begin{array}{rcccl}
0 &\le& \displaystyle \frac{a\_{0} \cdot s}{2 \cdot \text{gcd}(x, y)} + \frac{y}{\text{gcd}(x, y)} \cdot t &\le& n\_x \\\\
0 &\le& \displaystyle \frac{b\_{0} \cdot s}{2 \cdot \text{gcd}(x, y)} - \frac{x}{\text{gcd}(x, y)} \cdot t &\le& n\_y \\\\
\end{array}
\right .
$$

```python
def divide_a(nx, x, ny, y):
    s = nx * x + ny * y
    if s % 2 == 1:
        return -1, -1
    s //= 2

    def ext_gcd(x, y):
        if y == 0:
            return x, 1, 0
        g, b, a = ext_gcd(y, x % y)
        return g, a, b - (x // y) * a

    g, a, b = ext_gcd(x, y)
    if s % g != 0:
        return -1, -1
    x, y, s = x // g, y // g, s // g
    a, b = a * s, b * s
    lx, rx = (-a + (y - 1)) // y, (nx - a) // y
    ly, ry = (b - ny + (x - 1)) // x, b // x
    if max(lx, ly) > min(rx, ry):
        return -1, -1
    t = max(lx, ly)
    return a + y * t, b - x * t
```

> __*b*__. The bag contains $n$ coins, with an arbitrary number of different denominations, but each denomination is a nonnegative integer power of 2, i.e., the possible denominations are 1 dollar, 2 dollars, 4 dollars, etc. Bonnie and Clyde wish to divide the money exactly evenly.

```python
import copy


def divide_b(nums):
    """
    :param nums: nums[i] means there are nums[i] coins with value 2^i
    """
    n = len(nums)
    nums = copy.copy(nums)
    powers = [2 ** i for i in range(n)]
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    sum_a, sum_b = 0, 0
    i = n - 1
    while i >= 0:
        if nums[i] == 0:
            i -= 1
            continue
        if sum_a == sum_b:
            if nums[i] > 1:
                num = nums[i] // 2
                a[i] += num
                b[i] += num
                sum_a += num * powers[i]
                sum_b = sum_a
                nums[i] %= 2
            else:
                a[i] += 1
                sum_a += powers[i]
                nums[i] -= 1
        else:
            num = min(nums[i], (sum_a - sum_b) // powers[i])
            b[i] += num
            sum_b += num * powers[i]
            nums[i] -= num
    if sum_a == sum_b:
        return a, b
    return None, None
```

> __*c*__. The bag contains $n$ checks, which are, in an amazing coincidence, made out to "Bonnie or Clyde". They wish to divide the checks so that they each get the exact same amount of money.

Equivalent to set-partition problems.

> __*d*__. The bag contains $n$ checks as in part (c), but this time Bonnie and Clyde are willing to accept a split in which the difference is no larger than 100 dollars.

The problem is NP since we can verify the difference in polynomial time. We can prove the problem is NP-hard to set partition problem by multiply the sets in set-partition problem by 101. If set-partition problem has a solution, the difference is exactly 0 in this problem; if this problem has a solution, the difference must be a multiple of 101 and the only value satisfies this constrain is 0. Therefore the problem is NP-complete.

### 34-3 Graph coloring

> Mapmakers try to use as few colors as possible when coloring countries on a map, as long as no two countries that share a border have the same color. We can model this problem with an undirected graph $G = (V, E)$ in which each vertex represents a country and vertices whose respective countries share a border are adjacent. Then, a __*k-coloring*__ is a function $c$ : $V \rightarrow \\{ 1, 2, \dots, k \\}$ such that $c(u) \ne c(v)$ for every edge $(u, v) \in E$. In other words, the numbers $1, 2, \dots, k$ represent the $k$ colors, and adjacent vertices must have different colors. The __*graph-coloring problem*__ is to determine the minimum number of colors needed to color a given graph.

> __*a*__. Give an efficient algorithm to determine a 2-coloring of a graph, if one exists.

```python
def graph_coloring_2(graph):
    n = len(graph)
    color = [-1 for _ in range(n)]

    def search(u, c):
        if color[u] != -1:
            return
        color[u] = c
        for v in graph[u]:
            if color[v] == -1:
                if not search(v, 1 - c):
                    return False
            elif color[v] == c:
                return False
        return True

    for u in range(n):
        if color[u] == -1:
            if not search(u, 0):
                return False

    return color
```

> __*b*__. Cast the graph-coloring problem as a decision problem. Show that your decision problem is solvable in polynomial time if and only if the graph-coloring problem is solvable in polynomial time.

Decision problem: whether there exists a coloring of the graph with at most $k$ colors.

Decision $\rightarrow$ graph-coloring: the first $k$ from 1 to $|V|$ that satisfies the decision problem.

Graph coloring $\rightarrow$ decision: suppose the minimum number of colors is $k'$, then check whether $k \ge k'$.

> __*c*__. Let the language 3-COLOR be the set of graphs that can be 3-colored. Show that if 3-COLOR is NP-complete, then your decision problem from part (b) is NP-complete.

__GCP $\in$ NP:__

Verify for each color $c(u)$ that $c(u) \in \\{ 1, 2, \dots, k \\}$ and for each $(u, v) \in E$ that $c(u) \ne c(v)$.

__3-COLOR $\le\_\text{P}$ GCP:__

A special case in GCP with $k = 3$.

> To prove that 3-COLOR is NP-complete, we use a reduction from 3-CNF-SAT. Given a formula $\phi$ of $m$ clauses on $n$ variables $x\_1, x\_2, \dots, x\_n$, we construct a graph $G = (V, E)$ as follows. The set $V$ consists of a vertex for each variable, a vertex for the negation of each variable, 5 vertices for each clause, and 3 special vertices: $\text{TRUE}$, $\text{FALSE}$, and $\text{RED}$. The edges of the graph are of two types: "literal" edges that are independent of the clauses and "clause" edges that depend on the clauses. The literal edges form a triangle on the special vertices and also form a triangle on $x\_i$ , $\neg x\_i$, and $\text{RED}$ for $i = 1, 2, \dots, n$.

> __*d*__. Argue that in any 3-coloring $c$ of a graph containing the literal edges, exactly one of a variable and its negation is colored $c(\text{TRUE})$ and the other is colored $c(\text{FALSE})$. Argue that for any truth assignment for $\phi$, there exists a 3-coloring of the graph containing just the literal edges.

Since there is a triangle on $x\_i$ , $\neg x\_i$, and $\text{RED}$, neither $x\_i$ or $\neg x\_i$ could be RED since they connect to RED, and they couldn't be the same color since they are connected. Therefore no matter what color we choose for each variable, there will always exists a 3-coloring of the graph containing just the literal edges.

> The widget shown in Figure 34.20 helps to enforce the condition corresponding to a clause $(x \vee y \vee z)$. Each clause requires a unique copy of the 5 vertices that are heavily shaded in the figure; they connect as shown to the literals of the clause and the special vertex TRUE.

> __*e*__. Argue that if each of $x$, $y$, and $z$ is colored $c(\text{TRUE})$ or $c(\text{FALSE})$, then the widget is 3-colorable if and only if at least one of $x$, $y$, and $z$ is colored $c(\text{TRUE})$.

Just enumerate all the possibilities.

> __*f*__. Complete the proof that 3-COLOR is NP-complete.

3-CNF-SAT $\Rightarrow$ 3-COLOR: the clauses are evaluates to TRUE and each variable is either TRUE or FALSE.

3-COLOR $\Rightarrow$ 3-CNT-SAT: use the color as the truth value of each variable.

### 34-4 Scheduling with profits and deadlines

> Suppose that we have one machine and a set of $n$ tasks $a\_1, a\_2, \dots, a\_n$, each of which requires time on the machine. Each task $a\_j$ requires $t\_j$ time units on the machine (its processing time), yields a profit of $p\_j$ , and has a deadline $d\_j$. The machine can process only one task at a time, and task $a\_j$ must run without interruption for $t\_j$ consecutive time units. If we complete task $a\_j$ by its deadline $d\_j$, we receive a profit $p\_j$ , but if we complete it after its deadline, we receive no profit. As an optimization problem, we are given the processing times, profits, and deadlines for a set of n tasks, and we wish to find a schedule that completes all the tasks and returns the greatest amount of profit. The processing times, profits, and deadlines are all nonnegative numbers.

> __*a*__. State this problem as a decision problem.

Whether there exists a schedule that completes all the tasks and has a profit of at least $k$.

> __*b*__. Show that the decision problem is NP-complete.

__SCHEDULE $\in$ NP:__

The cerificate $s\_1, s\_2, \dots, s\_n$ is a list of indices of tasks, we need to verify:

* $\forall s\_i$, $s\_i \in \\{ 1, 2, \dots, n \\}$,
* $\forall s\_i, s\_j$, $s\_i \ne s\_j$,
* $\displaystyle \sum\_{i \in \\{ 1, 2, \dots, n \\}} p\_{s\_i} \cdot \left [ \left ( \sum\_{j \in \\{ 1, 2, \dots, i - 1 \\}} t\_{s\_i} \right ) \le d\_{s\_i} \right ]$.

where $[ \cdot ]$ is the indicator funciton.

__SUBSET-SUM $\le\_\text{P}$ SCHEDULE:__

_Construction:_

For set $S$ and target $k$ in SUBSET-SUM, we construct $t\_i = S\_i$, $p\_i = S\_i$ and $d\_i = k$.

_SUBSET-SUM $\Rightarrow$ SCHEDULE:_

Suppose $S'$ is a solution for SUBSET-SUM, then in scheduling problem we first do $S'$ then do $\overline{S'}$.

_SCHEDULE $\Rightarrow$ SUBSET-SUM:_

The tasks can't gain profits after deadline, therefore the profits is less than or equal to $k$, then a solution must earn exactly $k$ profits since the solution has at least $k$ profits. The tasks done within deadline is a solution to SUBSET-SUM problem.

> __*c*__. Give a polynomial-time algorithm for the decision problem, assuming that all processing times are integers from $1$ to $n$. (Hint: Use dynamic programming.)

See __*d*__, suppose the result of the next problem is $k'$ then we could simply verify that $k' \ge k$.

> __*d*__. Give a polynomial-time algorithm for the optimization problem, assuming that all processing times are integers from $1$ to $n$.

```python
def schedule(t, p, d):
    k, n = 0, len(t)
    d, p, t = tuple(zip(*sorted(zip(d, p, t))))
    dp = [[0 for _ in range(n * n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n * n, 0, -1):
            dp[i][j] = dp[i - 1][j]
            if j - t[i - 1] >= 0:
                if j <= d[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]] + p[i - 1])
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - t[i - 1]])
            k = max(k, dp[i][j])
    return k
```