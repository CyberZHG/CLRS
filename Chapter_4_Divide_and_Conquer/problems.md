## Problems

### 4-1 Recurrence examples

> Give asymptotic upper and lower bounds for $$T(n)$$ in each of the following recurrences. Assume that $$T(n)$$ is constant for $$n \le 2$$. Make your bounds as tight as possible, and justify your answers.

> __a__. $$T(n)=2T(n/2)+n^4$$.

$$\Theta(n^4)$$

> __b__. $$T(n)=T(7n/10)+n$$.

$$\Theta(n)$$

> __c__. $$T(n)=16T(n/4)+n^2$$.

$$\Theta(n^2 \lg n)$$

> __d__. $$T(n)=7T(n/3)+n^2$$.

$$\Theta(n^2)$$

> __e__. $$T(n)=7T(n/2)+n^2$$.

$$\Theta(n^{\lg 7})$$

> __f__. $$T(n)=2T(n/4)+\sqrt{n}$$.

$$\Theta(\sqrt{n}\lg n)$$

> __g__. $$T(n)=T(n-2)+n^2$$.

$$\Theta(n^3)$$

### 4-2 Parameter-passing costs

> Throughout this book, we assume that parameter passing during procedure calls takes constant time, even if an $$N$$-element array is being passed. This assumption is valid in most systems because a pointer to the array is passed, not the array itself.
> 
> This problem examines the implications of three parameter-passing strategies:
> 
> 1. An array is passed by pointer. Time $$=\Theta(1)$$.
> 2. An array is passed by copying. Time $$=\Theta(N)$$ where $$N$$ is the size of the array.
> 3. An array is passed by copying only the subrange that might be accessed by the called procedure. Time D $$=\Theta(q-p+1)$$ if the subarray $$A[p \dots q]$$ is passed.

> a. Consider the recursive binary search algorithm for finding a number in a sorted array (see Exercise 2.3-5). Give recurrences for the worst-case running times of binary search when arrays are passed using each of the three methods above, and give good upper bounds on the solutions of the recurrences. Let $$N$$ be the size of the original problem and $$n$$ be the size of a subproblem.

1. $$T(n)=T(n/2)+1=\Theta(\lg n)$$
2. $$T(n)=T(n/2)+N=\Theta(n \lg n)$$
3. $$T(n)=T(n/2)+n=\Theta(n)$$

> b. Redo part (a) for the MERGE-SORT algorithm from Section 2.3.1.

1. $$T(n)=2T(n/2)+n+c=2T(n/2)+n=\Theta(n\lg n)$$
2. $$T(n)=2T(n/2)+n+N=2T(n/2)+N=\Theta(n^2)$$
3. $$T(n)=2T(n/2)+n+n=2T(n/2)+n=\Theta(n\lg n)$$

### 4-3 More recurrence examples

> Give asymptotic upper and lower bounds for $$T(n)$$ in each of the following recurrences. Assume that $$T(n)$$ is constant for sufficiently small $$n$$. Make your bounds as tight as possible, and justify your answers.

> __a__. $$T(n) = 4T(n/3) + n\lg n$$.

$$\Theta(n^{\log_3^4})$$

> __b__. $$T(n) = 3T(n/3) + n/\lg n$$.

For harmonic series:

$$
\ln (n+1) \le \int_1^{n+1} \frac{1}{t}dt \le \sum_{i=1}^n \frac{1}{i} \le 1 + \int_1^n \frac{1}{t}dt = 1 + \ln n
$$

Therefore, harmonic series are $$\Theta(\lg n)$$

$$
\begin{array}{rll}
T(n) & = & n\sum_{i=0}^{\log_3{n} - 1}\frac{1}{\lg \frac{n}{3^i}} \\
& = & \Theta(n\sum_{i=0}^{\log_3{n} - 1}\frac{1}{\log_3 \frac{n}{3^i}}) \\
& = & \Theta(n\sum_{i=1}^{\log_3{n}}\frac{1}{i}) \\
& = & \Theta(n\lg \lg n)
\end{array}
$$

> __c__. $$T(n) = 4T(n/2) + n^2\sqrt{n}$$.

$$\Theta(n^2\sqrt{n})$$

> __d__. $$T(n) = 3T(n/3-2) + n/2$$.

$$\Theta(n\lg n)$$

> __e__. $$T(n) = 2T(n/2) + n/\lg n$$.

Same as __b__,

$$\Theta(n\lg \lg n)$$

> __f__. $$T(n) = T(n/2) + T(n/4) + T(n/8) + n$$.

$$\Theta(n)$$

> __g__. $$T(n) = T(n-1) + 1/n$$.

$$
\begin{array}{rll}
T(n) & = & \sum_{i=1}^n \frac{1}{i} \\
& = & \Theta(\lg n)
\end{array}
$$

> __h__. $$T(n) = T(n-1) + \lg n$$.

$$
\begin{array}{rll}
T(n) & = & \sum_{i=1}^n \lg{i} \\
& = & \lg{n!} \\
& \le & \lg{n^n} \\
& = & \Theta(n\lg n)
\end{array}
$$

> __i__. $$T(n) = T(n-2) + 1/\lg n$$.

$$
\begin{array}{rll}
T(n) & = & \sum_{i=1}^{n/2} \frac{1}{\lg{2i}} \\
& = & \Theta(\lg \lg n)
\end{array}
$$

> __j__. $$T(n) = \sqrt{n} T(\sqrt{n}) + n$$.

Let $$n = 2^m$$,

$$
\begin{array}{rll}
T(n) &=& \sqrt{n} T(\sqrt{n}) + n \\
T(2^m) &=& 2^{m/2}T(2^{m/2}) + 2^m \\
\frac{T(2^m)}{2^m} &=& \frac{T(2^{m/2})}{2^{m/2}} + 1 \\
\end{array}
$$

Let $$S(m)=\frac{T(2^m)}{2^m}$$, $$ S(m) = S(m/2) + 1 = \Theta(\lg m)$$,

$$\therefore$$ $$T(2^m)=\Theta(2^m \lg m)$$

$$\therefore$$ $$T(n)=\Theta(n \lg \lg n)$$

### 4-4 Fibonacci numbers

> This problem develops properties of the Fibonacci numbers, which are defined by recurrence (3.22). We shall use the technique of generating functions to solve the Fibonacci recurrence. Define the __generating function__ (or __formal power series__) $$\mathcal{F}$$ as

> $$
\begin{array}{lll}
\mathcal{F}(z) & = & \sum_{i=0}^\infty F_i z^i \\
               & = & 0 + z + z^2 + 2z^3 + 3z^4 + 5z^5 + 8z^6 + 13z^7 + 21z^8+\dots
\end{array}
$$

> where $$\mathcal{F}_i$$ is the $$i$$th Fibonacci number.

> __a__. Show that $$\mathcal{F}(z) = z + z \mathcal{F}(z) + z^2\mathcal{F}(z)$$.

$$
\begin{array}{rll}
z + z \mathcal{F}(z) + z^2\mathcal{F}(z) &=& z + z\sum_{i=0}^\infty F_i z^i + z^2\sum_{i=0}^\infty F_i z^i \\ 
&=& z + \sum_{i=1}^\infty F_{i-1} z^i + \sum_{i=2}^\infty F_{i-2} z^i \\
&=& z + z^2 + \sum_{i=2}^\infty(F_{i-1} + F_{i-2})z^i \\
&=& z + z^2 + \sum_{i=2}^\infty F_iz^i \\
&=& \sum_{i=0}^\infty F_iz^i \\
& = & \mathcal{F}(z)
\end{array}
$$

> __b__. Show that
>
> $$
\begin{array}{lll}
\mathcal{F}(z) & = & \frac{z}{1-z-z^2} \\
               & = & \frac{z}{(1-\phi z)(1 - \hat{\phi}z)} \\
               & = & \frac{1}{\sqrt{5}}(\frac{1}{1-\phi z}-\frac{1}{1-\hat{\phi} z}) \\
\end{array}
$$

> $$\phi=\frac{1+\sqrt{5}}{2}=1.61803\dots$$

> and

> $$\hat{\phi}=\frac{1-\sqrt{5}}{2}=-0.61803\dots$$

$$
\begin{array}{rll}
\mathcal{F}(z) &=& z + z \mathcal{F}(z) + z^2\mathcal{F}(z) \\
(1-z-z^2)\mathcal{F}(z) &=& z \\
\mathcal{F}(z) &=& \frac{z}{1-z-z^2}
\end{array}
$$

$$
\begin{array}{rll}
(1-\phi z)(1 - \hat{\phi}z) &=& 1 - (\phi + \hat{\phi})z + \phi \hat{\phi} z^2 \\
\phi + \hat{\phi} &=& 1 \\
\phi \hat{\phi} &=& \frac{1-5}{4} = -1 \\
\therefore (1-\phi z)(1 - \hat{\phi}z) &=& 1 - z - z^2 \\
\therefore \mathcal{F}(z) & = & \frac{z}{(1-\phi z)(1 - \hat{\phi}z)}
\end{array}
$$

$$
\begin{array}{rll}
\frac{1}{\sqrt{5}}(\frac{1}{1-\phi z}-\frac{1}{1-\hat{\phi} z}) &=& \frac{1}{\sqrt{5}}(\frac{(\hat{\phi} - \phi)z}{(1-\phi z)(1-\hat{\phi} z)}) \\
\mathcal{F}(z) &=& \frac{1}{\sqrt{5}}(\frac{1}{1-\phi z}-\frac{1}{1-\hat{\phi} z}) \\
\end{array}
$$

> __c__. Show that

> $$\mathcal{F}(z)=\sum_{i=0}^{\infty}\frac{1}{\sqrt{5}}(\phi^i-\hat{\phi^i})z^i$$.

$$\sum_{i=0}^\infty x^i=\frac{1}{1-x}$$,

$$
\begin{array}{rll}
\mathcal{F}(z) &=& \frac{1}{\sqrt{5}}(\frac{1}{1-\phi z}-\frac{1}{1-\hat{\phi} z}) \\
&=& \sum_{i=0}^{\infty}\frac{1}{\sqrt{5}}(\phi^i-\hat{\phi^i})z^i
\end{array}
$$

> __d__. Use part (c) to prove that $$F_i=\phi^i/\sqrt{5}$$ for $$i>0$$, rounded to the nearest integer. (Hint: Observe that $$| \hat{\phi} | < 1$$.)

$$\frac{\hat{\phi^i}}{\sqrt{5}} \le 0.5$$
