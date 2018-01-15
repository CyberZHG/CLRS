## Problems

### A-1 Bounding summations

> Give asymptotically tight bounds on the following summations. Assume that $$r \ge 0$$ and $$s \ge 0$$ are constants.

> __*a*__. $$\displaystyle \sum_{k=1}^n k^r$$.

$$
\begin{array}{rrlll}
\displaystyle \int_{0}^n x^r dx &\le&
\displaystyle \sum_{k=1}^n k^r &\le&
\displaystyle \int_{1}^{n+1} x^r dx \\
\displaystyle \frac{n^{r+1}}{r+1} &\le&
\displaystyle \sum_{k=1}^n k^r &\le&
\displaystyle \frac{(n+1)^{r+1}}{r+1} - \frac{1}{r+1}
\end{array}
$$

$$\Theta(n^r)$$

> __*b*__. $$\displaystyle \sum_{k=1}^n \lg^sk$$.

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n \lg^sk &=& 
\displaystyle \sum_{k=1}^{\lfloor n / 2 \rfloor} \lg^sk + \sum_{k=\lfloor n / 2 \rfloor + 1}^n \lg^sk \\
&\ge& \displaystyle \sum_{k=1}^{\lfloor n / 2 \rfloor} 0 + \sum_{k=\lfloor n / 2 \rfloor + 1}^n \lg^s(\lfloor n / 2 \rfloor) \\
&=& \displaystyle n/2 \cdot \lg^s (n/2) \\
&=& \Omega(n\lg^s n)
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n \lg^sk &=& 
\displaystyle \sum_{k=1}^{\lfloor n / 2 \rfloor} \lg^sk + \sum_{k=\lfloor n / 2 \rfloor + 1}^n \lg^sk \\
&\le& \displaystyle \sum_{k=1}^{\lfloor n / 2 \rfloor} \lg^s(\lfloor n / 2 \rfloor) + \sum_{k=\lfloor n / 2 \rfloor + 1}^n \lg^sn \\
&=& \displaystyle n/2 \cdot \lg^s (n/2) + n/2 \cdot \lg^sn\\
&=& O(n\lg^s n)
\end{array}
$$

Therefore $$\Theta(n \lg^sn)$$

> __*c*__. $$\displaystyle \sum_{k=1}^n k^r \lg^sk$$.

$$\Theta(n^{r+1}\lg^sn)$$
