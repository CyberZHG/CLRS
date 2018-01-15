## 32.1 The naive string-matching algorithm

### 32.1-1

> Show the comparisons the naive string matcher makes for the pattern $$P = 0001$$ in the text $$T = 000010001010001$$.

$$\dots$$

### 32.1-2

> Suppose that all characters in the pattern $$P$$ are different. Show how to accelerate NAIVE-STRING-MATCHER to run in time $$O(n)$$ on an $$n$$-character text $$T$$.

Suppose $$T[i] \ne P[j]$$, then for $$k \in [1, j)$$, $$T[i - k] = P[j - k] \ne P[0]$$, the $$[i - k, i)$$ are all invalid shifts which could be skipped, therefore we can compare $$T[i]$$ with $$P[0]$$ in the next iteration.

### 32.1-3

> Suppose that pattern $$P$$ and text $$T$$ are randomly chosen strings of length $$m$$ and $$n$$, respectively, from the $$d$$-ary alphabet $$\Sigma_d = \{0, 1, \dots, d - 1 \}$$, where $$d \ge 2$$. Show that the expected number of character-to-character comparisons made by the implicit loop in line 4 of the naive algorithm is

> $$\displaystyle (n - m + 1) \frac{1 - d^{-m}}{1 - d^{-1}} \le 2 (n - m + 1)$$

> over all executions of this loop. (Assume that the naive algorithm stops comparing characters for a given shift once it finds a mismatch or matches the entire pattern.) Thus, for randomly chosen strings, the naive algorithm is quite efficient.

Suppose for each shift, the number of compared characters is $$L$$, then:

$$
\begin{array}{rll}
\text{E}[L] &=& 
\displaystyle 1 \cdot \frac{d - 1}{d} + 2 \cdot \left ( \frac{1}{d} \right )^1 \frac{d - 1}{d} + \cdots + m \cdot \left ( \frac{1}{d} \right )^{m - 1} \frac{d - 1}{d} + m \cdot \left ( \frac{1}{d} \right )^{m} \\
&=& 
\displaystyle \left (1 + 2 \cdot \left ( \frac{1}{d} \right )^1  + \cdots + m \cdot \left ( \frac{1}{d} \right )^{m} \right ) \frac{d - 1}{d} + m \cdot \left ( \frac{1}{d} \right )^{m}
\end{array}
$$

$$
\begin{array}{rllcl}
S &=& 1 + &\displaystyle 2 \cdot \left ( \frac{1}{d} \right )^1  + \cdots + m \cdot \left ( \frac{1}{d} \right )^{m - 1} \\
\displaystyle \frac{1}{d}S &=& &
\displaystyle 1 \cdot \left ( \frac{1}{d} \right )^1  + \cdots + (m - 1) \cdot \left ( \frac{1}{d} \right )^{m - 1} &\displaystyle  + m \cdot \left ( \frac{1}{d} \right )^{m} \\
\displaystyle \frac{d - 1}{d}S &=& &\displaystyle 1 +  \left ( \frac{1}{d} \right )^1  + \cdots + \cdot \left ( \frac{1}{d} \right )^{m - 1}&\displaystyle  - m \cdot \left ( \frac{1}{d} \right )^{m} \\
\displaystyle \frac{d - 1}{d}S &=& &
\displaystyle \frac{1 - d^{-m}}{1 - d^{-1}}
&\displaystyle  - m \cdot \left ( \frac{1}{d} \right )^{m} \\
\end{array}
$$

$$
\begin{array}{rll}
\text{E}[L] &=& 
\displaystyle \left (1 + 2 \cdot \left ( \frac{1}{d} \right )^1  + \cdots + m \cdot \left ( \frac{1}{d} \right )^{m} \right ) \frac{d - 1}{d} + m \cdot \left ( \frac{1}{d} \right )^{m} \\
&=&\displaystyle 
 \frac{1 - d^{-m}}{1 - d^{-1}}
 - m \cdot \left ( \frac{1}{d} \right )^{m}  + m \cdot \left ( \frac{1}{d} \right )^{m} \\
 &=&\displaystyle 
 \frac{1 - d^{-m}}{1 - d^{-1}}
\end{array}
$$

There are $$n - m + 1$$ shifts, therefore the expected number of comparisons is:

$$\displaystyle (n - m + 1) \cdot \text{E}[L] = (n - m + 1) \frac{1 - d^{-m}}{1 - d^{-1}}$$

And since $$d \ge 2$$, $$1 - d^{-1} \ge 0.5$$, and since $$1 - d^{-m} < 1$$, $$\displaystyle \frac{1 - d^{-m}}{1 - d^{-1}} \le 2$$, therefore $$\displaystyle (n - m + 1) \frac{1 - d^{-m}}{1 - d^{-1}} \le 2 (n - m + 1)$$.

### 32.1-4

> Suppose we allow the pattern $$P$$ to contain occurrences of a __*gap character*__ $$\diamond$$ that can match an _arbitrary_ string of characters (even one of zero length). For example, the pattern $$ab\diamond ba\diamond c$$ occurs in the text $$cabccbacbacab$$ as

> $$\displaystyle c \underbrace{ab}_{ab} \underbrace{cc}_{\diamond} \underbrace{ba}_{ba} \underbrace{cba}_{\diamond} \underbrace{c}_{c} ab$$

> and as

> $$\displaystyle c \underbrace{ab}_{ab} \underbrace{ccbac}_{\diamond} \underbrace{ba}_{ba} \underbrace{ }_{\diamond} \underbrace{c}_{c} ab$$

> Note that the gap character may occur an arbitrary number of times in the pattern but not at all in the text. Give a polynomial-time algorithm to determine whether such a pattern $$P$$ occurs in a given text $$T$$, and analyze the running time of your algorithm.

Dynamic programming, $$\Theta(n^2 m)$$.
