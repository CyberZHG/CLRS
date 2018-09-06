## 34.1 Polynomial time

### 34.1-1

> Define the optimization problem LONGEST-PATH-LENGTH as the relation that associates each instance of an undirected graph and two vertices with the number of edges in a longest simple path between the two vertices. Define the decision problem LONGEST-PATH $=\\{\langle G, u, v, k \rangle : G = (V, E)$ is an undirected graph, $u, v \in V$, $k \ge 0$ is an integer, and there exists a simple path from $u$ to $v$ in $G$ consisting of at least $k$ edges$\\}$. Show that the optimization problem LONGEST-PATH-LENGTH can be solved in polynomial time if and only if LONGEST-PATH $\in$ P.

* LONGEST-PATH-LENGTH can be solved in polynomial time $\Rightarrow$ LONGEST-PATH $\in$ P

Suppose it takes $O(n^k)$ time to determine that LONGEST-PATH-LENGTH is $k^\*$. For any $k \le k^\*$, LONGEST-PATH$(\langle G, u, v, k \rangle)=1$, otherwise LONGEST-PATH$(\langle G, u, v, k \rangle)=0$, which takes $O(n^k)$ time.

* LONGEST-PATH-LENGTH can be solved in polynomial time $\Leftarrow$ LONGEST-PATH $\in$ P 

Suppose LONGEST-PATH can be solved in $O(n^k)$ time. Enumerate $k \in [0, |V| - 1]$ to find the largest $k$ that LONGEST-PATH$(\langle G, u, v, k \rangle)=1$ takes $O(|V| \cdot n^k) = O(n^c \cdot n^k) = O(n^{ck})$ time, which is still polynomial, while the largest $k$ is the LONGEST-PATH-LENGTH.

### 34.1-2

> Give a formal definition for the problem of finding the longest simple cycle in an undirected graph. Give a related decision problem. Give the language corresponding to the decision problem.

* Formal definition

Instance: a graph $G$

Solutions: a seqeunce of vertices in the graph

Problem: find the simple cycle in $G$ which has the largest length $k$.

* Decision problem

If $i = \langle G, k \rangle$ is an instance of the decision problem CYCLE, then CYCLE$(i)=1$ if there exists a simple cycle whose length is at least $k$, and CYCLE$(i)=0$ otherwise.

* Language

$$
\begin{array}{rl}
\text{CYCLE} = \\{ \langle G, k \rangle: & G = (V, E) \text{ is an undirected graph}, \\\\
                           & k \ge 0 \text{ is an integer, and} \\\\
                           & \text{there exists a simple cycle in } G \text{ consisting of at least } k \text{ edges } \\}.
\end{array}
$$

### 34.1-3

> Give a formal encoding of directed graphs as binary strings using an adjacency-matrix representation. Do the same using an adjacency-list representation. Argue that the two representations are polynomially related.

* Adjacency-matrix

Suppose the matrix is $A$, then $A[u, v] = 1$ for any two vertices $u, v \in G = (V, E)$ there exists a path between them, otherwise $A[u, v] = 0$. The encoding is the concatenation of the binary encoded $|V|$ and all the values in the matrix.

* Adjacency-list

The head of the encoding is $|V|$, then for each $u$, encode $u$ and its out-degree $|u|$, then followed the $|u|$ $v$s that has a path between them.

* Polynomially related

matrix -> list: get column number
list -> matrix: fill 1s

### 34.1-4

> Is the dynamic-programming algorithm for the 0-1 knapsack problem that is asked for in Exercise 16.2-2 a polynomial-time algorithm? Explain your answer.

No. The algorithm runs in $O(nW)$ time. The concise encoding of $W$ has length $m = \lfloor \lg k \rfloor + 1$, therefore the algorithm is worse than $O(k) = O(2^m)$.

### 34.1-5

> Show that if an algorithm makes at most a constant number of calls to polynomial-time subroutines and performs an additional amount of work that also takes polynomial time, then it runs in polynomial time. Also show that a polynomial number of calls to polynomial-time subrountines may result in an exponential-time algorithm.

* Constant number

$O \left ( (((n^{d\_1})^{d\_2})\dots)^{d\_m} + n^{c} \right ) = O \left ( n^{d\_1+d\_2+\dots+d\_m} + n^{c} \right )$ which is still polynomial time.

* Polynomial number

Suppose the size of the output of a subrountines is twice the size of the input, then the algorithm is at least $O(2^m)$.

### 34.1-6

> Show that the class P, viewed as a set of languages, is closed under union, intersection, concatenation, complement, and Kleene star. That is, if $L\_1, L\_2 \in \text{P}$, then $L\_1 \cup L\_2 \in \text{P}$, $L\_1 \cap L\_2 \in \text{P}$, $L\_1L\_2 \in \text{P}$, $\overline{L\_1} \in \text{P}$, and $L\_1^\* \in \text{P}$.

Suppose $A\_1$ accepts $L\_1$ and $A\_2$ accepts $L\_2$, we can construct algorithm $A\_3$ that runs under polynomial time:

* $L\_1 \cup L\_2 \in \text{P}$

```
IF A_1(x) == 1 || A_2(x) == 1
THEN RETURN 1
ELSE RETURN 0
```

* $L\_1 \cap L\_2 \in \text{P}$

```
IF A_1(x) == 1 && A_2(x) == 1
THEN RETURN 1
ELSE RETURN 0
```

* $L\_1L\_2 \in \text{P}$

```
FOR i = 1 .. n
    IF A_1(x_1 ... x_i) == 1 && A_2(x_i+1 ... x_n) == 1
    THEN RETURN 1
RETURN 0
```

* $\overline{L\_1} \in \text{P}$

```
IF A_1(x) == 1:
RETURN 0
RETURN 1
```

* $L\_1^\* \in \text{P}$

```
IF x == epsilon
THEN RETURN 1

FOR i = 1 .. n
    DP[i] = 0
DP[0] = 1
FOR i = 0 .. n
    FOR j = i + 1 .. n
        IF A_1(x_i ... x_j) == 1
        THEN DP[j] = 1
RETURN DP[n]
```
