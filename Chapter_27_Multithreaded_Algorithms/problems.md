## Problems

### 27-1 Implementing parallel loops using nested parallelism

> Consider the following multithreaded algorithm for performing pairwise addition on n-element arrays $$A[1 \dots n]$$ and $$B[1 \dots n]$$, storing the sums in $$C[1 \dots n]$$:

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

> __*b*__. Suppose that we set $$grain\text{-}size = 1$$. What is the parallelism of this implementation?

$$T_1 = \Theta(n)$$, $$T_\infty = \Theta(n)$$, $$T_1 / T_\infty = \Theta(1)$$.

> __*c*__. Give a formula for the span of SUM-ARRAYS' in terms of $$n$$ and $$grain\text{-}size$$. Derive the best value for grain-size to maximize parallelism.

$$T_\infty(n) = \Theta(\max(grain\text{-}size, n / grain\text{-}size))$$

### 27-2 Saving temporary space in matrix multiplication

> The P-MATRIX-MULTIPLY-RECURSIVE procedure has the disadvantage that it must allocate a temporary matrix $$T$$ of size $$n \times n$$, which can adversely affect the constants hidden by the $$\Theta$$-notation. The P-MATRIX-MULTIPLY-RECURSIVE procedure does have high parallelism, however. For example, ignoring the constants in the $$\Theta$$-notation, the parallelism for multiplying $$1000 \times 1000$$ matrices comes to approximately $$1000^3 / 10^2 = 10^7$$, since $$\lg 1000 \approx 10$$. Most parallel computers have far fewer than 10 million processors.

> __*a*__. Describe a recursive multithreaded algorithm that eliminates the need for the temporary matrix $$T$$ at the cost of increasing the span to $$\Theta(n)$$.

Initialize $$C = 0$$ in parallel in $$\Theta(\lg n)$$, add __sync__ after the 4th __spawn__, $$c_{11} = c_{11} + a_{11} \cdot b_{11}$$, $$T_\infty(n) = 2 T_\infty(n / 2) + \Theta(\lg n) = \Theta(n)$$

> __*b*__. Give and solve recurrences for the work and span of your implementation.

* Work: $$T_1 = \Theta(n^3)$$.
* Span: $$T_\infty = \Theta(n)$$.

> __*c*__. Analyze the parallelism of your implementation. Ignoring the constants in the $$\Theta$$-notation, estimate the parallelism on $$1000 \times 1000$$ matrices. Compare with the parallelism of P-MATRIX-MULTIPLY-RECURSIVE.

Parallelism: $$T_1 / T_\infty = \Theta(n^2) = 1000^2 = 10^6$$.

Most parallel computers still have far fewer than 1 million processors.

### 27-3 Multithreaded matrix algorithms

> __*a*__. Parallelize the LU-DECOMPOSITION procedure on page 821 by giving pseudocode for a multithreaded version of this algorithm. Make your implementation as parallel as possible, and analyze its work, span, and parallelism.

> __*b*__. Do the same for LUP-DECOMPOSITION on page 824.

> __*c*__. Do the same for LUP-SOLVE on page 817.

> __*d*__. Do the same for a multithreaded algorithm based on equation (28.13) for inverting a symmetric positive-definite matrix.

### 27-4 Multithreading reductions and prefix computations

> A __*$$\otimes$$-reduction*__ of an array $$x[1 \dots n]$$, where $$\otimes$$ is an associative operator, is the value 

> $$y = x[1] \otimes x[2] \otimes \cdots \otimes x[n]$$

> The following procedure computes the $$\otimes$$-reduction of a subarray $$x[i \dots j]$$ serially.

> ```
REDUCE(x, i, j)
1  y = x[i]
2  for k = i + 1 to j
3       y = y \otimes x[k]
4  return y
```

> __*a*__. Use nested parallelism to implement a multithreaded algorithm P-REDUCE, which performs the same function with $$\Theta(n)$$ work and $$\Theta(\lg n)$$ span. Analyze your algorithm.

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

> A related problem is that of computing a __*$$\otimes$$-prefix*__ computation, sometimes called a __*$$\otimes$$-scan*__, on an array $$x[1 \dots n]$$, where $$\otimes$$ is once again an associative operator. The $$\otimes$$-scan produces the array $$y[1 \dots n]$$.

> Unfortunately, multithreading SCAN is not straightforward. For example, changing the __for__ loop to a __parallel for__ loop would create races, since each iteration of the loop body depends on the previous iteration. The following procedure P-SCAN-1 performs the $$\otimes$$-prefix computation in parallel, albeit inefficiently.

> __*b*__. Analyze the work, span, and parallelism of P-SCAN-1.

* Work: $$T_1 = \Theta(n^2)$$.
* Span: $$T_\infty = \Theta(\lg n) + \Theta(\lg n) = \Theta(\lg n)$$.
* Parallelism: $$T_1 / T_\infty = \Theta(n^2 / \lg n)$$.

> By using nested parallelism, we can obtain a more efficient $$\otimes$$-prefix computation

> __*c*__. Argue that P-SCAN-2 is correct, and analyze its work, span, and parallelism.

* Work: $$T_1(n) = 2 T_1(n / 2) + \Theta(n) = \Theta(n \lg n)$$.
* Span: $$T_\infty(n) = T_\infty(n / 2) + \Theta(\lg n) = \Theta(\lg^2n)$$.
* Parallelism: $$T_1 / T_\infty = \Theta(n / \lg n)$$.

> __*d*__. Fill in the three missing expressions in line 8 of P-SCAN-UP and lines 5 and 6 of P-SCAN-DOWN. Argue that with expressions you supplied, P-SCAN-3 is correct.

* 8: t[k] * right
* 5: v
* 6: t[k]

> __*e*__. Analyze the work, span, and parallelism of P-SCAN-3.

* Work: $$T_1 = \Theta(n)$$.
* Span: $$T_\infty = \Theta(\lg n)$$.
* Parallelism: $$T_1 / T_\infty = \Theta(n / \lg n)$$.

