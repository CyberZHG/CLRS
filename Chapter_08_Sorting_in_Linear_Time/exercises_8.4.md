## 8.4 Bucket sort

### 8.4-1

> Using Figure 8.4 as a model, illustrate the operation of BUCKET-SORT on the array $A = \left \langle.79, .13, .16, .64, .39, .20, .89, .53, .71, .42\right \rangle$.

| R | |
|:-:|:--|
| 0 ||
| 1 |.13 .16|
| 2 |.20|
| 3 |.39|
| 4 |.42|
| 5 |.53|
| 6 |.64|
| 7 ||
| 8 |.79 .71|
| 9 |.89|

$A = \left \langle.13, .16, .20, .39, .42, .53, .64, .71, .79, .89\right \rangle$

### 8.4-2

> Explain why the worst-case running time for bucket sort is $\Theta(n^2)$. What simple change to the algorithm preserves its linear average-case running time and makes its worst-case running time $O(n \lg n)$?

Worst: all the elements falls in one bucket, $\Theta(n ^ 2)$ sorting.

Change: use merge sort in each bucket.

### 8.4-3

> Let $X$ be a random variable that is equal to the number of heads in two flips of a fair coin. What is $\text{E}[X^2]$? What is $\text{E}^2[X]$?

$$
\text{E}[X] = 2 \cdot \frac{1}{4} + 1 \cdot \frac{1}{2} + 0 \cdot \frac{1}{4} = 1
$$

$$
\text{E}[X^2] = 4 \cdot \frac{1}{4} + 1 \cdot \frac{1}{2} + 0 \cdot \frac{1}{4} = 1.5
$$

$$
\text{E}^2[X] = \text{E}[X] \cdot \text{E}[X] = 1 \cdot 1 = 1
$$

### 8.4-4 $\star$

> We are given $n$ points in the unit circle, $p\_i = (xi, yi)$, such that $0 < x\_i^2 + y\_i^2 \le 1$ for $i = 1,2, \dots ,n$. Suppose that the points are uniformly distributed; that is, the probability of finding a point in any region of the circle is proportional to the area of that region. Design an algorithm with an average-case running time of $\Theta(n)$ to sort the $n$ points by their distances $d\_i = \sqrt{x\_i^2+y\_i^2}$ from the origin. 

Bucket sort by radius, 

$$
\pi r\_i^2 = \frac{i}{10} \cdot \pi 1^2
$$

$$
r\_i = \sqrt{\frac{i}{10}}
$$

### 8.4-5 $\star$

> A __*probability distribution function*__ $P(x)$ for a random variable $X$ is defined by $P(x) = \text{Pr}\{X \le x\}$. Suppose that we draw a list of $n$ random variables $X\_1,X\_2, \dots ,X\_n$ from a continuous probability distribution function $P$ that is computable in $O(1)$ time. Give an algorithm that sorts these numbers in linear average-case time.

Bucket sort by $p\_i$,

$$
P(p\_i) = \frac{i}{10}
$$
