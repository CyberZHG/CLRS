## Problems

### 31-1 Binary gcd algorithm

> Most computers can perform the operations of subtraction, testing the parity (odd or even) of a binary integer, and halving more quickly than computing remainders. This problem investigates the __*binary gcd algorithm*__, which avoids the remainder computations used in Euclid's algorithm.

> __*a*__. Prove that if $$a$$ and $$b$$ are both even, then $$\text{gcd}(a, b) = 2 \cdot \text{gcd}(a/2, b/2)$$.

> __*b*__. Prove that if $$a$$ is odd and $$b$$ is even, then $$\text{gcd}(a, b) = \text{gcd}(a, b/2)$$.

> __*c*__. Prove that if $$a$$ and $$b$$ are both odd, then $$\text{gcd}(a, b) = \text{gcd}((a - b) / 2, b)$$.

> __*d*__. Design an efficient binary gcd algorithm for input integers $$a$$ and $$b$$, where $$a \ge b$$, that runs in $$O(\lg a)$$ time. Assume that each subtraction, parity test, and halving takes unit time.

```python
def binary_gcd(a, b):
    if a < b:
        return binary_gcd(b, a)
    if b == 0:
        return a
    if (a & 1 == 1) and (b & 1 == 1):
        return binary_gcd((a - b) >> 1, b)
    if (a & 1 == 0) and (b & 1 == 0):
        return binary_gcd(a >> 1, b >> 1) << 1
    if a & 1 == 1:
        return binary_gcd(a, b >> 1)
    return binary_gcd(a >> 1, b)
```

### 31-2 Analysis of bit operations in Euclid's algorithm

> __*a*__. Consider the ordinary "paper and pencil" algorithm for long division: dividing $$a$$ by $$b$$, which yields a quotient $$q$$ and remainder $$r$$. Show that this method requires $$O((1 + \lg q) \lg b)$$ bit operations.



> __*b*__. Define $$\mu(a, b) = (1 + \lg a)(1 + \lg b)$$. Show that the number of bit operations performed by EUCLID in reducing the problem of computing $$\text{gcd}(a, b)$$ to that of computing $$\text{gcd}(b, a~\text{mod}~b)$$ is at most $$c(\mu(a, b) - \mu(b, a~\text{mod}~b))$$ for some sufficiently large constant $$c > 0$$.

> __*c*__. Show that EUCLID$$(a, b)$$ requires $$O(\mu(a, b))$$ bit operations in general and $$O(\beta^2)$$ bit operations when applied to two $$\beta$$-bit inputs.

### 31-3 Three algorithms for Fibonacci numbers

> This problem compares the efficiency of three methods for computing the $$n$$th Fibonacci number $$F_n$$, given $$n$$. Assume that the cost of adding, subtracting, or multiplying two numbers is $$O(1)$$, independent of the size of the numbers.

> __*a*__. Show that the running time of the straightforward recursive method for computing $$F_n$$ based on recurrence (3.22) is exponential in $$n$$. (See, for example, the FIB procedure on page 775.)


> __*b*__. Show how to compute $$F_n$$ in $$O(n)$$ time using memoization.


> __*c*__. Show how to compute $$F_n$$ in $$O(\lg n)$$ time using only integer addition and multiplication.
(Hint: Consider the matrix

> $$\displaystyle \left (
\begin{matrix}
0 & 1 \\
1 & 1
\end{matrix}
\right )
$$

> and its powers.)


> __*d*__. Assume now that adding two $$\beta$$-bit numbers takes $$\Theta(\beta)$$ time and that multiplying two $$\beta$$-bit numbers takes $$\Theta(\beta^2)$$ time. What is the running time of these three methods under this more reasonable cost measure for the elementary arithmetic operations?

### 31-4 Quadratic residues

> Let $$p$$ be an odd prime. A number $$a \in Z_p^*$$ is a __*quadratic residue*__ if the equation $$x^2 = a ~(\text{mod}~p)$$ has a solution for the unknown $$x$$.

> __*a*__. Show that there are exactly $$(p - 1) / 2$$ quadratic residues, modulo $$p$$.


> __*b*__. If $$p$$ is prime, we define the __*Legendre symbol*__ $$(\frac{a}{p})$$, for $$a \in \mathbb{Z}_p^*$$, to be $$1$$ if $$a$$ is a quadratic residue modulo $$p$$ and $$-1$$ otherwise. Prove that if $$a \in \mathbb{Z}_p^*$$, then

> $$\displaystyle \left ( \frac{a}{p} \right ) \equiv a^{(p - 1) / 2} ~(\text{mod}~ p)$$.

> Give an efficient algorithm that determines whether a given number $$a$$ is a quadratic residue modulo $$p$$. Analyze the efficiency of your algorithm.

> __*c*__. Prove that if $$p$$ is a prime of the form $$4k + 3$$ and $$a$$ is a quadratic residue in $$\mathbb{Z}_b^*$$, then $$a^{k+1} ~\text{mod}~ p$$ is a square root of $$a$$, modulo $$p$$. How much time is required to find the square root of a quadratic residue $$a$$ modulo $$p$$?

> __*d*__. Describe an efficient randomized algorithm for finding a nonquadratic residue, modulo an arbitrary prime $$p$$, that is, a member of $$\mathbb{Z}_p^*$$ that is not a quadratic residue. How many arithmetic operations does your algorithm require on average?

