## Problems

### 11-1 Longest-probe bound for hashing

> Suppose that we use an open-addressed hash table of size $$m$$ to store $$n \le m/2$$ items.

> __*a*__. Assuming uniform hashing, show that for $$i=1,2,\dots,n$$, the probability is at most $$2^{-k}$$ that the $$i$$th insertion requires strictly more than $$k$$ probes.

$$
\begin{array}{rll}
\displaystyle \text{Pr}\{X_i > k\} &=& 
\displaystyle \frac{n}{m} \cdot \frac{n - 1}{m - 1} \cdots \frac{n - k + 1}{m - k + 1} \\
&\le& \displaystyle \left ( \frac{n}{m} \right ) ^ {k} \\
&\le& \displaystyle \left ( \frac{1}{2} \right ) ^ {k} \\
&=& 2^{-k}
\end{array}
$$

> __*b*__. Show that for $$i=1,2,\dots,n$$, the probability is $$O(1/n^2)$$ that the $$i$$th insertion requires more than $$2\lg n$$ probes.

$$
\displaystyle \text{Pr}\{X_i > 2\lg n\} \le 2^{-2 \lg n} = 1/n^2 = O(1/n^2)
$$

> Let the random variable $$X_i$$ denote the number of probes required by the $$i$$th insertion. You have shown in part (b) that $$\text{Pr}\{X_i > 2\lg n\} = O(1/n^2)$$. Let the random variable $$X = \max_{1 \le i \le n} X_i$$ denote the maximum number of probes required by any of the $$n$$ insertions.

> __*c*__. Show that $$\text{Pr}\{ X > 2\lg n\}=O(1/n)$$.

$$
\text{Pr}\{ X > 2\lg n\}\le\sum_{i=1}^n 1/n^2 = 1/n =O(1/n)
$$

> __*d*__. Show that the expected length $$\text{E}[X]$$ of the longest probe sequence is $$O(\lg n)$$.

$$
\begin{array}{rll}
\text{E}[X] 
&=& \displaystyle \sum_{i=1}^n i \cdot \text{Pr}\{X = i\} \\
&=& \displaystyle \sum_{i=1}^{2 \lg n} i \cdot \text{Pr}\{X = i\} + \sum_{i=2 \lg n + 1}^n i \cdot \text{Pr}\{X = i\} \\ 
&\le& \displaystyle 2 \lg n \cdot \sum_{i=1}^{2 \lg n} \text{Pr}\{X = i\} + n \cdot \sum_{i=2 \lg n + 1}^n \text{Pr}\{X = i\} \\ 
&\le& \displaystyle 2 \lg n \cdot 1 + n \cdot 1/n \\ 
&=& \displaystyle 2 \lg n + 1 \\ 
&=& O(\lg n)
\end{array}
$$



