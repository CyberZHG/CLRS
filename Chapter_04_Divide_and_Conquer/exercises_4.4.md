## 4.4 The recursion-tree method for solving recurrences

### 4.4-1

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=3T(\left \lfloor n / 2 \right \rfloor) + n$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{\lg n - 1}(\frac{3}{2})^i n + \Theta(n^{\lg 3}) \\
& = & \displaystyle \frac{(3/2)^{\lg n}-1}{(3/2)-1}n + \Theta(n^{\lg 3}) \\
& = & \displaystyle 2n^{\lg 3} - 2n + \Theta({n^{\lg 3}}) \\
& = & \displaystyle \Theta({n^{\lg 3}})
\end{array}
$$

### 4.4-2

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=T(n/2)+n^2$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{\lg n - 1}(\frac{1}{2})^i n^2 + \Theta(1) \\
& = & \displaystyle \frac{(1/2)^{\lg n}-1}{(1/2)-1}n^2 + \Theta(1) \\
& = & \displaystyle 2n^2 - \frac{2}{n} + \Theta(1) \\
& = & \displaystyle \Theta(n^2) \\
\end{array}
$$

### 4.4-3

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=4T(n/2+2)+n$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{\lg n - 1}(2^in) + \sum_{i=0}^{\lg n - 1}(2^{2i+1}) + \Theta(n^2) \\
& = & \displaystyle \frac{2^{\lg n}-1}{2-1}n + \Theta(n^2) \\
& = & \displaystyle n^2 - n + \Theta(n^2) \\
& = & \displaystyle \Theta(n^2) \\
\end{array}
$$

### 4.4-4

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=2T(n-1)+1$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{n - 1}(2^i) + \Theta(2^n) \\
& = & \displaystyle \frac{2^n-1}{2-1} + \Theta(2^n) \\
& = & \displaystyle 2^n - 1 + \Theta(2^n) \\
& = & \displaystyle \Theta(2^n) \\
\end{array}
$$

### 4.4-5

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=T(n-1)+T(n/2)+n$$. Use the substitution method to verify your answer.

$$
O(n^{\lg n})
$$

### 4.4-6

> Argue that the solution to the recurrence $$T(n)=T(n/3)+T(2n/3)+cn$$, where $$c$$ is a constant, is $$\Omega(n \lg n)$$ by appealing to a recursion tree.

Shortest path is $$\log_3n$$.

### 4.4-7

> Draw the recursion tree for $$T(n)=4T(\left \lfloor n / 2 \rfloor \right) + cn$$, where $$c$$ is a constant, and provide a tight asymptotic bound on its solution. Verify your bound by the substitution method.

$$\Theta(n^2)$$.

### 4.4-8

> Use a recursion tree to give an asymptotically tight solution to the recurrence $$T(n) = T(n-a) + T(a) + cn$$, where $$a \ge 1$$ and $$c > 0 $$ are constants.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{n/a}(c(n-ai) )+ cn \\
& = & \displaystyle \Theta(n^2) \\
\end{array}
$$

### 4.4-9

> Use a recursion tree to give an asymptotically tight solution to the recurrence $$T(n)=T(\alpha n)+T((1-\alpha)n)+cn$$, where $$\alpha$$ is a constant in the range $$0 < \alpha < 1$$ and $$c > 0$$ is also a constant.

$$
\begin{array}{lll}
T(n) & = & \displaystyle \sum_{i=0}^{\log_{1/\alpha}n}cn + \Theta(n) \\
& = & \displaystyle \Theta(n\lg n) \\
\end{array}
$$
