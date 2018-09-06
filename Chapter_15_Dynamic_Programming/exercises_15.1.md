## 15.1 Rod cutting

### 15.1-1

> Show that equation (15.4) follows from equation (15.3) and the initial condition $T(0) = 1$.

For $n=0$, $T(0) = 2^0 = 1$.

Suppose $T(i) = 2^i$ for $i$ in $[0, n - 1]$, then
$$
T(n) = 1 + \sum\_{j=0}^{n-1} T(j) = 1 + 1 + 2 + 2^2 + \cdots + 2^{n-1} = 2^n - 1 + 1 = 2^n
$$
### 15.1-2

> Show, by means of a counterexample, that the following "greedy" strategy does not always determine an optimal way to cut rods. Define the density of a rod of length $i$ to be $p\_i/i$, that is, its value per inch. The greedy strategy for a rod of length $n$ cuts off a first piece of length $i$, where $1 \le i \le n$, having maximum density. It then continues by applying the greedy strategy to the remaining piece of length $n - i$ .

Suppose $p\_1  = 1, p\_2 = 8, p\_3 = 14, p\_4 = 0$, the densities $p\_1 / 1 = 1, p\_2 / 4 = 2, p\_3 / 3 = 4 \frac{2}{3}$, for $n=4$, the greedy result is $3$ and $1$, the total value if $15$, and the dynamic programming solution is $2$ and $2$, which is $16$.

### 15.1-3

> Consider a modification of the rod-cutting problem in which, in addition to a price $p\_i$ for each rod, each cut incurs a fixed cost of $c$. The revenue associated with a solution is now the sum of the prices of the pieces minus the costs of making the cuts. Give a dynamic-programming algorithm to solve this modified problem.

$r\_n = \max(\max\_{1 \le i \le {n - 1}} (p\_i + r\_{n-i}) - c, p\_n)$

```python
def cut_rod(p, n, c):
    r = [0 for _ in xrange(n + 1)]
    for j in range(1, n + 1):
        r[j] = p[j]
        for i in range(1, j):
            r[j] = max(r[j], p[i] + r[j - i] - c)
    return r[n]
```

### 15.1-4

> Modify MEMOIZED-CUT-ROD to return not only the value but the actual solution, too.

```python
def cut_rod_sub(p, n, r, s):
    if r[n] >= 0:
        return r[n]
    r[n] = 0
    for i in range(1, n + 1):
        ret = p[i] + cut_rod_sub(p, n - i, r, s)
        if r[n] < ret:
            r[n] = ret
            s[n] = i
    return r[n]


def cut_rod(p, n):
    r = [-1 for _ in xrange(n + 1)]
    s = [i for i in xrange(n + 1)]
    cut_rod_sub(p, n, r, s)
    r = r[n]
    subs = []
    while n > 0:
        subs.append(s[n])
        n -= s[n]
    return r, subs
```

### 15.1-5

> The Fibonacci numbers are defined by recurrence (3.22). Give an $O(n)$-time dynamic-programming algorithm to compute the nth Fibonacci number. Draw the subproblem graph. How many vertices and edges are in the graph?

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(1, n):
        c = a + b
        a, b = b, c
    return c
```
