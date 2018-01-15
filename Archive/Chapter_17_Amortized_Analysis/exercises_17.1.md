## 17.1 Aggregate analysis

### 17.1-1

> If the set of stack operations included a MULTIPUSH operation, which pushses $$k$$ items onto the stack, would the $$O(1)$$ bound on the amortized cost of stack operations continue to hold?

No.

### 17.1-2

> Show that if a DECREMENT operatoin were included in the $$k$$-bit counter example, $$n$$ operations could cost as much as $$\Theta(nk)$$ time.

Increment and decrement repeatly on $$011\cdots11$$.

### 17.1-3

> Suppose we perform a sequence of $$n$$ operations on a data structure in which the $$i$$th operation costs $$i$$ if $$i$$ is an exact power of $$2$$, and $$1$$ otherwise. Use aggregate analysis to determine the amortized cost per operation.

$$1 + 2 + 2^2 + \cdots + 2^{\lfloor \lg n \rfloor} \le 2n$$
