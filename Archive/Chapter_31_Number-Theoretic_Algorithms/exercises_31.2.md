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

### 31.2-7

> Define the $$\text{gcd}$$ function for more than two arguments by the recursive equation $$\text{gcd}(a_0, a_1, \cdots, a_n) = \text{gcd}(a_0, \text{gcd}(a_1, a_2, \cdots, a_n))$$. Show that the $$\text{gcd}$$ function returns the same answer independent of the order in which its arguments are specified. Also show how to find integers $$x_0, x_1, \cdots, x_n$$ such that $$\text{gcd}(a_0, a_1, \dots, a_n) = a_0 x_0 + a_1 x_1 + \cdots + a_n x_n$$. Show that the number of divisions performed by your algorithm is $$O(n + \lg (max \{a_0, a_1, \cdots, a_n \}))$$.

Suppose $$\text{gcd}(a_0, \text{gcd}(a_1, a_2, \cdots, a_n))  = a_0 \cdot x + \text{gcd}(a_1, a_2, \cdots, a_n) \cdot y$$ and $$\text{gcd}(a_1, \text{gcd}(a_2, a_3, \cdots, a_n))  = a_1 \cdot x' + \text{gcd}(a_2, a_3, \cdots, a_n) \cdot y'$$, then the coefficient of $$a_1$$ is $$y \cdot x'$$.

```python
def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    d, x, y = extended_euclid(b, a % b)
    return (d, y, x - (a // b) * y)


def extended_eculid_multi(a):
    if len(a) == 1:
        return (a[0], [1])
    g = a[-1]
    xs = [1] * len(a)
    ys = [0] * len(a)
    for i in xrange(len(a) - 2, -1, -1):
        g, xs[i], ys[i + 1] = extended_euclid(a[i], g)
    m = 1
    for i in xrange(1, len(a)):
        m *= ys[i]
        xs[i] *= m
    return (g, xs)
```

### 31.2-8

> Define $$\text{lcm}(a_1, a_2, \dots, a_n)$$ to be the __*least common multiple*__ of the $$n$$ integers $$a_1, a_2, \dots, a_n$$, that is, the smallest nonnegative integer that is a multiple of each $$a_i$$. Show how to compute $$\text{lcm}(a_1, a_2, \dots, a_n)$$ efficiently using the (two-argument) $$\text{gcd}$$ operation as a subroutine.

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b


def lcm_multi(lst):
    l = lst[0]
    for i in xrange(1, len(lst)):
        l = lcm(l, lst[i])
    return l
```

### 31.2-9

> Prove that $$n_1$$, $$n_2$$, $$n_3$$, and $$n_4$$ are pairwise relatively prime if and only if
> 
> $$\text{gcd}(n_1n_2,n_3n_4) = \text{gcd}(n_1n_3, n_2n_4) = 1$$
> 
> More generally, show that $$n_1, n_2, \dots, n_k$$ are pairwise relatively prime if and only if a set of $$\lceil \lg k \rceil$$ pairs of numbers derived from the $$n_i$$ are relatively prime.

Suppose $$n_1 n_2 x + n_3 n_4 y = 1$$, then $$n_1 (n_2 x) + n_3 (n_4 y) = 1$$, thus $$n_1$$ and $$n_3$$ are relatively prime, $$n_1$$ and $$n_4$$, $$n_2$$ and $$n_3$$, $$n_2$$ and $$n_4$$ are the all relatively prime. And since $$\text{gcd}(n_1n_3, n_2n_4) = 1$$, all the pairs are relatively prime.

General: in the first round, divide the elements into two sets with equal number of elements, calculate the products of the two set separately, if the two products are relatively prime, then the element in one set is pairwise relatively prime with the element in the other set. In the next iterations, for each set, we divide the elements into two subsets, suppose we have subsets $$\{ (s_1, s_2), (s_3, s_4), \dots \}$$, then we calculate the products of $$\{s_1, s_3, \dots\}$$ and $$\{s_2, s_4, \dots\}$$, if the two products are relatively prime, then all the pairs of subset are pairwise relatively prime similar to the first round. In each iteration, the number of elements in a subset is half of the original set, thus there are $$\lceil \lg k \rceil$$ pairs of products.

To choose the subsets efficiently, in the $$k$$th iteration, we could divide the numbers based on the value of the index's $$k$$th bit.

