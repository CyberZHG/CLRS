## 11.5 Perfect hashing

### 11.5-1 $$\star$$

> Suppose that we insert $$n$$ keys into a hash table of size $$m$$ using open addressing and uniform hashing. Let $$p(n, m)$$ be the probability that no collisions occur. Show that $$p(n, m) \le e^{-n(n-1)/2m}$$.

$$
p(n, m) = \frac{m}{m} \cdot \frac{m-1}{m} \cdots \frac{m-n+1}{m} = \frac{m \cdot (m-1) \cdots (m-n+1)}{m^n}
$$

$$
\begin{array}{rll}
\displaystyle (m - i) \cdot (m - n + i) &=&
\displaystyle \left (m - \frac{n}{2} + \frac{n}{2} - i \right ) \cdot \left ( m - \frac{n}{2} - \frac{n}{2} + i \right ) \\
&=& \displaystyle \left ( m - \frac{n}{2} \right ) ^2 - \left ( i - \frac{n}{2} \right ) ^2 \\
&\le& \displaystyle \left ( m - \frac{n}{2} \right ) ^2
\end{array}
$$

$$
\begin{array}{rll}
p(n, m) &\le&
\displaystyle \frac{\displaystyle m \cdot \left ( m - \frac{n}{2} \right ) ^ {n-1}}{m^n} \\
&=& \displaystyle \left ( 1 - \frac{n}{2m} \right ) ^ {n - 1} \\
\end{array}
$$

Based on equation (3.12), $$e^x \ge 1 + x$$,

$$
\begin{array}{rll}
p(n, m) &\le&
\displaystyle \left ( e^{-n/2m} \right ) ^ {n - 1} \\
&=& \displaystyle e^{-n(n-1)/2m}
\end{array}
$$
