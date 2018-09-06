## 3.1 Asymptotic notation

### 3.1-1

> Let $f(n)$ and $g(n)$ be asymptotically nonnegative functions. Using the basic definition of $\Theta$-notation, prove that $\max(f(n), g(n)) = \Theta (f(n) + g(n))$.

$0.5 \cdot (f(n) + g(n)) \le \max(f(n), g(n)) \le 1 \cdot (f(n) + g(n))$

### 3.1-2

> Show that for any real constants $a$ and $b$, where $b>0$, $(n+a)^b=\Theta(n^b)$.

If $a > 0$, then $(n + a) ^ b < (n + n) ^ b = (2 n)^b = 2^b \cdot n^b$;

If $a < 0$, let $a := -a$, then $(n - a) ^ b > (n - 0.5n) ^ b = (0.5 n)^b = 0.5^b \cdot n^b$,

Since $0.5^b \cdot n^b \le (n+a)^b \le 2^b \cdot n^b$, therefore $(n+a)^b=\Theta(n^b)$.

### 3.1-3

> Explain why the statement, "The running time of algorithm $A$ is at least $O(n^2)$," is meaningless.

$O$ is an upper bound, which means $A$ could be $\Omega(1)$.

### 3.1-4

> Is $2^{n+1}=O(2^n)$? Is $2^{2n}=O(2^n)$?

* $2^{n+1}=O(2^n)$?

$1 \cdot 2^n \le 2^{n+1} \le 2 \cdot 2^n$, thus $2^{n+1}=O(2^n)$.

* $2^{2n}=O(2^n)$?

$2^{2n} \le c \cdot 2^n$

$2^n \le c$ which is impossible, thus $2^{2n} \ne O(2^n)$.

### 3.1-5

> Prove Theorem 3.1.

> Theorem 3.1
>
> For any two function $f(n)$ and $g(n)$, we have $f(n)=\Theta(g(n))$ if and only if $f(n)=O(g(n))$ and $f(n)=\Omega(g(n))$.

$f(n)=O(g(n))$ implies $0 \le f(n) \le c\_2 g(n)$

$f(n)=\Omega(g(n))$ implies $0 \le c\_1 g(n) \le f(n)$

Thus $c\_1 g(n) \le f(n) \le c\_2 g(n)$, $f(n)=\Theta(g(n))$, and vice versa.

### 3.1-6

> Prove that the running time of an algorithm is $\Theta(g(n))$ if and only if its worst-case running time is $O(g(n))$ and its best-case running time is $\Omega(g(n))$.

Theorem 3.1

### 3.1-7

> Prove that $o(g(n)) \cap \omega(g(n))$ is the empty set.

There is no $f(n)$ that $f(n) < g(n)$ and $f(n) > g(n)$.

### 3.1-8

> We can extend our notation to the case of two parameters $n$ and $m$ that can go to infinity independently at different rates. For a given function $g(n,m)$, we denote by $O(g(n,m))$ the set of functions
>
> $O(g(n,m))=\\{f(n,m)$: there exist positive constants $c$, $n\_0$, and $m\_0$ such that $0 \le f(n,m) \le c g(n,m)$ for all $n \ge n\_0$ or $m \ge m\_0$ $\\}$.
>
> Give corresponding definitions for $\Omega(g(n,m))$ and $\Theta(g(n,m))$.


$\Omega(g(n,m))=\\{f(n,m)$: there exist positive constants $c$, $n\_0$, and $m\_0$ such that $0 \le c g(n,m) \le f(n,m)$ for all $n \ge n\_0$ or $m \ge m\_0$ $\\}$.

$\Theta(g(n,m))=\\{f(n,m)$: there exist positive constants $c\_1$, $c\_2$, $n\_0$, and $m\_0$ such that $c\_1 g(n,m) \le f(n,m) \le c\_2 g(n,m)$ for all $n \ge n\_0$ or $m \ge m\_0$ $\\}$.
