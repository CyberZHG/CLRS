## Indicator random variables

### 5.2-1

> In HIRE-ASSISTANT, assuming that the candidates are presented in a random order, what is the probability that you hire exactly one time? What is the probability that you hire exactly $$n$$ times?

* Extractly one time

The best candidate comes first, which is $$\frac{1}{n}$$.

* Extractly $$n$$ times

The candidates presented in ascending order, which is $$\frac{1}{n!}$$.

### 5.2-2

> In HIRE-ASSISTANT, assuming that the candidates are presented in a random order, what is the probability that you hire exactly twice?

Suppose the first candidate is of rank $$k$$, followed by some candidates with rank less than $$k$$, then followed the candidate with rank $$n$$.

$$
P=\sum_{k=1}^{n-1}\frac{1}{n}\frac{1}{n-k}=\frac{1}{n}\sum_{i=1}^{n-1}\frac{1}{i}=O \left ( \frac{\lg n}{n} \right )
$$

### 5.2-3

> Use indicator random variables to compute the expected value of the sum of $$n$$ dice.

$$
E[X_i] = \frac{1+2+3+4+5+6}{6} = 3.5
$$

$$
\begin{array}{rll}
E[X] &=& \displaystyle E \left [ \sum_{i=1}^n X_i \right ] \\
&=& \displaystyle \sum_{i=1}^n E[X_i] \\
&=& \displaystyle \sum_{i=1}^n 3.5 \\
&=& \displaystyle 3.5n
\end{array}
$$

### 5.2-4

> Use indicator random variables to solve the following problem, which is known as the __*hat-check problem*__. Each of $$n$$ customers gives a hat to a hat-check person at a restaurant. The hat-check person gives the hats back to the customers in a random order. What is the expected number of customers who get back their own hat?

The probability of one customer get his/her hat back is $$1/n$$, therefore the expectation is $$n \dot (1/n) = 1$$.

### 5.2-5

> Let $$A[1 \dots n]$$ be an array of $$n$$ distinct numbers. If $$i < j$$ and $$A[i] > A[j]$$, then the pair $$(i,j)$$ is called an __*inversion*__ of $$A$$. (See Problem 2-4 for more on inversions.) Suppose that the elements of $$A$$ form a uniform random permutation of $$\left \langle 1, 2, \dots, n \right \rangle$$. Use indicator random variables to compute the expected number of
inversions.

Suppose $$X_{ij} = I\{(i, j) \text{ is an inversion}\}$$,

$$
E[X_{ij}] = \frac{1}{2}
$$

$$
E[X] = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} E[X_{ij}]
= \frac{n(n-1)}{4}
$$

