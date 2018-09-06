## 15.2 Matrix-chain multiplication

### 15.2-1

> Find an optimal parenthesization of a matrix-chain product whose sequence of dimensions is $\left \langle 5, 10, 3, 12, 5, 50, 6 \right \rangle$.

Table $m$:

|  | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 150 | 330 | 405 | 1655 | 2010 |
| 2 |  | 0 | 360 | 330 | 2430 | 1950 |
| 3 |  |  | 0 | 180 | 930 | 1770 |
| 4 |  |  |  | 0 | 3000 | 1860 |
| 5 |  |  |  |  | 0 | 1500 |
| 6 |  |  |  |  |  | 0 |

Table $s$:

|  | 1 | 2 | 3 | 4 | 5 | 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  | 1 | 2 | 2 | 4 | 2 |
| 2 |  |  | 2 | 2 | 2 | 2 |
| 3 |  |  |  | 3 | 4 | 4 |
| 4 |  |  |  |  | 4 | 4 |
| 5 |  |  |  |  |  | 5 |
| 6 |  |  |  |  |  |  |

Optimal parenthesization:


$$
(A\_1 \times A\_2) \times ((A\_3 \times A\_4) \times (A\_5 \times A\_6))
$$


### 15.2-2

> Give a recursive algorithm MATRIX-CHAIN-MULTIPLY$(A, s, i, j)$ that actually performs the optimal matrix-chain multiplication, given the sequence of matrices $\langle A\_1, A\_2, \dots ,A\_{n\_i} \rangle$, the $s$ table computed by MATRIX-CHAIN-ORDER, and the indices $i$ and $j$. \(The initial call would be MATRIX-CHAIN-MULTIPLY$(A, s, 1, n)$.\)

```
MATRIX-CHAIN-MULTIPLY(A, s, i, j)
1 if i == j
2     return A[i]
3 if i + 1 == j
4     return A[i] * A[j]
5 b = MATRIX-CHAIN-MULTIPLY(A, s, i, s[i, j])
6 c = MATRIX-CHAIN-MULTIPLY(A, s, s[i, j] + 1, j)
7 return b * c
```

### 15.2-3

> Use the substitution method to show that the solution to the recurrence \(15.6\) is $\Omega(2^n)$.

Suppose $P(n) \ge c2^n$,


$$
\begin{array}{rlll}
P(n) &\ge& \displaystyle \sum\_{k=1}^{n-1} c2^k \cdot c2^{n-k} \\\\
&=& \displaystyle \sum\_{k=1}^{n-1} c^2 2^n \\\\
&=& \displaystyle c^2 (n - 1) 2^n \\\\
&\ge& \displaystyle c^2 2^n & (n > 1) \\\\
&\ge& \displaystyle c 2^n & (0 < c \le 1)
\end{array}
$$


### 15.2-4

> Describe the subproblem graph for matrix-chain multiplication with an input chain of length $n$. How many vertices does it have? How many edges does it have, and which edges are they?

Vertice: $O(n^2)$, edges: $O(n^3)$.

### 15.2-5

> Let $R(i, j)$ be the number of times that table entry $m[i, j]$ is referenced while computing other table entries in a call of MATRIX-CHAIN-ORDER. Show that the total number of references for the entire table is  
> $\displaystyle \sum\_{i=1}^n \sum\_{j=i}^n R(i, j) = \frac{n^3 - n}{3}$.


$$
\sum\_{i=1}^n \sum\_{j=i}^n R(i, j) = \sum\_{l=2}^n 2 (n - l + 1) (l - 1) = \frac{n^3 - n}{3}
$$


### 15.2-6

> Show that a full parenthesization of an $n$-element expression has exactly $n-1$ pairs  
> of parentheses.

$n - 1$ multiplications.
