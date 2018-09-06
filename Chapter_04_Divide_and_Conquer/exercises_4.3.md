## 4.3 The substitution method for solving recurrences

### 4.3-1

> Show that the solution of $T(n) = T(n-1) + n$ is $O(n^2)$.

Suppose $T(n) \le n^2$

$$
\begin{array}{lll}
T(n) & \le & \displaystyle (n-1)^2 + n  \\
     &   = & \displaystyle n^2 - 2n + 1 + n \\
     &   = & \displaystyle n^2 - n + 1 \\
     & \le & \displaystyle n^2
\end{array}
$$

### 4.3-2

> Show that the solution of $T(n) = T(\left \lceil n / 2 \right \rceil) + 1$ is $O(\lg n)$.

Suppose $T(n) \le c\lg(n-1)$

$$
\begin{array}{llll}
T(n) & \le & \displaystyle c\lg(\left \lceil n/2 \right \rceil - a) + 1 & \\
     & \le & \displaystyle c\lg(\frac{n+1}{2} - a) + 1 & \\
     &  =  & \displaystyle c\lg(n + 1 - 2a) - c + 1 & \\
     & \le & \displaystyle c\lg(n - a) - c + 1 & \displaystyle (a \ge \frac{1}{3}) \\
     & \le & \displaystyle c\lg(n - a) & \displaystyle (c \ge 1)
\end{array}
$$

### 4.3-3

> We saw that the solution of $T(n) = 2T(\left \lfloor n / 2 \right \rfloor) + n$ is $O(n \lg n)$. Show that the solution of this recurrence is also $\Omega(n \lg n)$. Conclude that the solution is $\Theta(n \lg n)$.

Suppose $T(n) \ge cn \lg n$

$$
\begin{array}{llll}
T(n) & \ge & \displaystyle 2c(n/2)\lg(n/2)+n & \\
     &  =  & \displaystyle cn\lg n - cn + n & \\
     & \ge & \displaystyle cn\lg n & (c \le 1)
\end{array}
$$

### 4.3-4

> Show that by making a different inductive hypothesis, we can overcome the difficulty with the boundary condition $T(1) = 1$ for recurrence (4.19) without adjusting the boundary conditions for the inductive proof.

Suppose $T(n) \le cn \lg n + n$

$$
\begin{array}{llll}
T(n) & \le & \displaystyle cn\lg n - 2n + n & \\
     & \le & \displaystyle cn\lg n + n &
\end{array}
$$

When $n=1$, $T(n)=0+1=1$.

### 4.3-5

> Show that $\Theta(n\lg n)$ is the solution to the "exact" recurrence (4.3) for merge sort.

We know $T(n) = T(\left \lceil n / 2 \right \rceil) + T(\left \lfloor n / 2 \right \rfloor) + n$ is $O(n \lg n)$.

Based on 4.3-3, $T(n)$ is $\Omega(n \lg n)$.

Therefore, $T(n)$ is $\Theta(n\lg n)$.

### 4.3-6

> Show that the solution to $T(n)=2T(\left \lfloor n/2 \right \rfloor + 17) + n$ is $O(n \lg n)$.

Suppose $T(n) \le c(n-a)\lg(n-a)$

$$
\begin{array}{llll}
T(n) & \le & \displaystyle c(n+34-2a)\lg(n+34-2a) & \\
     & \le & \displaystyle c(n-a)\lg(n-a) & (a \ge 34)
\end{array}
$$

### 4.3-7

> Using the master method in Section 4.5, you can show that the solution to the recurrence $T(n)=4T(n/3)+N$ is $T(n)=\Theta(n^{\log_34})$. Show that a substitution proof with the assumption $T(n) \le n^{\log_34}$ fails. Then show how to subtract off a lower-order term to make a substitution proof work.

Suppose $T(n) \le cn^{\log_34}$

$$
T(n) \le cn^{\log_34}+n
$$

Suppose $T(n) \le cn^{\log_34} - an$

$$
\begin{array}{llll}
T(n) & \le & \displaystyle cn^{\log_34} + (1 - \frac{4}{3})n & \\
     & \le & \displaystyle cn^{\log_34} - an & (a \ge 3)
\end{array}
$$

### 4.3-8

> Using the master method in Section 4.5, you can show that the solution to the recurrence $T(n)=4T(n/2)+n$ is $T(n)=\Theta(n^2)$. Show that a substitution proof with the assumption $T(n)=cn^2$ fails. Then show how to subtract off a lower-order term to make a substitution proof work.

Suppose $T(n) \le cn^2$

$$
T(n) \le cn^2+n
$$

Suppose $T(n) \le cn^2 - an$

$$
\begin{array}{llll}
T(n) & \le & cn^2 + (1 - 2a)n & \\
     & \le & cn^2 - an & (a \ge \frac{1}{3})
\end{array}
$$

### 4.3-9

> Solve the recurrence $T(n)=3T(\sqrt{n}) + \log n$ by making a change of variables. Your solution should be  are integral.

Let $n=2^m$

$T(2^m)=3T(2^{m/2}) + m$

$S(m) = 3S(m/2)+m$

$S(m)=\Theta(m^{\lg 3})$

$T(n) = \Theta({\lg^{\lg 3} n})$
