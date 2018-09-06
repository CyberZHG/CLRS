## 17.4 Dynamic tables

### 17.4-1

> Suppose that we wish to implement a dynamic, open-address hash table. Why might we consider the table to be full when its load factor reaches some value $\alpha$ that is strictly less than 1? Describe briefly how to make insertion into a dynamic, open-address hash table run in such a way that the expected value of the amortized cost per insertion is $O(1)$. Why is the expected value of the actual cost per insertion not necessarily $O(1)$ for all insertions?

### 17.4-2

> Show that if $\alpha\_{i-1} \ge 1/2$ and the $i$th operation on a dynamic table is TABLE-DELETE, then the amortized cost of the operation with respect to the potential function (17.6) is bounded above by a constant.

$$
\begin{array}{rll}
\displaystyle \hat{c\_i} 
&=& \displaystyle c\_i + \Phi\_i - \Phi\_{i-1} \\\\
&=& \displaystyle 1 + (2 \cdot num\_i - size\_i) - (2 \cdot (num\_i + 1) - size\_i) \\\\
&=& -1
\end{array}
$$

### 17.4-3

> Suppose that instead of contracting a table by halving its size when its load factor drops below $1/4$, we contract it by multiplying its size by $2/3$ when its load factor drops below $1/3$. Using the potential function

> $\Phi(T) = | 2 \cdot T.num - T.size |$,

> show that the amortized cost of a TABLE-DELETE that uses this strategy is bounded above by a constant.

If $1/3 < \alpha\_i \le 1/2$,

$$
\begin{array}{rll}
\hat{c\_i} &=& c\_i + \Phi\_i - \Phi\_{i-1} \\\\
&=& 1 + (size\_i - 2 \cdot num\_i) - (size\_i - 2 \cdot (num\_i + 1)) \\\\
&=& 3
\end{array}
$$
If the $i$th operation does trigger a contraction,

$$
\frac{1}{3} size\_{i-1} = num\_i + 1 \\\\
size\_{i-1} = 3 (num\_i + 1) \\\\
size\_{i} = \frac{2}{3} size\_{i-1} = 2 (num\_i + 1)
$$

$$
\begin{array}{rll}
\hat{c\_i} &=& c\_i + \Phi\_i - \Phi\_{i-1} \\\\
&=& (num\_i + 1) + [2 \cdot (num\_i + 1) - 2 \cdot num\_i] - [3 \cdot (num\_i + 1) - 2 \cdot (num\_i + 1)] \\\\
&=& 2
\end{array}
$$
