## Problems

### 11-1 Longest-probe bound for hashing

> Suppose that we use an open-addressed hash table of size $$m$$ to store $$n \le m/2$$ items.

> __*a*__. Assuming uniform hashing, show that for $$i=1,2,\dots,n$$, the probability is at most $$2^{-k}$$ that the $$i$$th insertion requires strictly more than $$k$$ probes.

$$
\begin{array}{rll}
\displaystyle \text{Pr}\{X > k\} &=& 
\displaystyle \frac{n}{m} \cdot \frac{n - 1}{m - 1} \cdots \frac{n - k + 1}{m - k + 1} \\
&\le& \displaystyle \left ( \frac{n}{m} \right ) ^ {k} \\
&\le& \displaystyle \left ( \frac{1}{2} \right ) ^ {k} \\
&=& 2^{-k}
\end{array}
$$

