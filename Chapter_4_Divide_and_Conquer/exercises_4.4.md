## The recursion-tree method for solving recurrences

### 4.4-1

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=3T(\left \lfloor n / 2 \right \rfloor) + n$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \sum_{i=0}^{\lg n - 1}(\frac{3}{2})^i n + \Theta(n^{\lg 3}) \\
& = & \frac{(3/2)^{\lg n}-1}{(3/2)-1}n + \Theta(n^{\lg 3}) \\
& = & 2n^{\lg 3} - 2n + \Theta({n^{\lg 3}}) \\
& = & \Theta({n^{\lg 3}})
\end{array}
$$

### 4.4-2

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=T(n/2)+n^2$$. Use the substitution method to verify your answer.

$$
\begin{array}{lll}
T(n) & = & \sum_{i=0}^{\lg n - 1}(\frac{1}{2})^i n^2 + \Theta(1) \\
& = & \frac{(1/2)^{\lg n}-1}{(1/2)-1}n^2 + \Theta(1) \\
& = & 2n^2 - \frac{2}{n} + \Theta(1) \\
& = & \Theta(n^2) \\
\end{array}
$$

### 4.4-3

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=4T(n/2+2)+n$$. Use the substitution method to verify your answer.

### 4.4-4

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=2T(n-1)+1$$. Use the substitution method to verify your answer.

### 4.4-5

> Use a recursion tree to determine a good asymptotic upper bound on the recurrence $$T(n)=T(n-1)+T(n/2)+n$$. Use the substitution method to verify your answer.

### 4.4-6

> Argue that the solution to the recurrence $$T(n)=T(n/3)+T(2n/3)+cn$$, where $$c$$ is a constant, is $$\Omega(n \lg n)$$ by appealing to a recursion tree.

### 4.4-7

> Draw the recursion tree for $$T(n)=4T(\left \lfloor n / 2 \rfloor \right) + cn$$, where $$c$$ is a constant, and provide a tight asymptotic bound on its solution. Verify your bound by the substitution method.

### 4.4-8

> Use a recursion tree to give an asymptotically tight solution to the recurrence $$T(n) = T(n-a) + T(a) + cn$$, where $$a \ge 1$$ and $$c > 0 $$are constants.

### 4.4-9

> Use a recursion tree to give an asymptotically tight solution to the recurrence $$T(n)=T(\alpha n)+T((1-\alpha)n)+cn$$, where $$\alpha$$ is a constant in the range $$0 < \alpha < 1$$ and $$c > 0$$ is also a constant.

