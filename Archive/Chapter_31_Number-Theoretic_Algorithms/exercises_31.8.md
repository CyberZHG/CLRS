## 31.8 Primality testing

### 31.8-1

> Prove that if an odd integer $$n > 1$$ is not a prime or a prime power, then there exists a nontrivial square root of $$1$$ modulo $$n$$.


### 31.8-2 $$\star$$

### 31.8-3

> Prove that if $$x$$ is a nontrivial square root of $$1$$, modulo $$n$$, then $$\text{gcd}(x - 1, n)$$ and $$\text{gcd}(x + 1, n)$$ are both nontrivial divisors of $$n$$.

$$
\begin{array}{rlll}
x^2 &\equiv& 1 & (\text{mod}~ n) \\
x^2 - 1 &\equiv& 0 & (\text{mod}~ n) \\
(x + 1) (x - 1) &\equiv& 0 & (\text{mod}~ n) \\
\end{array}
$$

$$n ~|~ (x + 1)(x - 1)$$, suppose $$\text{gcd}(x - 1, n) = 1$$, then $$n ~|~ (x + 1)$$, then $$x \equiv -1 ~(\text{mod}~ n)$$ which is trivial, it contradicts the fact that $$x$$ is nontrivial, therefore $$\text{gcd}(x - 1, n) \ne 1$$, $$\text{gcd}(x + 1, n) \ne 1$$.
