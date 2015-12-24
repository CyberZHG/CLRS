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

> __b__. $$T(n) = 3T(n/3) + n/\lg n$$.

> __c__. $$T(n) = 4T(n/2) + n^2\sqrt{n}$$.

> __d__. $$T(n) = 3T(n/3-2) + n/2$$.

> __e__. $$T(n) = 2T(n/2) + n/\lg n$$.

> __f__. $$T(n) = T(n/2) + T(n/4) + T(n/8) + n$$.

> __g__. $$T(n) = T(n-1) + 1/n$$.

> __h__. $$T(n) = T(n-1) + \lg n$$.

> __i__. $$T(n) = T(n-2) + 1/\lg n$$.

> __j__. $$T(n) = \sqrt{n} T(\sqrt{n}) + n$$.

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

> __c__. Show that

> $$\mathcal{F}(z)=\sum_{i=0}^{\infty}\frac{1}{\sqrt{5}}(\phi^i-\hat{\phi^i})z^i$$.

> __d__. Use part (c) to prove that $$F_i=\phi^i/\sqrt{5}$$ for $$i>0$$, rounded to the nearest integer. (Hint: Observe that $$| \hat{\phi} | < 1$$.)

### 4-5 Chip testing

> Professor Diogenes has n supposedly identical integrated-circuit chips that in principle are capable of testing each other. The professor’s test jig accommodates two chips at a time. When the jig is loaded, each chip tests the other and reports whether it is good or bad. A good chip always reports accurately whether the other chip is good or bad, but the professor cannot trust the answer of a bad chip. Thus, the four possible outcomes of a test are as follows:

> | Chip A says | Chip B says | Conclusion |
  |:------------|:------------|:-----------|
  |B is good |A is good |both are good, or both are bad|
  |B is good |A is bad |at least one is bad|
  |B is bad |A is good |at least one is bad|
  |B is bad |A is bad |at least one is bad|
  
> __a__. Show that if more than $$n/2$$ chips are bad, the professor cannot necessarily determine which chips are good using any strategy based on this kind of pairwise test. Assume that the bad chips can conspire to fool the professor.

> __b__. Consider the problem of finding a single good chip from among $$n$$ chips, assuming that more than $$n/2$$ of the chips are good. Show that $$\left \lfloor n / 2 \right \rfloor$$ pairwise tests are sufficient to reduce the problem to one of nearly half the size.

> __c__. Show that the good chips can be identified with $$\Theta(n)$$ pairwise tests, assuming that more than $$n/2$$ of the chips are good. Give and solve the recurrence that describes the number of tests.

### 4-6 Monge arrays

> An $$m \times n$$ array $$A$$ of real numbers is a __Monge array__ if for all $$i$$, $$j$$, $$k$$ and $$l$$ such that $$1 \le i < k \le m$$ and $$1 \le j < l \le n$$, we have

> $$A[i,j]+a[k,l] \le A[i,l]+A[k,j]$$.

> In other words, whenever we pick two rows and two columns of a Monge array and consider the four elements at the intersections of the rows and the columns, the sum of the upper-left and lower-right elements is less than or equal to the sum of the lower-left and upper-right elements. For example, the following array is Monge:

> $$\begin{matrix}
10 & 17 & 13 & 28 & 23 \\
17 & 22 & 16 & 29 & 23 \\
24 & 28 & 22 & 34 & 24 \\
11 & 13 & 6 & 17 & 7 \\
45 & 44 & 32 & 37 & 23 \\
36 & 33 & 19 & 21 & 6 \\
75 & 66 & 51 & 53 & 34 \\
\end{matrix}$$

> __a__. Prove that an array is Monge if and only if for all $$i=1,2,\dots,m-1$$ and $$j=1,2,\dots,n-1$$, we have

> $$A[i,j]+A[i+1,j+1] \le A[i,j+1]+A[i+1,j]$$.

> (Hint: For the "if" part, use induction separately on rows and columns.)

> __b__. The following array is not Monge. Change one element in order to make it Monge. (Hint: Use part (a).)

> $$\begin{matrix}
37 & 23 & 22 & 32 \\
21 & 6 & 7 & 10 \\
53 & 34 & 30 & 31 \\
32 & 13 & 9 & 6 \\
43 & 21 & 15 & 8 \\
\end{matrix}$$


> __c__. Let $$f(i)$$ be the index of the column containing the leftmost minimum element of row $$i$$ . Prove that $$f(1) \le f(2) \le \dots \le f(m)$$ for any $$m \times n$$ Monge array.

> __d__. Here is a description of a divide-and-conquer algorithm that computes the leftmost minimum element in each row of an $$m \times n$$ Monge array $$A$$:

> > Construct a submatrix $$A'$$ of $$A$$ consisting of the even-numbered rows of $$A$$. Recursively determine the leftmost minimum for each row of $$A$$. Then compute the leftmost minimum in the odd-numbered rows of $$A$$.

> Explain how to compute the leftmost minimum in the odd-numbered rows of $$A$$ (given that the leftmost minimum of the even-numbered rows is known) in $$O(m+n)$$ time.

> __e__. Write the recurrence describing the running time of the algorithm described in part (d). Show that its solution is $$O(m+n\log m)$$.

