## 5.1 The hiring problem

### 5.1-1

> Show that the assumption that we are always able to determine which candidate is best, in line 4 of procedure HIRE-ASSISTANT, implies that we know a total order on the ranks of the candidates.

Transitive


### 5.2-2 $\star$

> Describe an implementation of the procedure RANDOM$(a, b)$ that only makes calls to RANDOM$(0, 1)$. What is the expected running time of your procedure, as a function of $a$ and $b$?

Divide $[a, b]$ into $[a, mid]$ and $(mid, b]$, if RANDOM$(0, 1)$ gives 0 then we choose $[a, mid]$ and repeat the step until there is only one element left. The expected running time is $\Theta(\lg(b-a))$.

```python
import random


def random_interval(a, b):
    while a < b:
        if random.randint(0, 1) == 0:
            b = (a + b) // 2
        else:
            a = (a + b) // 2 + 1
    return a
```

### 5.2-3 $\star$

> Suppose that you want to output $0$ with probability $1/2$ and $1$ with probability $1/2$. At your disposal is a procedure BIASED-RANDOM, that outputs either $0$ or $1$. It outputs $1$ with some probability $p$ and $0$ with probability $1 - p$, where $0 < p < 1$, but you do not know what $p$ is. Give an algorithm that uses BIASED-RANDOM as a subroutine, and returns an unbiased answer, returning $0$ with probability $1/2$ and $1$ with probability $1/2$. What is the expected running time of your algorithm as a function of $p$?

The probabilities of generating (0, 1) and (1, 0) with BIASED-RANDOM is the same. We can generate two numbers with BIASED-RANDOM, and if they are different, we can return the first number, otherwise we should regenerate the two numbers. Since the probability of generating two different number is $2p(1-p)$, thus the expectation of generation times is $\frac{1}{2p(1-p)}$.


```python
import random


def biased_random():
    if random.random() < 0.1:
        return 0
    return 1


def unbiased_random():
    while True:
        a = biased_random()
        b = biased_random()
        if a != b:
            return a
```
