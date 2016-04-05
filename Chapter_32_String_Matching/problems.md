## Problems

### 32-1 String matching based on repetition factors

> Let $$y^i$$ denote the concatenation of string $$y$$ with itself $$i$$ times. For example, $$(\text{ab})^3=\text{ababab}$$. We say that a string $$x \in \Sigma^*$$ has __*repetition factor*__ $$r$$ if $$x = y ^ r$$ for some string $$y \in \Sigma^*$$ and some $$r > 0$$. Let $$\rho$$ denote the largest $$r$$ such that $$x$$ has repetition factor $$r$$.

> __*a*__. Give an efficient algorithm that takes as input a pattern $$P[1 \dots m]$$ and computes the value $$\rho(P_i)$$ for $$i = 1, 2, \dots, m$$. What is the running time of your algorithm?

> __*b*__. For any pattern $$P[1 \dots m]$$, let $$\rho^*(P)$$ be defined as $$\max_{1 \le i \le m} \rho(P_i)$$. Prove that if the pattern $$P$$ is chosen randomly from the set of all binary strings of length $$m$$, then the expected value of $$\rho^*(P)$$ is $$O(1)$$.

> __*c*__. Argue that the following string-matching algorithm correctly finds all occurrences of pattern $$P$$ in a text $$T[1 \dots n]$$ in time $$O(\rho^*(P)n + m)$$:

> ```
REPETITION-MATCHER(P, T)
 1  m = P.length
 2  n = T.length
 3  k = 1 + \rho^*(P)
 4  q = 0
 5  s = 0
 6  while s <= n - m
 7      if T[s + q + 1] == P[q + 1]
 8          q = q + 1
 9          if q == m
10               print "Pattern occurs with shift" s
11      if q == m or T[s + q + 1] != P[q + 1]
12          s = s + max(1, ceil(q/k))
13          q = 0
```

> This algorithm is due to Galil and Seiferas. By extending these ideas greatly, they obtained a linear-time string-matching algorithm that uses only $$O(1)$$ storage beyond what is required for $$P$$ and $$T$$.
