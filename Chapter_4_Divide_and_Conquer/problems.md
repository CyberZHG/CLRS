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

