## 31.1 Elementary number-theoretic notions

### 31.1-1

> Prove that if $$a > b > 0$$ and $$c = a + b$$, then $$c ~\text{mod}~ a = b$$.

$$
\begin{array}{rll}
c ~\text{mod}~ a &=& (a + b) ~\text{mod}~ a \\
&=& (a ~\text{mod}~ a) + (b ~\text{mod}~ a) \\
&=& 0 + b \\
&=& b
\end{array}
$$

### 31.1-2

> Prove that there are infinitely many primes.

$$
\begin{array}{rl}
& ((p_1 p_2 \cdots p_k) + 1) ~\text{mod}~ p_i \\
=& (p_1 p_2 \cdots p_k) ~\text{mod}~ p_i + (1 ~\text{mod}~ p_i) \\
=& 0 + 1 \\
=& 1
\end{array}
$$

### 31.1-3

> Prove that if $$a ~|~ b$$ and $$b ~|~ c$$, then $$a ~|~ c$$.

* If $$a ~|~ b$$, then $$b = a \cdot k_1$$.
* If $$b ~|~ c$$, then $$c = b \cdot k_2 = a \cdot (k_1 \cdot k_2) = a \cdot k_3$$, then $$a | c$$.

### 31.1-4

> Prove that if $$p$$ is prime and $$0 < k < p$$, then $$\text{gcd}(k, p) = 1$$.

* If $$k \ne 1$$, then $$k~\nmid~p$$.
* If $$k = 1$$, then the divisor is $$1$$.

### 31.1-5

> Prove Corollary 31.5.

> For all positive integers $$n$$, $$a$$, and $$b$$, if $$n~|~ab$$ and $$\text{gcd}(a, n) = 1$$, then $$n~|~b$$.

If $$n ~|~ ab$$, then $$ab = kn$$, then $$b = nk / a$$; since $$\text{gcd}(a, n) = 1$$, then $$n / a$$ could not be an integer; since $$b$$ is an integer, then $$k / a$$ must be an integer, $$b = nk / a = n (k / a) = n k'$$, then $$n ~|~ b$$.

### 31.1-6

> Prove that if $$p$$ is prime and $$0 < k < p$$, then $$p ~|~ \binom{p}{k}$$. Conclude that for all integers $$a$$ and $$b$$ and all primes $$p$$,

> $$(a + b)^p \equiv a^p + b^p ~(\text{mod}~p)$$.

$$
\begin{array}{rlll}
(a + b) ^ p &\equiv& \displaystyle a^p + \binom{p}{1} a^{p-1}b^{1} + \cdots + \binom{p}{p-1} a^{1}b^{p-1} + b^p &(\text{mod}~ p) \\
&\equiv& a^p + 0 + \cdots + 0 + b^p &(\text{mod}~ p) \\
&\equiv& a^p + b^p &(\text{mod} p)~ \\
\end{array}
$$

### 31.1-7

> Prove that if $$a$$ and $$b$$ are any positive integers such that $$a~|~b$$, then

> $$(x~\text{mod}~b)~\text{mod}~a = x~\text{mod}~a$$

> for any $$x$$. Prove, under the same assumptions, that

> $$x \equiv y ~(\text{mod}~ b)$$ implies $$x \equiv y ~(\text{mod}~a)$$

> for any integers $$x$$ and $$y$$.

Suppose $$x = kb + c$$, then $$(x~\text{mod}~b)~\text{mod}~a = c~\text{mod}~a$$, and $$x~\text{mod}~a = (kb + c)~\text{mod}~a = (kb~\text{mod}~a) + (c~\text{mod}~a) = c~\text{mod}~a$$.

### 31.1-8

> For any integer $$k > 0$$, an integer $$n$$ is a __*$$k$$th power*__ if there exists an integer $$a$$ such that $$a^k = n$$. Furthermore, $$n > 1$$ is a __*nontrivial power*__ if it is a $$k$$th power for some integer $$k > 1$$. Show how to determine whether a given $$\beta$$-bit integer $$n$$ is a nontrivial power in time polynomial in $$\beta$$.

Iterate $$a$$ from $$2$$ to $$\sqrt{n}$$, and do binary searching.

### 31.1-9

> Prove equations (31.6)-(31.10).

$$\dots$$

### 31.1-10

> Show that the gcd operator is associative. That is, prove that for all integers $$a$$, $$b$$, and $$c$$,

> $$\text{gcd}(a, \text{gcd}(b, c)) = \text{gcd}(\text{gcd}(a, b), c)$$.

$$\dots$$

### 31.1-11 $$\star$$

> Prove Theorem 31.8.

### 31.1-12

> Give efficient algorithms for the operations of dividing a $$\beta$$-bit integer by a shorter integer and of taking the remainder of a $$\beta$$-bit integer when divided by a shorter integer. Your algorithms should run in time $$\Theta(\beta^2)$$.

Shift left until the two numbers have the same length, then repeatedly subtract with proper multiplier and shift right.

### 31.1-13

> Give an efficient algorithm to convert a given $$\beta$$-bit (binary) integer to a decimal representation. Argue that if multiplication or division of integers whose length is at most $$\beta$$ takes time $$M(\beta)$$, then we can convert binary to decimal in time $$\Theta(M(\beta) \lg \beta)$$.

```python
def bin2dec(s):
    n = len(s)
    if n == 1:
        return ord(s) - ord('0')
    m = n // 2
    h = bin2dec(s[:m])
    l = bin2dec(s[m:])
    return (h << (n - m)) + l
```
