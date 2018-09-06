## Problems

### 27-1 Implementing parallel loops using nested parallelism

> Consider the following multithreaded algorithm for performing pairwise addition on n-element arrays $A[1 \dots n]$ and $B[1 \dots n]$, storing the sums in $C[1 \dots n]$:

> ```
SUM-ARRAYS(A, B, C)
1  parallel for i = 1 to A.length
2      C[i] = A[i] + B[i]
```

> __*a*__. Rewrite the parallel loop in SUM-ARRAYS using nested parallelism (__spawn__ and __sync__) in the manner of MAT-VEC-MAIN-LOOP. Analyze the parallelism of your implementation.

```
MAT-VEC-MAIN-LOOP(A, B, C, l, r)
1  if l == r
2      C[l] = A[l] + B[l]
3  mid = (l + r) / 2
4  spwan MAT-VEC-MAIN-LOOP(A, B, C, l, mid)
5  MAT-VEC-MAIN-LOOP(A, B, C, mid + 1, r)
6  sync
```

```
SUM-ARRAYS(A, B, C)
1  len = A.length
2  MAT-VEC-MAIN-LOOP(A, B, C, 1, len)
```

> Consider the following alternative implementation of the parallel loop, which contains a value grain-size to be specified:

> __*b*__. Suppose that we set $grain\text{-}size = 1$. What is the parallelism of this implementation?

$T\_1 = \Theta(n)$, $T\_\infty = \Theta(n)$, $T\_1 / T\_\infty = \Theta(1)$.

> __*c*__. Give a formula for the span of SUM-ARRAYS' in terms of $n$ and $grain\text{-}size$. Derive the best value for grain-size to maximize parallelism.

$T\_\infty(n) = \Theta(\max(grain\text{-}size, n / grain\text{-}size))$

### 27-2 Saving temporary space in matrix multiplication

> The P-MATRIX-MULTIPLY-RECURSIVE procedure has the disadvantage that it must allocate a temporary matrix $T$ of size $n \times n$, which can adversely affect the constants hidden by the $\Theta$-notation. The P-MATRIX-MULTIPLY-RECURSIVE procedure does have high parallelism, however. For example, ignoring the constants in the $\Theta$-notation, the parallelism for multiplying $1000 \times 1000$ matrices comes to approximately $1000^3 / 10^2 = 10^7$, since $\lg 1000 \approx 10$. Most parallel computers have far fewer than 10 million processors.

> __*a*__. Describe a recursive multithreaded algorithm that eliminates the need for the temporary matrix $T$ at the cost of increasing the span to $\Theta(n)$.

Initialize $C = 0$ in parallel in $\Theta(\lg n)$, add __sync__ after the 4th __spawn__, $c\_{11} = c\_{11} + a\_{11} \cdot b\_{11}$, $T\_\infty(n) = 2 T\_\infty(n / 2) + \Theta(\lg n) = \Theta(n)$

> __*b*__. Give and solve recurrences for the work and span of your implementation.

* Work: $T\_1 = \Theta(n^3)$.
* Span: $T\_\infty = \Theta(n)$.

> __*c*__. Analyze the parallelism of your implementation. Ignoring the constants in the $\Theta$-notation, estimate the parallelism on $1000 \times 1000$ matrices. Compare with the parallelism of P-MATRIX-MULTIPLY-RECURSIVE.

Parallelism: $T\_1 / T\_\infty = \Theta(n^2) = 1000^2 = 10^6$.

Most parallel computers still have far fewer than 1 million processors.

### 27-3 Multithreaded matrix algorithms

> __*a*__. Parallelize the LU-DECOMPOSITION procedure on page 821 by giving pseudocode for a multithreaded version of this algorithm. Make your implementation as parallel as possible, and analyze its work, span, and parallelism.

> __*b*__. Do the same for LUP-DECOMPOSITION on page 824.

> __*c*__. Do the same for LUP-SOLVE on page 817.

> __*d*__. Do the same for a multithreaded algorithm based on equation (28.13) for inverting a symmetric positive-definite matrix.

### 27-4 Multithreading reductions and prefix computations

> A __*$\otimes$-reduction*__ of an array $x[1 \dots n]$, where $\otimes$ is an associative operator, is the value 

> $y = x[1] \otimes x[2] \otimes \cdots \otimes x[n]$

> The following procedure computes the $\otimes$-reduction of a subarray $x[i \dots j]$ serially.

> ```
REDUCE(x, i, j)
1  y = x[i]
2  for k = i + 1 to j
3       y = y \otimes x[k]
4  return y
```

> __*a*__. Use nested parallelism to implement a multithreaded algorithm P-REDUCE, which performs the same function with $\Theta(n)$ work and $\Theta(\lg n)$ span. Analyze your algorithm.

```
REDUCE(x, i, j)
1  if i == j
2      return x[i]
3  else if i + 1 == j
4      return x[i] \otimes x[j]
5  mid = (i + j) / 2
6  spawn y1 = REDUCE(x, i, mid)
7  y2 = REDUCE(x, mid + 1, j)
8  sync
9  return y1 \otimes y2
```

> A related problem is that of computing a __*$\otimes$-prefix*__ computation, sometimes called a __*$\otimes$-scan*__, on an array $x[1 \dots n]$, where $\otimes$ is once again an associative operator. The $\otimes$-scan produces the array $y[1 \dots n]$.

> Unfortunately, multithreading SCAN is not straightforward. For example, changing the __for__ loop to a __parallel for__ loop would create races, since each iteration of the loop body depends on the previous iteration. The following procedure P-SCAN-1 performs the $\otimes$-prefix computation in parallel, albeit inefficiently.

> __*b*__. Analyze the work, span, and parallelism of P-SCAN-1.

* Work: $T\_1 = \Theta(n^2)$.
* Span: $T\_\infty = \Theta(\lg n) + \Theta(\lg n) = \Theta(\lg n)$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n^2 / \lg n)$.

> By using nested parallelism, we can obtain a more efficient $\otimes$-prefix computation

> __*c*__. Argue that P-SCAN-2 is correct, and analyze its work, span, and parallelism.

* Work: $T\_1(n) = 2 T\_1(n / 2) + \Theta(n) = \Theta(n \lg n)$.
* Span: $T\_\infty(n) = T\_\infty(n / 2) + \Theta(\lg n) = \Theta(\lg^2n)$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n / \lg n)$.

> __*d*__. Fill in the three missing expressions in line 8 of P-SCAN-UP and lines 5 and 6 of P-SCAN-DOWN. Argue that with expressions you supplied, P-SCAN-3 is correct.

* 8: t[k] * right
* 5: v
* 6: t[k]

> __*e*__. Analyze the work, span, and parallelism of P-SCAN-3.

* Work: $T\_1 = \Theta(n)$.
* Span: $T\_\infty = \Theta(\lg n)$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n / \lg n)$.

### 27-5 Multithreading a simple stencil calculation

> Computational science is replete with algorithms that require the entries of an array to be filled in with values that depend on the values of certain already computed neighboring entries, along with other information that does not change over the course of the computation. The pattern of neighboring entries does not change during the computation and is called a __*stencil*__.

> __*a*__. a. Give multithreaded pseudocode that performs this simple stencil calculation using a divide-and-conquer algorithm SIMPLE-STENCIL based on the decomposition (27.11) and the discussion above. (Don't worry about the details of the base case, which depends on the specific stencil.) Give and solve recurrences for the work and span of this algorithm in terms of $n$. What is the parallelism?

```
SIMPLE-STENCIL(A)
1  SIMPLE-STENCIL(A11)
2  spawn SIMPLE-STENCIL(A12)
3  SIMPLE-STENCIL(A21)
3  sync
5  SIMPLE-STENCIL(A22)
```

* Work: $T\_1 = \Theta(n^2)$.
* Span: $T\_\infty(n) = 3 T\_\infty(n / 2) + \Theta(1) = \Theta(n^{\lg 3}) \approx \Theta(n^{1.58})$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n^{2/\lg 3}) \approx \Theta(n^{1.26})$.

> __*b*__. Modify your solution to part (a) to divide an $n \times n$ array into nine $n / 3 \times n / 3$ subarrays, again recursing with as much parallelism as possible. Analyze this algorithm. How much more or less parallelism does this algorithm have compared with the algorithm from part (a)?

```
11
spawn 12 21 sync
spawn 13 22 31 sync
spawn 23 32 sync
33
```

* Work: $T\_1 = \Theta(n^2)$.
* Span: $T\_\infty(n) = 5 T\_\infty(n / 3) + \Theta(1) = \Theta(n^{\log\_3 5}) \approx \Theta(n^{1.46})$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n^{2/\log\_3 5}) \approx \Theta(n^{1.37})$.

> __*c*__. Generalize your solutions to parts (a) and (b) as follows. Choose an integer $b \ge 2$. Divide an $n \times n$ array into $b^2$ subarrays, each of size $n / b \times n / b$, recursing with as much parallelism as possible. In terms of $n$ and $b$, what are the work, span, and parallelism of your algorithm? Argue that, using this approach, the parallelism must be $o(n)$ for any choice of $b \ge 2$. (Hint: For this last argument, show that the exponent of $n$ in the parallelism is strictly less than 1 for any choice of $b \ge 2$.)

* Work: $T\_1 = \Theta(n^2)$.
* Span: $T\_\infty(n) = (2b - 1) T\_\infty(n / b) + \Theta(1) = \Theta(n^{\log\_b (2b - 1)})$.
* Parallelism: $T\_1 / T\_\infty = \Theta(n^{2/\log\_b (2b-1)}) = \Theta(n^{\log\_{2b - 1}b^2})$.

$b^2 \le 2b - 1$, $(b - 1)^2 \le 0$, since $b \ge 2$, the parallelism must be $o(n)$.

> __*d*__. Give pseudocode for a multithreaded algorithm for this simple stencil calculation that achieves $\Theta(n \lg n)$ parallelism. Argue using notions of work and span that the problem, in fact, has $\Theta(n)$ inherent parallelism. As it turns out, the divide-and-conquer nature of our multithreaded pseudocode does not let us achieve this maximal parallelism.

### 27-6 Randomized multithreaded algorithms

> Just as with ordinary serial algorithms, we sometimes want to implement randomized multithreaded algorithms. This problem explores how to adapt the various performance measures in order to handle the expected behavior of such algorithms. It also asks you to design and analyze a multithreaded algorithm for randomized quicksort.

> __*a*__. Explain how to modify the work law (27.2), span law (27.3), and greedy scheduler bound (27.4) to work with expectations when $T\_P$, $T\_1$, and $T\_\infty$ are all random variables.

$\text{E}[T\_P] \ge \text{E}[T\_1] / P$

$\text{E}[T\_P] \ge \text{E}[T\_\infty]$

$\text{E}[T\_P] \le \text{E}[T\_1]/P + \text{E}[T\_\infty]$

> __*b*__. Consider a randomized multithreaded algorithm for which 1% of the time we have $T\_1 = 10^4$ and $T\_{10,000} = 1$, but for 99% of the time we have $T\_1 = T\_{10,000} = 10^9$. Argue that the __*speedup*__ of a randomized multithreaded algorithm should be defined as $\text{E}[T\_1]/\text{E}[T\_P]$, rather than $\text{E}[T\_1 / T\_P]$.

$\text{E}[T\_1] \approx \text{E}[T\_{10,000}] \approx 9.9 \times 10^8$, $\text{E}[T\_1]/\text{E}[T\_P] = 1$.

$\text{E}[T\_1 / T\_{10,000}] = 10^4 \* 0.01 + 0.99 = 100.99$.

> __*c*__. Argue that the __*parallelism*__ of a randomized multithreaded algorithm should be defined as the ratio $\text{E}[T\_1] / \text{E}[T\_\infty]$.

Same as the above.

> __*d*__. Multithread the RANDOMIZED-QUICKSORT algorithm on page 179 by using nested parallelism. (Do not parallelize RANDOMIZED-PARTITION.) Give the pseudocode for your P-RANDOMIZED-QUICKSORT algorithm.

```
RANDOMIZED-QUICKSORT(A, p, r)
1  if p < r
2       q = RANDOM-PARTITION(A, p, r)
3  spawn RANDOMIZED-QUICKSORT(A, p, q - 1)
4  RANDOMIZED-QUICKSORT(A, q + 1, r)
5  sync
```

> __*e*__. Analyze your multithreaded algorithm for randomized quicksort. (Hint: Review the analysis of RANDOMIZED-SELECT on page 216.)

$\text{E}[T\_1] = O(n \lg n)$

$\text{E}[T\_\infty] = O(\lg n)$

$\text{E}[T\_1] / \text{E}[T\_\infty] = O(n)$
