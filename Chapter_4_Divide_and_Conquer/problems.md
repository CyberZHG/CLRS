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

### 4-5 Chip testing

> Professor Diogenes has $$n$$ supposedly identical integrated-circuit chips that in principle are capable of testing each other. The professor’s test jig accommodates two chips at a time. When the jig is loaded, each chip tests the other and reports whether it is good or bad. A good chip always reports accurately whether the other chip is good or bad, but the professor cannot trust the answer of a bad chip. Thus, the four possible outcomes of a test are as follows:

> | Chip A says | Chip B says | Conclusion |
  |:------------|:------------|:-----------|
  |B is good |A is good |both are good, or both are bad|
  |B is good |A is bad |at least one is bad|
  |B is bad |A is good |at least one is bad|
  |B is bad |A is bad |at least one is bad|
  
> __a__. Show that if more than $$n/2$$ chips are bad, the professor cannot necessarily determine which chips are good using any strategy based on this kind of pairwise test. Assume that the bad chips can conspire to fool the professor.

Symmetric.

> __b__. Consider the problem of finding a single good chip from among $$n$$ chips, assuming that more than $$n/2$$ of the chips are good. Show that $$\left \lfloor n / 2 \right \rfloor$$ pairwise tests are sufficient to reduce the problem to one of nearly half the size.

First assume $$n$$ is even, then divide the chips in two groups, test each pair of chips with the same index from the two groups. If the result are is good, we keep one of chips; otherwise we remove both the chips. If $$n$$ is odd, if there are odd number of chips left after the selections, then there must be more good chips than bad chips, we can simply discard the odd chip; otherwise if there are even number of chips, then if there are equal number of good and bad chips, the odd one must be good, and if there are more good chips than bad chips, the difference must be larger or equal to 2, therefore we can safely add the odd one to the set for next iteration.

$$T(n)=T(n/2)+n/2 = \sum_{i=0}^{\lg n - 1} \frac{n}{2^i} \le n/2$$

```python
import random


class Chip:
    def __init__(self, state):
        self.state = state

    def check(self, other):
        if self.state:
            return other.state
        return random.randint(0, 1)


def check(chip_a, chip_b):
    return chip_a.check(chip_b) and chip_b.check(chip_a)


def choose_good_chip(chips):
    assert(len(chips) > 0)
    if len(chips) == 1:
        return chips[0]
    mid = len(chips) // 2
    next_chips = []
    for i in range(mid):
        if check(chips[i], chips[mid + i]):
            next_chips.append(chips[i])
    if len(chips) % 2 == 1 and len(next_chips) % 2 == 0:
        next_chips.append(chips[-1])
    return choose_good_chip(next_chips)
```

> __c__. Show that the good chips can be identified with $$\Theta(n)$$ pairwise tests, assuming that more than $$n/2$$ of the chips are good. Give and solve the recurrence that describes the number of tests.

Based on master method, $$T(n)=T(n/2)+n/2=\Theta(n)$$

### 4-6 Monge arrays

> An $$m \times n$$ array $$A$$ of real numbers is a __Monge array__ if for all $$i$$, $$j$$, $$k$$ and $$l$$ such that $$1 \le i < k \le m$$ and $$1 \le j < l \le n$$, we have

> $$A[i,j]+A[k,l] \le A[i,l]+A[k,j]$$.

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

If $$A[i,j]+A[i+1,j+1] \ge A[i,j+1]+A[i+1,j]$$, it contradicts the definition of Monge arrays.

If $$A[i,j]+A[i+1,j+1] \le A[i,j+1]+A[i+1,j]$$, 

suppose $$A[i,l-1]+A[k-1,l] \le A[i,l]+A[k-1,l-1]$$,

since $$A[k-1,l-1]+A[k,l] \le A[k-1,l]+A[k,l-1]$$,

therefore $$A[i,l-1]+A[k,l] \le A[i,l]+A[k,l-1]$$;

suppose $$A[i, j]+A[k, l-1] \le A[i, l-1] + A[k, j]$$,

since $$A[i,l-1]+A[k,l] \le A[i,l]+A[k,l-1]$$,

therefore $$A[i,j]+A[k,l] \le A[i,l]+A[k,j]$$.

> __b__. The following array is not Monge. Change one element in order to make it Monge. (Hint: Use part (a).)

> $$\begin{matrix}
37 & 23 & 22 & 32 \\
21 & 6 & 7 & 10 \\
53 & 34 & 30 & 31 \\
32 & 13 & 9 & 6 \\
43 & 21 & 15 & 8 \\
\end{matrix}$$

$$
\begin{matrix}
37 & 23 & \mathbf{24} & 32 \\
21 & 6 & 7 & 10 \\
53 & 34 & 30 & 31 \\
32 & 13 & 9 & 6 \\
43 & 21 & 15 & 8 \\
\end{matrix}
$$

> __c__. Let $$f(i)$$ be the index of the column containing the leftmost minimum element of row $$i$$ . Prove that $$f(1) \le f(2) \le \dots \le f(m)$$ for any $$m \times n$$ Monge array.

Let $$i$$ and $$j$$ be the index of leftmost minimal elements on row $$a$$ and $$b$$, suppose $$a < b$$ and $$i \ge j$$.

$$A[a,i] \le A[a,j]$$,

$$A[b,j] \le A[b,i]$$,

$$A[a,j] + A[b,i] \le A[a,i]+ A[b,j]$$,

the inequality is satisfied only when $$i = j$$, therefore $$i \le j$$.

> __d__. Here is a description of a divide-and-conquer algorithm that computes the leftmost minimum element in each row of an $$m \times n$$ Monge array $$A$$:

> > Construct a submatrix $$A'$$ of $$A$$ consisting of the even-numbered rows of $$A$$. Recursively determine the leftmost minimum for each row of $$A$$. Then compute the leftmost minimum in the odd-numbered rows of $$A$$.

> Explain how to compute the leftmost minimum in the odd-numbered rows of $$A$$ (given that the leftmost minimum of the even-numbered rows is known) in $$O(m+n)$$ time.

Search in the interval $$[f(i-1), f(i+1)]$$.

$$c_1m/2 + c_2n = O(m+n)$$

> __e__. Write the recurrence describing the running time of the algorithm described in part (d). Show that its solution is $$O(m+n\log m)$$.

$$
\begin{array}{rll}
T(m,n)&=&T(m/2,n) + m + n \\
&=&\sum_{i=0}^{\lg m - 1}(\frac{m}{2^i} + n) \\
&=&\sum_{i=0}^{\lg m - 1}(\frac{m}{2^i} + n) \\
&=&\frac{1}{1-1/2}m + n \lg m \\
&=&2m + n \lg m \\
&=&O(m+n\log m) \\
\end{array}
$$

```python
def get_min_index(arr):
    def get_min_index_rec(idx):
        if len(idx) == 1:
            min_idx = 0
            for j in range(1, len(arr[0])):
                if arr[idx[0]][j] < arr[idx[0]][min_idx]:
                    min_idx = j
            return [min_idx]
        sub_idx = [idx[i] for i in range(len(idx)) if i % 2 == 0]
        sub_min_idx = get_min_index_rec(sub_idx)
        sub_min_idx.append(len(arr[0]) - 1)
        min_idx = [sub_min_idx[i//2] for i in range(len(idx))]
        for i in range(1, len(idx), 2):
            for j in range(sub_min_idx[i//2] + 1, sub_min_idx[i//2 + 1] + 1):
                if arr[idx[i]][j] < arr[idx[i]][min_idx[i]]:
                    min_idx[i] = j
        return min_idx
    return get_min_index_rec([i for i in range(len(arr))])
```
