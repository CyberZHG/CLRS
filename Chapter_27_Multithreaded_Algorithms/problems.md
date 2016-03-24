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

