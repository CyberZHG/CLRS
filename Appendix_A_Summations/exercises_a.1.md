## A.1 Summation formulas and properties

### A.1-1

> Find a simple formula for $$\sum_{k=1}^n(2k-1)$$.

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n(2k-1) &=& \displaystyle 2\sum_{k=1}^nk-\sum_{k=1}^n1 \\
&=& \displaystyle 2 \cdot \frac{n(n+1)}{2} - n \\
&=& n^2
\end{array}
$$

### A.1-2 $$\star$$

> Show that $$\sum_{k=1}^n 1/(2k-1) = \ln(\sqrt{n})+O(1)$$ by manipulating the harmonic series.

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n \frac{1}{2k-1} &=& \displaystyle \sum_{k=1}^{2n} \frac{1}{k} - \sum_{k=1}^n \frac{1}{2k} \\
&=& \displaystyle \ln(2n) - \frac{1}{2}\ln n + O(1) \\
&=& \displaystyle \frac{1}{2}\ln(n) + O(1) \\
&=& \displaystyle \ln(\sqrt{n}) + O(1) \\
\end{array}
$$

### A.1-3

> Show that $$\sum_{k=0}^\infty k^2 x^k = x(1+x)/(1-x)^3$$ for $$0 < |x| < 1$$.

First we need:

$$
\begin{array}{rlllllll}
\displaystyle \sum_{k=0}^\infty kx^k &=&x+ &2x^2 + &3x^3 + &4x^4 + \dots \\
\displaystyle \left (\sum_{k=0}^\infty kx^k\right)x &=& & x^2 + &2x^3 + &3x^4 + \dots \\
\displaystyle \left (\sum_{k=0}^\infty kx^k\right) (1 - x) &=&x+ &x^2 + &x^3 + &x^4 + \dots \\
\displaystyle \left (\sum_{k=0}^\infty kx^k\right) (1 - x) &=& \displaystyle \frac{x}{1-x} \\
\displaystyle \sum_{k=0}^\infty kx^k &=& \displaystyle \frac{x}{(1-x)^2}
\end{array}
$$

Then:

$$
\begin{array}{rlllllll}
\displaystyle \sum_{k=0}^\infty k^2 x^k &=& x + 4x^2 + 9x^3 + 16x^4 + \dots \\
&=& x+ x^2 + x^3 + x^4 + \dots \\
&& + 3x^2 + 3x^3 + 3x^4 + \dots \\
&& + 5x^3 + 5x^4 + \dots \\
&=& \displaystyle \sum_{k=0}^\infty (2k+1) \cdot \frac{x^{k+1}}{1-x} \\
&=& \displaystyle \frac{x}{1-x} \left ( 2\sum_{k=0}^\infty k x^k + \sum_{k=0}^\infty x^k \right ) \\
&=& \displaystyle \frac{x}{1-x} \left ( \frac{2x}{(1-x)^2} + \frac{1}{1-x} \right ) \\
&=& \displaystyle \frac{x(1+x)}{(1-x)^3}
\end{array}
$$

### A.1-4 $$\star$$

> Show that $$\sum_{k=0}^\infty (k-1)/2^k=0$$.

$$
\sum_{k=0}^\infty \frac{1}{2^k} = 1 \cdot \frac{1}{1 - \frac{1}{2}} = 2
$$

$$
\begin{array}{rll}
\displaystyle \sum_{k=0}^\infty \frac{k}{2^k} &=& \displaystyle \frac{1}{2^1} + \frac{2}{2^2} + \frac{3}{2^3} + \dots \\
\displaystyle \frac{1}{2} \left (\sum_{k=0}^\infty \frac{k}{2^k} \right ) &=& \displaystyle \frac{1}{2^2} + \frac{2}{2^3} + \frac{3}{2^4} + \dots \\
&=& \displaystyle \frac{1}{2} \cdot \frac{1}{1 - \frac{1}{2}} \\
&=& 1 \\
\displaystyle \sum_{k=0}^\infty \frac{k}{2^k} &=& 2
\end{array}
$$

$$
\sum_{k=0}^\infty \frac{k-1}{2^k} = \left ( \sum_{k=0}^\infty \frac{k}{2^k} \right ) - \left ( \sum_{k=0}^\infty \frac{1}{2^k} \right ) = 2 - 2 = 0
$$

### A.1-5 $$\star$$

> Evaluate the sum $$\sum_{k=1}^\infty (2k + 1)x^{2k}$$.

If $$|x| = 0$$, the result is $$0$$.

If $$|x| \ge 1$$, the result is $$+\infty$$.

If $$0 < |x| < 1$$:

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^\infty (2k + 1)x^{2k} &=& 3x^2 + 5x^4 + 7x^6 + \dots \\
\displaystyle x^2 \left ( \sum_{k=1}^\infty (2k + 1)x^{2k} \right ) &=& 3x^4 + 5x^6 + \dots \\
\displaystyle (1-x^2) \left ( \sum_{k=1}^\infty (2k + 1)x^{2k} \right ) &=& 3x^2 + 2x^4 + 2x^6 + \dots \\
&=& \displaystyle \frac{3x^2-x^4}{1-x^2} \\
\displaystyle \sum_{k=1}^\infty (2k + 1)x^{2k} &=& \displaystyle \frac{3x^2-x^4}{(1-x^2)^2}
\end{array}
$$

### A.1-6

> Prove that $$\sum_{k=1}^n O(f_k(i)) = O(\sum_{k=1}^n f_k(i))$$ by using the linearity property of summations.

$$
\sum_{k=1}^n \Theta(f(k)) = \Theta(\sum_{k=1}^n f(k))
$$

### A.1-7

> Evaluate the product $$\prod_{k=1}^n 2 \cdot 4^k$$.

$$
\prod_{k=1}^n 2 \cdot 4^k = 2^n \cdot 4^{\sum_{k=1}^n k} = 2^{n^2 + 2n}
$$

### A.1-8 $$\star$$

> Evaluate the product $$\prod_{k=2}^n (1-1/k^2)$$.

$$
\begin{array}{rll}
\displaystyle \prod_{k=2}^n (1-1/k^2) &=& \displaystyle \prod_{k=2}^n \frac{(k+1)(k-1)}{k^2} \\
&=& \displaystyle \frac{1}{n!^2} \prod_{k=2}^n (k+1) \prod_{k=2}^n (k-1) \\ 
&=& \displaystyle \frac{1}{n!^2} \prod_{k=3}^{n+1} k \prod_{k=1}^{n-1} k \\ 
&=& \displaystyle \frac{1}{n!^2} \cdot \frac{n+1}{2n} \cdot \prod_{k=1}^{n} k \prod_{k=1}^{n} k \\ 
&=& \displaystyle \frac{n+1}{2n}
\end{array}
$$
