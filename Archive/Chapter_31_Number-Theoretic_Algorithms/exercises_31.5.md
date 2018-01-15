## 31.5 The Chinese remainder theorem

### 31.5-1

> Find all solutions to the equations $$x \equiv 4 ~(\text{mod}~5)$$ and $$x \equiv 5 ~(\text{mod}~11)$$.

$$m_1 = 11$$, $$m_2 = 5$$.

$$m_1^{-1} = 1$$, $$m_2^{-1} = 9$$.

$$c_1 = 11$$, $$c_2 = 45$$.

$$a = (c_1 \cdot a_1 + c_2 \cdot a_2) ~\text{mod}~ (n_1 \cdot n_2) = (11 * 4 + 45 * 5) ~\text{mod}~ 55 = 49$$.

## 31.5-2

> Find all integers $$x$$ that leave remainders $$1, 2, 3$$ when divided by $$9, 8, 7$$ respectively.

$$10 + 504i$$, $$i \in \mathbb{Z}$$.

### 31.5-3

> Argue that, under the definitions of Theorem 31.27, if $$\text{gcd}(a, n) = 1$$, then
> 
>  $$(a^{-1} ~\text{mod}~ n) \leftrightarrow ((a_1^{-1} ~\text{mod}~ n_1), (a_2^{-1} ~\text{mod}~ n_2), \dots, (a_k^{-1} ~\text{mod}~ n_k))$$.

$$\text{gcd}(a, n) = 1 \rightarrow \text{gcd}(a, n_i) = 1$$.

### 31.5-4

> Under the definitions of Theorem 31.27, prove that for any polynomial $$f$$, the number of roots of the equation $$f(x) \equiv 0 ~(\text{mod}~n)$$ equals the product of the number of roots of each of the equations $$f(x) \equiv 0 ~(\text{mod}~n_1), f(x) \equiv 0 ~(\text{mod}~n_2), \dots, f(x) \equiv 0 ~(\text{mod}~n_k)$$.

Based on 31.28 ~ 31.30.
