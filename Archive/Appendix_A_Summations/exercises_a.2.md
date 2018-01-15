## A.2 Bounding summations

### A.2-1

> Show that $$\sum_{k=1}^n 1/k^2$$ is bounded above by a constant.

$$1/k^2$$ is a monotonically decreasing function,

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n \frac{1}{k^2} &=& 1 + \displaystyle \sum_{k=2}^n \frac{1}{k^2} \\
&\le& 1 + \displaystyle \int_{1}^{n} \frac{1}{x^2} dx \\
&=& \displaystyle 1 + \left ( -\frac{1}{x} \Bigr|_1^n \right ) \\
&=& \displaystyle 2 - \frac{1}{n} \\
&<& 2
\end{array}
$$

### A.2-2

> Find an asymptotic upper bound on the summation

> $$\displaystyle \sum_{k=0}^{\lfloor \lg n \rfloor} \lceil n / 2^k \rceil$$.

$$
\begin{array}{rll}
\displaystyle \sum_{k=0}^{\lfloor \lg n \rfloor} \lceil n / 2^k \rceil &\le& \displaystyle \int_{-1}^{\lfloor \lg n \rfloor} -\frac{2^{-x}}{\ln2}dx \\
&\le& \displaystyle \frac{2}{\ln2} - \frac{1}{\ln) \cdot n} \\
&<& \displaystyle \frac{2}{\ln2}
\end{array}
$$

### A.2-3

> Show that the $$n$$th harmonic number is $$\Omega(\lg n)$$ by splitting the summation.

$$
\begin{array}{rll}
\displaystyle \sum_{i=1}^n \frac{1}{k} &\ge& \displaystyle \sum_{i=0}^{\lfloor \lg n \rfloor - 1} \sum_{j=}^{2^i-1} \frac{1}{2^i+j} \\
&\ge& \displaystyle \sum_{i=0}^{\lfloor \lg n \rfloor - 1} \sum_{j=}^{2^i-1} \frac{1}{2^{i+1}} \\
&=& \displaystyle \frac{1}{2} \sum_{i=0}^{\lfloor \lg n \rfloor - 1} \sum_{j=}^{2^i-1} \frac{1}{2^i} \\
&=& \displaystyle \frac{1}{2} \sum_{i=0}^{\lfloor \lg n \rfloor - 1} 1 \\
&=& \displaystyle \frac{1}{2} \lfloor \lg n \rfloor
\end{array}
$$

### A.2-4

> Approximate $$\sum_{k=1}^n k^3$$ with an integral.

$$k^3$$ is a monotonically increasing function,

$$
\begin{array}{rrlll}
\displaystyle \int_{0}^n x^3 dx &\le& \displaystyle \sum_{k=1}^n k^3 &\le& \displaystyle \int_{1}^{n+1} x^3 dx \\
\displaystyle \frac{1}{4}x^4 \Bigr|_{0}^n &\le& \displaystyle \sum_{k=1}^n k^3 &\le& \displaystyle \frac{1}{4}x^4 \Bigr|_{1}^{n+1} \\
\displaystyle \frac{1}{4}n^4 &\le& \displaystyle \sum_{k=1}^n k^3 &\le& \displaystyle \frac{1}{4}(n+1)^4 - \frac{1}{4} \\
\end{array}
$$

### A.2-5

> Why didn’t we use the integral approximation (A.12) directly on $$\sum_{k=1}^n 1/k$$ to obtain an upper bound on the $$n$$th harmonic number?

Because we cannot calculate $$\ln0$$.
