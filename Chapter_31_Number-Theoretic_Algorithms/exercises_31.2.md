## 31.2 Greatest common divisor

### 31.2-1

> Prove that equations (31.11) and (31.12) imply equation (31.13).

### 31.2-2

 > Compute the values $$(d, x, y)$$ that the call EXTENDED-EUCLID$$(899, 493)$$ returns.

$$(29, -6, 11)$$.

### 31.2-3

> Prove that for all integers $$a$$, $$k$$, and $$n$$,

> $$\text{gcd}(a, n) = \text{gcd}(a + kn, n)$$.

* $$\text{gcd}(a, n) ~|~ \text{gcd}(a + kn, n)$$

Let $$d = \text{gcd}(a, n)$$, then $$d ~|~ a$$ and $$d ~|~ n$$. Since $$(a + kn) ~\text{mod}~ d = a ~\text{mod}~ d + k \cdot (n ~\text{mod}~ d) = 0$$ and $$d ~|~ n$$, then $$d ~|~ \text{gcd}(a + kn, n)$$, $$\text{gcd}(a, n) ~|~ \text{gcd}(a + kn, n)$$.

* $$\text{gcd}(a + kn, n) ~|~ \text{gcd}(a, n)$$

Let $$d = \text{gcd}(a + kn, n)$$, then $$d ~|~ n$$ and $$d ~|~ (a + kn)$$. Since $$(a + kn) ~\text{mod}~ d = a ~\text{mod}~ d + k \cdot (n ~\text{mod}~ d) = a ~\text{mod}~ d = 0$$, then $$d ~|~ a$$. Since $$d ~|~ a$$ and $$d ~|~ n$$, then $$d ~|~ \text{gcd}(a, n)$$,  $$\text{gcd}(a + kn, n) ~|~ \text{gcd}(a, n)$$.

Since $$\text{gcd}(a, n) ~|~ \text{gcd}(a + kn, n)$$ and $$\text{gcd}(a + kn, n) ~|~ \text{gcd}(a, n)$$, then $$\text{gcd}(a, n) = \text{gcd}(a + kn, n)$$.

### 31.2-4

> Rewrite EUCLID in an iterative form that uses only a constant amount of memory (that is, stores only a constant number of integer values).

```python
def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### 31.2-5

> If $$a > b \ge 0$$, show that the call EUCLID$$(a, b)$$ makes at most $$1 + \log_\phi b$$ recursive calls. Improve this bound to $$1 + \log_\phi(b / \text{gcd}(a, b))$$.

$$b \ge F_{k+1} \approx \phi^{k+1} / \sqrt{5}$$

$$k + 1 < \log_\phi \sqrt{5} + \log_\phi b \approx 1.67 + \log_\phi b$$

$$k < 0.67 + \log_\phi b < 1 + \log_\phi b$$.

Since $$d \cdot a ~\text{mod}~ d \cdot b = d \cdot (a ~\text{mod}~ b)$$, $$\text{gcd}(d \cdot a, d \cdot b)$$ has the same number of recursive calls with $$\text{gcd}(a, b)$$, therefore we could let $$b' = b / \text{gcd}(a, b)$$, the inequality $$k < 1 + \log_\phi(b') = 1 + \log_\phi(b / \text{gcd}(a, b))$$. will holds.

## 31.2-6

> What does EXTENDED-EUCLID$$(F_{k+1}, F_k)$$ return? Prove your answer correct.

* If $$k$$ is odd, then $$(1, -F_{k-2}, F_{k-1})$$.
* If $$k$$ is even, then $$(1, F_{k-2}, -F_{k-1})$$.

If $$k = 2$$, then $$F_2 = 2$$, $$F_3 = 3$$, $$1 \cdot 3 - 1 \cdot 2 = 1$$.

If $$k$$ is odd, 

$$
\begin{array}{ll}
& -F_{k-2} \cdot F_{k+1} + F_{k-1} \cdot F_{k} \\
=& -F_{k-2} \cdot (F_{k} + F_{k-1} ) + F_{k-1} \cdot F_k \\ 
\end{array}
$$


31.2-7
Define the gcd function for more than two arguments by the recursive equation
gcd.a0; a1; : : : ;an/ D gcd.a0; gcd.a1; a2; : : : ;an//. Show that the gcd function
returns the same answer independent of the order in which its arguments are specified.
Also show how to find integers x0; x1; : : : ;xn such that gcd.a0; a1; : : : ;an/ D
a0x0 C a1x1 C  Canxn. Show that the number of divisions performed by your
algorithm is O.n C lg.max fa0; a1; : : : ;ang//.
31.2-8
Define lcm.a1; a2; : : : ;an/ to be the least common multiple of the n integers
a1; a2; : : : ;an, that is, the smallest nonnegative integer that is a multiple of each ai .
Show how to compute lcm.a1; a2; : : : ;an/ efficiently using the (two-argument) gcd
operation as a subroutine.
31.2-9
Prove that n1, n2, n3, and n4 are pairwise relatively prime if and only if
gcd.n1n2; n3n4/ D gcd.n1n3; n2n4/ D 1 :
More generally, show that n1; n2; : : : ;nk are pairwise relatively prime if and only
if a set of dlg ke pairs of numbers derived from the ni are relatively prime.