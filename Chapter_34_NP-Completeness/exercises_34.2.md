## 34.2 Polynomial-time verification

### 34.2-1

> Consider the language GRAPH-ISOMORPHISM $ = \\{ \langle G\_1, G\_2 \rangle : G\_1$ and $G\_2$ are isomorphic graphs$\\}$. Prove that GRAPH-ISOMORPHISM $\in$ NP by describing a polynomial-time algorithm to verfify the language.

The certificate should be a mapping $f$ that maps $u\_1 \in G\_1$ to $u\_2 \in G\_2$, which could be an array and the mapping takes $O(1)$ time in a random-access machine.

For any $u\_1, v\_1 \in G\_1$ if there exists an edge in $G\_1$ between $u\_1$ and $v\_1$, then there must exist an edge in $G\_2$ that connects $u\_2 = f(u\_1) \in G\_2$ and $v\_2 = f(v\_1) \in G\_2$, and vice versa.

### 34.2-3

> Show that if HAM-CYCLE $\in$ P, then the problem of listing the vertices of a hamiltonian cycle, in order, is polynomial-time solvable.

For every vertex $u \in V$, let $E\_u$ be the set of edges that connects to $u$, enumerate two edges $e\_1, e\_2 \in E\_u$ until HAM-CYCLE$(\langle G' = (V, (E - E\_u) \cup \\{e\_1, e\_2\\}) \rangle) = 1$ and keep only these two edges (since there exists a hamiltonian cycle that uses the two edges). After removing the edges we can get the order by running a DFS from any vertex.

### 34.2-4

> Prove that the class NP of languages is closed under union, intersection, concatenation, and Kleene star. Discuss the closure of NP under complement.

* Union

```
IF A_1(x, y) == 1 || A_2(x, y) == 1
THEN RETURN TRUE
ELSE RETURN FALSE
```

* Intersection

```
IF A_1(x, y) == 1 && A_2(x, y) == 1
THEN RETURN TRUE
ELSE RETURN FALSE
```

* Concatenation

```
FOR i = 1 .. n
    FOR j = 1 .. m
    IF A_1(x_1 ... x_i, y_1 ... y_j) == 1 && A_2(x_i+1 ... x_n, y_j+1 ... y_m) == 1
    THEN RETURN 1
RETURN 0
```

* Kleene star

```
IF x == epsilon
THEN RETURN 1

FOR i = 1 .. n
    FOR j = 1 .. m
        DP[i, j] = 0
DP[0, 0] = 1
FOR i = 0 .. n
    FOR j = 0 .. m
        FOR k = i + 1 .. n
            FOR l = j + 1 .. m
        IF A_1(x_i ... x_k, y_j .. y_l) == 1
        THEN DP[k, l] = 1
RETURN DP[n, m]
```

### 34.2-5

> Show that any language in NP can be decided by an algorithm running in time $2^{O(n^k)}$ for some constant $k$.

```
FOR all possible y
    IF A(x, y) == 1
    THEN RETURN 1
RETURN 0
```

### 34.2-6

> A __hamiltonian path__ in a graph is a simple path that visits every vertex exactly once. Show that the language HAM-PATH$=\{\langle G, u, v \rangle:$ there is a hamiltonian path from $u$ to $v$ in graph $G\\}$ belongs to NP.

Suppose $G = (V, E)$ and the certificate is the sequence of vertices $\\{v\_1, \dots v\_n\\}$, then we should verify:

* $ n = |G| $
* $ v\_1 = u $
* $ v\_n = v $
* $ \forall i \in \\{1, \dots, n\\}, v\_i \in V $
* $ \forall i \in \\{1, \dots, n - 1\\}, j \in \\{i + 1, \dots, n\\}, v\_i \ne v\_j $
* $ \forall i \in \\{1, \dots, n - 1\\}, (v\_i, v\_{i+1}) \in E $

### 34.2-7

> Show that the hamiltonian-path problem from Exercise 34.2-6 can be solved in polynomial time on directed acyclic graphs. Give an efficient algorithm for the problem.

Find the longest path from $u$ to $v$. It is a hamniltonian-path if the length of the path is $|V|$.

### 34.2-8

> Let $\phi$ be a boolean formula constructed from the boolean input variables $x\_1, x\_2, \dots, x\_k$, negations($\neg$), ANDs($\wedge$), ORs($\vee$), and parentheses. The formula $\phi$ is a __tautology__ if it evaluates to 1 for every assignment of 1 and 0 to the input varibales. Define TAUTOLOGY as the lanuage of boolean formulas that are tautologies. Show that TAUTOLOGY $\in$ co-NP.

The certificate is a set of assignments of 0s and 1s to $x$s. Since it takes $O(n)$ to verify $\overline{\text{TAUTOLOGY}}$ by substituting and evaluating the formula and checking whether the result equals to 0, therefore $\overline{\text{TAUTOLOGY}}$ $\in$ NP and TAUTOLOGY $\in$ co-NP.

### 34.2-9

> Prove that $\text{P} \subseteq \text{co-NP}$.

$\text{P} \subseteq \text{NP}$ (ingores any certificate)

$\overline{\text{P}} \subseteq \text{NP}$ (exercise 34.1-6)

$\text{P} \subseteq \text{co-NP}$

### 34.2-10

> Prove that if $\text{NP} \ne \text{co-NP}$, then $\text{P} \ne \text{NP}$.

Prove the contrapositive.

Suppose $\text{P} = \text{NP}$:

* $\forall L \in \text{NP}$ $\Rightarrow$ $L \in \text{P}$ $\Rightarrow$ $\overline{L} \in \text{P}$ $\Rightarrow$ $L \in \text{co-NP}$
* $\forall L \in \text{co-NP}$ $\Rightarrow$ $\overline{L} \in \text{NP}$ $\Rightarrow$ $\overline{L} \in \text{P}$ $\Rightarrow$ $L \in \text{P}$
*  $\Rightarrow$ $\text{NP} = \text{co-NP}$.

### 34.2-11

> Let $G$ be a connected, undirected graph with at least 3 vertices, and let $G^3$ be the graph obtained by connecting all pairs of vertices that are connected by a path in $G$ of length at most 3. Prove that $G^3$ is hamiltonian.

Let $T$ be a spanning tree of $G$, since $T$ has fewer edges than $G$, therefore $T^3$ is hamiltonian $\Rightarrow$ $G^3$ is hamiltonian.

We can prove $T^3$ is hamiltonian by induction:

For $|V| = 3$, any permutation forms a hamilton cycle and all edges are used.

Suppose $T^3$ is hamiltonian for $|V| < n$, and $u$, $v$ are two vertices connected by an edge $e$ in a $T$ that $|V| = n$.
Suppose $u$ and $v$ already belong to two different spanning trees $T\_u$ and $T\_v$, $|T\_u.V| + |T\_v.V| = n$. We may assume, with loss of generality, that $|T\_u.V| \ge 3$. Denote one of the vertices connected to $u$ in $T\_u$ by $u'$ and one of the vertices connected to $v$ in $T\_v$ by $v'$. And through the following constructions we can see there would always exist a hamilton cycle that uses the edge $(u', u)$ ($(\dots, u, v, \dots)$ will always be in the hamilton cycle in the construction).

* $|T\_v.V| = 1$

The distance between $u'$ and $v$ is 2, thus there is an edge $(u', v)$ and we can modity the hamilton cycle in $T\_u$ from $(\dots, u', u, \dots)$ to $(\dots, u', v, u, \dots)$.

* $|T\_v.V| = 2$

The distancce between $u'$ and $v'$ is 3, thus there is an edge $(u', v')$ and we can modify the hamilton cycle in $T\_u$ and $T\_v$ from $(\dots, u', u, \dots)$ to $(\dots, u', v', v, u, \dots)$.

* $|T\_v.V| \ge 3$

Same as $|T\_v.V| \ge 2$, we can modify the hamilton cycle in $T\_u$ and $T\_v$ from $(\dots, u', u, \dots)$ and $(\dots, v', v, \dots)$ to $(\dots, u', v', \dots, v, u, \dots)$. 
