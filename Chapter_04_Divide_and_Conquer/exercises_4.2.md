## 4.2 Strassen's algorithm for matrix multiplication

### 4.2-1

> Use Strassen’s algorithm to compute the matrix product
>
> $\begin{pmatrix} 1 & 3 \\\\ 7 & 5 \end{pmatrix}\begin{pmatrix} 6 & 8 \\\\ 4 & 2 \end{pmatrix}$.
>
> Show your work.

$S\_1 = B\_{12} - B\_{22} = 8 - 2 = 6$

$S\_2 = A\_{11} + A\_{12} = 1 + 3 = 4$

$S\_3 = A\_{21} + A\_{22} = 7 + 5 = 12$

$S\_4 = B\_{21} - B\_{11} = 4 - 6 = -2$

$S\_5 = A\_{11} + A\_{22} = 1 + 5 = 6$

$S\_6 = B\_{11} + B\_{22} = 6 + 2 = 8$

$S\_7 = A\_{12} - A\_{22} = 3 - 5 = -2$

$S\_8 = B\_{21} + B\_{22} = 4 + 2 = 6$

$S\_9 = A\_{11} - A\_{21} = 1 - 7 = -6$

$S\_{10} = B\_{11} + B\_{12} = 6 + 8 = 14$

$P\_1 = A\_{11} \cdot S\_1 = 1 \times 6 = 6$

$P\_2 = S\_{2} \cdot B\_{22} = 4 \times 2 = 8$

$P\_3 = S\_{3} \cdot B\_{11} = 12 \times 6 = 72$

$P\_4 = A\_{22} \cdot S\_4 = 5 \times -2 = -10$

$P\_5 = S\_{5} \cdot S\_6 = 6 \times 8 = 48$

$P\_6 = S\_{7} \cdot S\_8 = -2 \times 6 = -12$

$P\_7 = S\_{9} \cdot S\_{10} = -6 \times 14 = -84$

$C\_{11} = P\_5 + P\_4 - P\_2 + P\_6 = 48 - 10 - 8 - 12 = 18$

$C\_{12} = P\_1 + P\_2 = 8 + 6 = 14$

$C\_{21} = P\_3 + P\_4 = 72 - 10 = 62$

$C\_{22} = P\_5 + P\_1 - P\_3 - P\_7 = 48 + 6 - 72 + 84 = 66$

$$\begin{pmatrix} 18 & 14 \\\\ 62 & 66 \end{pmatrix}$$

### 4.2-2

> Write pseudocode for Strassen’s algorithm.

```python
def matrix_product_strassen_sub(a, b, r_low, r_high, c_low, c_high):
    n = r_high - r_low
    if n == 1:
        return [[a[r_low][c_low] * b[r_low][c_low]]]
    mid = n // 2
    r_mid = (r_low + r_high) // 2
    c_mid = (c_low + c_high) // 2
    s = [[[0 for _ in range(mid)] for _ in range(mid)] for _ in range(10)]
    for i in range(mid):
        for j in range(mid):
            s[0][i][j] = b[r_low + i][c_mid + j] - b[r_mid + i][c_mid + j]
            s[1][i][j] = a[r_low + i][c_low + j] + a[r_low + i][c_mid + j]
            s[2][i][j] = a[r_mid + i][c_low + j] + a[r_mid + i][c_mid + j]
            s[3][i][j] = b[r_mid + i][c_low + j] - b[r_low + i][c_low + j]
            s[4][i][j] = a[r_low + i][c_low + j] + a[r_mid + i][c_mid + j]
            s[5][i][j] = b[r_low + i][c_low + j] + b[r_mid + i][c_mid + j]
            s[6][i][j] = a[r_low + i][c_mid + j] - a[r_mid + i][c_mid + j]
            s[7][i][j] = b[r_mid + i][c_low + j] + b[r_mid + i][c_mid + j]
            s[8][i][j] = a[r_low + i][c_low + j] - a[r_mid + i][c_low + j]
            s[9][i][j] = b[r_low + i][c_low + j] + b[r_low + i][c_mid + j]
    p = [[[0 for _ in range(mid)] for _ in range(mid)] for _ in range(7)]
    for i in range(mid):
        for j in range(mid):
            for k in range(mid):
                p[0][i][j] += a[r_low + i][c_low + k] * s[0][k][j]
                p[1][i][j] += s[1][i][k] * b[r_mid + k][c_mid + j]
                p[2][i][j] += s[2][i][k] * b[r_low + k][c_low + j]
                p[3][i][j] += a[r_mid + i][c_mid + k] * s[3][k][j]
                p[4][i][j] += s[4][i][k] * s[5][k][j]
                p[5][i][j] += s[6][i][k] * s[7][k][j]
                p[6][i][j] += s[8][i][k] * s[9][k][j]
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            c[r_low + i][c_low + j] = p[4][i][j] + p[3][i][j] - p[1][i][j] + p[5][i][j]
            c[r_low + i][c_mid + j] = p[0][i][j] + p[1][i][j]
            c[r_mid + i][c_low + j] = p[2][i][j] + p[3][i][j]
            c[r_mid + i][c_mid + j] = p[4][i][j] + p[0][i][j] - p[2][i][j] - p[6][i][j]
    return c


def matrix_product_strassen(a, b):
    n = len(a)
    return matrix_product_strassen_sub(a, b, 0, n, 0, n)
```

### 4.2-3

> How would you modify Strassen’s algorithm to multiply $n \times n$ matrices in which $n$ is not an exact power of $2$? Show that the resulting algorithm runs in time $\Theta(n^{\lg 7})$.

Extend the matrix with zeros.

### 4.2-4

> What is the largest $k$ such that if you can multiply $3 \times 3$ matrices using k multiplications (not assuming commutativity of multiplication), then you can multiply $n \times n$ matrices in time $\Theta(n^{\lg 7})$? What would the running time of this algorithm be?

$T(n) = kT(n/3) + O(n^2)$

Running time: $\Theta(n^{\log\_3 7})$

$k \le 3^{\lg 7} \approx 21.84986222490514$

### 4.2-5

> V. Pan has discovered a way of multiplying $68 \times 68$ matrices using $132,464$ multiplications, a way of multiplying $70 \times 70$ matrices using $143,640$ multiplications, and a way of multiplying $72 \times 72$ matrices using $155,424$ multiplications. Which method yields the best asymptotic  matrix-multiplication algorithm? How does it compare to Strassen’s algorithm?

$T\_1 = \Theta(n^{\log\_{68}132464}) = \Theta(n^{2.7951284873613815})$

$T\_2 = \Theta(n^{\log\_{70}143640}) = \Theta(n^{2.795122689748337})$

$T\_3 = \Theta(n^{\log\_{72}155424}) = \Theta(n^{2.795147391093449})$

$T\_2 < T\_1 < T\_3 < \Theta(n^{\lg 7})$


### 4.2-6

> How quickly can you multiply a $kn \times n$ matrix by an $n \times kn$ matrix, using Strassen’s algorithm as a subroutine? Answer the same question with the order of the input matrices reversed.

$\Theta(k^2n^{\lg 7})$

Reversed: $\Theta(kn^{\lg 7})$


### 4.2-7

> Show how to multiply the complex numbers $a + bi$ and $c + di$ using only three multiplications of real numbers. The algorithm should take $a$, $b$, $c$, and $d$ as input and produce the real component $ac - bd$ and the imaginary component $ad + bc$ separately.

$P\_1 = a \cdot (c - d)$

$P\_2 = b \cdot (c + d)$

$P\_3 = d \cdot (a - b)$

Real component: $P\_1 + P\_3$

Image component: $P\_2 + P\_3$
