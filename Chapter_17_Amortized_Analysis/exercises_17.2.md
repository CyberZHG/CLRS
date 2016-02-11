## 17.2 The accounting method

### 17.2-1

> Suppose we perform a sequence of stack operations on a stack whose size never exceeds $$k$$. After every $$k$$ operations, we make a copy of the entire stack for backup purposes. Show that the cost of $$n$$ stack operations, including copying the stack, is $$O(n)$$ by assigning suitable amortized costs to the various stack operations.

PUSH: $$2$$, POP: $$2$$, COPY: $$0$$.

### 17.2-2

> Redo Exercise 17.1-3 using an accounting method of analysis.

### 17.2-3

> Suppose we wish not only to increment a counter but also to reset it to zero (i.e., make all bits in it 0). Counting the time to examine or modify a bit as $$\Theta(1)$$, show how to implement a counter as an array of bits so that any sequence of $$n$$ INCREMENT and RESET operations takes time $$O(n)$$ on an initially zero counter.

Twice cost of each bit.
