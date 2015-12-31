## 9.3 Selection in worst-case linear time

### 9.3-1

> In the algorithm SELECT, the input elements are divided into groups of 5. Will the algorithm work in linear time if they are divided into groups of 7? Argue that SELECT does not run in linear time if groups of 3 are used.

Suppose the input elements are divided into $$7$$ groups, then

$$
4 \left (\left \lceil \frac{1}{2} \left \lceil \frac{n}{7} \right \rceil \right \rceil - 2 \right ) \ge \frac{2n}{7} - 8
$$

$$
T(n) = T(\lceil n / 7 \rceil) + T(5n/7 + 8) + O(n)
$$

Suppose $$T(n) \le cn$$,

$$
\begin{array}{rll}
T(n) &\le& cn/7 + c + 8c + 5cn/7 + an \\
&=& 6cn / 7 + 9c + an \\
&=& cn + (-cn/7+9c+an) \\
&\le& cn
\end{array}
$$

Suppose the input elements are divided into $$3$$ groups, then

$$
2 \left (\left \lceil \frac{1}{2} \left \lceil \frac{n}{3} \right \rceil \right \rceil - 2 \right ) \ge \frac{n}{3} - 4
$$

$$
T(n) = T(\lceil n / 3 \rceil) + T(2n/3 + 4) + O(n)
$$

Suppose $$T(n)\ge cn$$,

$$
\begin{array}{rll}
T(n) &\ge& cn/3 + c + 4c + 2cn/3 + an \\
&=& cn + 5c + an \\
&>& cn \\
\end{array}
$$

Therefore SELECT does not run in linear time if groups of 3 are used.

