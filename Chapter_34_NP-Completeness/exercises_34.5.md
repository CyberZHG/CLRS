## 34.5 NP-complete problems

### 34.5-1

> The __*subgraph-isomorphism problem*__ takes two undirected graphs $G\_1$ and $G\_2$, and it asks whether $G\_1$ is isomorphic to a subgraph of $G\_2$. Show that the subgraph-isomorphism problem is NP-complete.

__Prove SIP $\in$ NP__

The certificate $C$ is a permutation of $[1, \dots, n]$, we need to check:

* $|V\_1| = |V\_2|$
* $|E\_1| = |E\_2|$
* for each pair of nodes $u\_i, v\_i \in V\_1$: $(u\_{C\_{u\_i}}, v\_{C\_{v\_i}}) \in E\_2$ if $(u\_i, v\_i) \in E\_1$
* for each pair of nodes $u\_i, v\_i \in V\_1$: $(u\_{C\_{u\_i}}, v\_{C\_{v\_i}}) \notin E\_2$ if $(u\_i, v\_i) \notin E\_1$

It takes $O(|V\_1|^2)$ time to verify the certificate, therefore subgraph-isomorphism problem $\in$ NP.

__Prove SIP $\in$ NPC by proving CLIQUE $\le\_\text{P}$ SIP__

*Construction:*

Suppose we want to check whether $G\_2$ contains a clique of size $k$. We can construct a complete graph $G\_1$ that has $k$ vertices, and check whether $G\_1$ is isomorphic to a subgraph of $G\_2$. The construction takes $O(|V|^2)$ time since $k \le |V|$ without the loss of generality.

*CLIQUE $\Rightarrow$ SIP:*

The clique is a subgraph of $G\_2$ and isomorphic to $G\_1$.

*SIP $\Rightarrow$ CLIQUE:*

A subgraph in $G\_2$ has $k$ vertices and is complete.

### 34.5-2

> Given an integer $m \times n$ matrix $A$ and an integer $m$-vector $b$, the __*0-1 integer-programming problem*__ asks whether there exists an integer $n$-vector $x$ with elements in the set $\\{0, 1\\}$ such that $Ax \le b$. Prove that 0-1 integer programming is NP-complete. (Hint: Reduce from 3-CNF-SAT.)

__Prove 0-1-IP $\in$ NP__

The certificate is $x$, we can calculate $Ax$ in $O(mn)$.

__Prove 0-1-IP $\in$ NPC by proving 3-CNT-SAT $\le\_\text{P}$ 0-1-IP__

_Construction:_

(To satisfy $x\_1 \vee \neg x\_2 \vee \neg x\_3$, we can convert it to $x\_1 + (1 - x\_2) + (1 - x\_3) \ge 1$ $\Rightarrow$ $-x\_1 + x\_2 + x\_3 \le 1$)

Suppose in 3-CNT-SAT the formula $\phi$ has $m$ clauses and $n$ variables. Construct a matrix $A$ of size $m \times n$, that for each clause $C\_i$:

* if $x\_j \in C\_i$, set $A\_{i, j} = -1$,
* if $\neg x\_j \in C\_i$, set $A\_{i, j} = 1$.

Construct a $m$-vector $b$ that:

* if there are $k$ $\neg$s in $C\_i$, set $b\_{i} = k - 1$.

The construction runs in $O(mn)$.

_3-CNT-SAT $\Rightarrow$ 0-1-IPP:_

Based on how we construct $A$ and $b$.

_0-1-IPP $\Rightarrow$ 3-CNT-SAT:_

By moving back 1s, at least one item in $C\_i$ must be 1.

### 34.5-3

> The __integer linear-programming problem__ is like the 0-1 integer-programming problem given in Exercise 34.5-2, except that the values of the vector $x$ may be any integers rather than just 0 or 1. Assuming that the 0-1 integer-programming problem is NP-hard, show that the integer linear-programming problem is NP-complete.

__Prove ILP $\in$ NP__

The certificate is $x$, we can calculate $Ax$ in $O(mn)$.

__Prove ILP $\in$ NPC by proving 0-1-IP $\le\_\text{P}$ ILP__

(Add constrains $0 \le x\_i \le 1$ $\Rightarrow$ $-x\_i \le 0$ and $x\_i \le 1$)

Suppose the original $A$ in 0-1-IP is of size $m \times n$, then the extended $A'$ is of size $(m + 2n) \times n$:

* if $i <= m$, $A'\_{i, j} = A\_{i, j}$,
* if $i > m$ and $i - m$ is even, $A\_{i, (i - m) / 2} = -1$,
* if $i > m$ and $i - m$ is odd, $A\_{i, (i - m - 1) / 2} = 1$.

The constructed $(m + 2n)$-vector $b'$:

* if $i <= m$, $b'\_{i} = b\_{i}$,
* if $i > m$ and $i - m$ is even, $b\_{i} = 0$,
* if $i > m$ and $i - m$ is odd, $b\_{i} = 1$.

The construction runs in $O(mn)$.

### 34.5-4

> Show how to solve the subset-sum problem in polynomial time if the target value $t$ is expressed in unary.

0-1 knapsack.

```
dp[0, .., t] = FALSE
dp[0] = TRUE
FOR s IN S
    FOR i IN [t, .., 0]
        IF dp[i - s] THEN
            dp[i] = TRUE
            BREAK
RETURN dp[t]
```

Runs in $O(|S|t)$, since $t$ is expressed in unary, the time complexity is a polynomial function of the input.

### 34.5-5

> The __*set-partition problem*__ takes as input a set $S$ of numbers. The question is whether the numbers can be partitioned into two sets $A$ and $\overline{A} = S - A$ such that $\sum\_{x \in A} x = \sum\_{x \in \overline{A}} x$. Show that the set-partition problem is NP-complete.

__Prove SPP $\in$ NP__

The certificate is $A$, just calculate the sum of $A$ and $\overline{A}$ and check whether the results are the same.

The verification runs in $O(|S|)$.

__Prove SPP $\in$ NPC by proving SUBSET-SUM $\le\_\text{P}$ SPP__

_Construction:_

Suppose the target is $t$ in SUBSET-SUM, the sum of $S$ is $s$, then $\sum\_{x \in A} x = t$, $\sum\_{x \in \overline{A}} x = s - t$. We construct $S' = S \cup \\{ |s - 2t| \\}$ for set-partition problem.

_SUBSET-SUM $\Rightarrow$ SPP:_

* if $t \le s - t$, we add $s - 2t$ to $A$, then $\sum\_{x \in A} x = t + s - 2t = s - t = \sum\_{x \in \overline{A}} x$,
* if $t > s - t$, we add $2t - s$ to $\overline{A}$, then $\sum\_{x \in \overline{A}} x = s - t + 2t - s = t = \sum\_{x \in A} x$.

_SPP $\Rightarrow$ SUBSET-SUM:_

* if $t \le s - t$, then the set contains $s - 2t$ is a solution for SUBSET-SUM after removing $s - 2t$,
* if $t > s - t$, suppose set $A$ containts $s - 2t$, then $\overline{A}$ is a solution for SUBSET-SUM.

### 34.5-6

> Show that the hamiltonian-path problem is NP-complete.

__Prove HAM-PATH $\in$ NP__

Given the vertices $(v\_1, \dots, v\_n)$ as certificate, verify in $O(|V|^2)$:

* $v\_1 = u$,
* $v\_n = v$,
* $v\_i \ne v\_j$ $\forall i, j \in [1, \dots, n]$,
* $(v\_i, v\_{i + 1}) \in E \forall i \in [1, \dots, n - 1]$.

__Prove HAM-PATH $\in$ NPC by proving HAM-CYCLE $\le\_\text{P}$ HAM-PATH__

_Construction:_

Choose a vertex $a$ arbitrarily, add a vertex $a'$ to the graph and $\forall (a, v\_i) \in E$ add edges $(a', v\_i)$. Add edge $(u, a)$ and $(v, a')$. The construction takes $O(V)$ time.

_HAM-CYCLE $\Rightarrow$ HAM-PATH:_

If there is a hamilton cycle in $G$, suppose the two vertices connects to $a$ are $c\_1$ and $c\_2$, then there is a hamilton path $(u, a, c\_1, \dots, c\_2, a', v)$.

_HAM-PATH $\Rightarrow$ HAM-CYCLE:_

If there is a hamilton path from $u$ to $v$, then there is a hamilton cycle by removing $u$, $v$ and $a'$.

### 34.5-7

> The __*longest-simple-cycle problem*__ is the problem of determining a simple cycle (no repeated vertices) of maximum length in a graph. Formulate a related decision problem, and show that the decision problem is NP-complete.

Decision problem: a simple cycle of size at most $k$.

__Prove LSC $\in$ NP__

Given the vertices $(v\_1, \dots, v\_n)$ as certificate, verify in $O(|V|^2)$:

* $v\_i \ne v\_j \forall i, j \in [1, \dots, n]$,
* $(v\_i, v\_{i + 1}) \in E$ $\forall i \in [1, \dots, n - 1]$,
* $(v\_n, v\_1) \in E$.

__Prove LSC $\in$ NPC by proving HAM-CYCLE $\le\_\text{P}$ LSC__

HAM-CYCLE is equivalent to solve LSC with $k = |V|$.

### 34.5-8

> In the __*half 3-CNF satisfiability problem*__, we are given a 3-CNF formula $\phi$ with $n$ variables and $m$ clauses, where $m$ is even. We wish to determine whether there exists a truth assignment to the variables of $\phi$ such that exactly half the clauses evaluate to 0 and exactly half the clauses evaluate to 1. Prove that the half 3-CNF satisfiability problem is NP-complete.

__Prove HALF-3-CNF-SAT $\in$ NP__

Evaluate in $O(n)$.

__Prove HALF-3-CNF-SAT $\in$ NPC by proving 3-CNF-SAT $\le\_\text{P}$ HALF-3-CNF-SAT__

_Construction:_

Suppose $p, q, r$ are variables not in $\phi$, we add $m$ clauses $(p \vee \neg p \vee q)$ which are always evaluated to 1 and $2m$ clauses  $(p \vee q \vee r)$. The construction takes $O(m)$ time and results in $4m$ clauses.

_3-CNT-SAT $\Rightarrow$ HALF-3-CNF-SAT:_

The original $\phi$ has $m$ clauses evaluate to 1, let $p = q = r = 0$, then there are $2m$ clauses evaluate to 0 and $2m$ clauses evaluate to 1.

_HALF-3-CNF-SAT $\Rightarrow$ 3-CNT-SAT:_

There is no solution if any one of $p, q, r$ is 1 since there will be at least $3m$ clauses evaluate to 1. Therefore the rest $m$ clauses in original $\phi$ must evaluate to 1.
