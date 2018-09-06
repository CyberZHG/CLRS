## 34.3 NP-completeness and reducibility

### 34.3-1

> Verify that the circuit in Figure 34.8(b) is unsatisfiable.

```python
results = []
for x1 in [0, 1]:
    for x2 in [0, 1]:
        for x3 in [0, 1]:
            g11 = x1 | x2
            g12 = ~~x3
            g13 = x1 & x2 & ~x3
            g21 = g11 & g12
            g22 = g12 | g13
            result = g21 & g22 & g13
            results.append(result)
print(max(results))
```

### 34.3-2

> Show that the $\le\_\text{P}$ relation is a transitive relation on languages. That is, show that if $L\_1 \le\_\text{P} L\_2$ and $L\_2 \le\_\text{P} L\_3$, then $L\_1 \le\_\text{P} L\_3$.

Suppose the reduction function of $L\_1 \le\_\text{P} L\_2$ is $f$ and the reduction function of $L\_2 \le\_\text{P} L\_3$ is $g$, then the reduction function from $L\_1$ to $L\_3$ is $g(f)$. Suppose $f$ runs in $O(n^k)$ time with some constant $k$, then the size of output is also $O(n^k)$. Suppose $g$ runs in $O(n^c)$ time with some constant $c$, then the total time of $g(f)$ is $O((n^k)^c) = O(n^{kc})$, which is polynomial to $n$. Therefore $L\_1$ is polynomial-time reducible to $L\_3$, $L\_1 \le\_\text{P} L\_3$.

### 34.3-3

> Prove that $L \le\_{\text{P}} \overline{L}$ if and only if $\overline{L} \le\_{\text{P}} L$.

* $L \le\_{\text{P}} \overline{L} \Rightarrow \overline{L} \le\_{\text{P}} L$

Suppose the polynomial-time reduction is $f$, then $\forall x \in L, f(x) \in \overline{L}$, and $\forall x \notin L, f(x) \notin \overline{L}$. $x \notin L$ means $x \in \overline{L}$, $f(x) \notin \overline{L}$ means $f(x) \in L$, therefore we can use the same $f$ for reduction.

* $\overline{L} \le\_{\text{P}} L \Rightarrow L \le\_{\text{P}} \overline{L}$

Symmetric.

### 34.3-4

> Show that we could have used a satisfying assignment as a certificate in an alternative proof of Lemma 34.5. Which certificate makes for an easier proof?

Use only inputs and calculate the output.

### 34.3-5

> The proof of Lemma 34.6 assumes that the working storage for algorithm $A$ occupies a contiguous region of polynomial size. Where in the proof do we exploit this assumption? Argue that this assumption does not involve any loss of generality.

Just like virtual memory, we can add a mapping from scattered regions to one continguous region.

### 34.3-6

> A language $L$ is __*complete*__ for a language class $C$ with respect to polynomial-time reductions if $L \in C$ and $L' \le\_\text{P} L$ for all $L' \in C$. Show that $\emptyset$ and $\\{0, 1\\}^\*$ are the only languages in $\text{P}$ that are not complete for $\text{P}$ with respect to polynomial-time reductions.

* $\emptyset$: rejects everything.
* $\\{0, 1\\}^\*$: accepts everything.
* others: we can choose a string in $L$ (in polynomial time since $L' \in P$) if $i \in L'$ is accepted, and a string in $\overline{L}$ if it is rejected.

### 34.3-7

> Show that, with respect to polynomial-time reductions (see Exercise 34.3-6), $L$ is complete for $\text{NP}$ if and only if $\overline{L}$ is complete for $\text{co-NP}$.

* $L \Rightarrow \overline{L}$

$L \in \text{NP}$ and $\forall L' \in \text{NP}, L' \le\_\text{P} L$

$L \in \text{NP} \Rightarrow \overline{L} \in \text{co-NP}$

$\forall L' \in \text{NP}, L' \le\_\text{P} L \Rightarrow \forall \overline{L'} \in \text{NP}, \overline{L'} \le\_\text{P} L \Rightarrow \forall L' \in \text{co-NP}, \overline{L'} \le\_\text{P} L \Rightarrow \forall L' \in \text{co-NP}, L' \le\_\text{P} \overline{L}$

* $\overline{L} \Rightarrow L$

Symmetric

### 34.3-8

> The reduction algorithm $F$ in the proof of Lemma 34.6 constructs the circuit $C = f(x)$ based on knowledge of $x$, $A$ and $k$. Professor Sartre observes that the string $x$ is input to $F$, but only the existence of $A$, $k$, and the constant factor implicit in the $O(n^k)$ running time is known to $F$ (since language $L$ belongs to $\text{NP}$), not their actual values. Thus the professor concludes that $F$ can't possibly construct the circuit $C$ and that language CIRCUIT-SAT is not necessarily NP-hard. Explain the flaw in professor's reasoning.

Without a concrete $A(x, y)$ we can't prove $L \in \text{NP}$.
