## Problems

### 11-1 Longest-probe bound for hashing

> Suppose that we use an open-addressed hash table of size $$m$$ to store $$n \le m/2$$ items.

> __*a*__. Assuming uniform hashing, show that for $$i=1,2,\dots,n$$, the probability is at most $$2^{-k}$$ that the $$i$$th insertion requires strictly more than $$k$$ probes.

$$
\begin{array}{rll}
\displaystyle \text{Pr}\{X_i > k\} &=& 
\displaystyle \frac{n}{m} \cdot \frac{n - 1}{m - 1} \cdots \frac{n - k + 1}{m - k + 1} \\
&\le& \displaystyle \left ( \frac{n}{m} \right ) ^ {k} \\
&\le& \displaystyle \left ( \frac{1}{2} \right ) ^ {k} \\
&=& 2^{-k}
\end{array}
$$

> __*b*__. Show that for $$i=1,2,\dots,n$$, the probability is $$O(1/n^2)$$ that the $$i$$th insertion requires more than $$2\lg n$$ probes.

$$
\displaystyle \text{Pr}\{X_i > 2\lg n\} \le 2^{-2 \lg n} = 1/n^2 = O(1/n^2)
$$

> Let the random variable $$X_i$$ denote the number of probes required by the $$i$$th insertion. You have shown in part (b) that $$\text{Pr}\{X_i > 2\lg n\} = O(1/n^2)$$. Let the random variable $$X = \max_{1 \le i \le n} X_i$$ denote the maximum number of probes required by any of the $$n$$ insertions.

> __*c*__. Show that $$\text{Pr}\{ X > 2\lg n\}=O(1/n)$$.

$$
\text{Pr}\{ X > 2\lg n\}\le\sum_{i=1}^n 1/n^2 = 1/n =O(1/n)
$$

> __*d*__. Show that the expected length $$\text{E}[X]$$ of the longest probe sequence is $$O(\lg n)$$.

$$
\begin{array}{rll}
\text{E}[X] 
&=& \displaystyle \sum_{i=1}^n i \cdot \text{Pr}\{X = i\} \\
&=& \displaystyle \sum_{i=1}^{2 \lg n} i \cdot \text{Pr}\{X = i\} + \sum_{i=2 \lg n + 1}^n i \cdot \text{Pr}\{X = i\} \\ 
&\le& \displaystyle 2 \lg n \cdot \sum_{i=1}^{2 \lg n} \text{Pr}\{X = i\} + n \cdot \sum_{i=2 \lg n + 1}^n \text{Pr}\{X = i\} \\ 
&\le& \displaystyle 2 \lg n \cdot 1 + n \cdot 1/n \\ 
&=& \displaystyle 2 \lg n + 1 \\ 
&=& O(\lg n)
\end{array}
$$

### 11-2 Slot-size bound for chaining

> Suppose that we have a hash table with $$n$$ slots, with collisions resolved by chaining, and suppose that $$n$$ keys are inserted into the table. Each key is equally likely to be hashed to each slot. Let $$M$$ be the maximum number of keys in any slot after all the keys have been inserted. Your mission is to prove an $$O(\lg n/\lg\lg n)$$ upper bound on $$\text{E}[M]$$, the expected value of $$M$$.

> __*a*__. Argue that the probability $$Q_k$$ that exactly $$k$$ keys hash to a particular slot is given by

> $$\displaystyle Q_k = \left ( \frac{1}{n} \right ) ^ k \left ( 1 - \frac{1}{n} \right ) ^ {n - k} \binom{n}{k}$$.

Obviously.

> __*b*__. Let $$P_k$$ be the probability that $$M = k$$, that is, the probability that the slot containing the most keys contains $$k$$ keys. Show that $$P_k \le n Q_k$$.

$$nQ_k$$ is the probability that at least one slot contains $$k$$ keys, thus $$P_k \le nQ_k$$.

> __*c*__. Use Stirling's approximation, equation (3.18), to show that $$Q_k < e^k / k^k$$.

$$
\begin{array}{rll}
Q_k &=& \displaystyle Q_k = \left ( \frac{1}{n} \right ) ^ k \left ( 1 - \frac{1}{n} \right ) ^ {n - k} \binom{n}{k} \\
&=& \displaystyle \frac{(n-1)^{n-k}}{n^n} \cdot \frac{n \cdot (n-1) \cdots (n - k + 1)}{k!} \\
&\le& \displaystyle \frac{(n-1)^{n-k}}{n^n} \cdot \frac{n^k}{\sqrt{2 \pi k} \left ( \frac{k}{e} \right ) ^ k} \\
&=& \displaystyle \left ( \frac{n - 1}{n} \right ) ^ {n - k} \cdot \frac{(e/k)^k}{\sqrt{2 \pi k}} \\
&\le& e^k / k^k
\end{array}
$$

> __*d*__. Show that there exists a constant $$c>1$$ such that $$Q_{k_0} < 1/n^3$$ for $$k_0 = c \lg n / \lg \lg n$$. Conclude that $$P_k < 1/n^2$$ for $$k \ge k_0 = c\lg n/ \lg \lg n$$.

$$
\begin{array}{rll}
\lg Q_{k_0} 
&=& \displaystyle \frac{c \lg n (\lg e - \lg c)}{\lg \lg n} + c\lg n \cdot \left ( \frac{\lg\lg\lg n}{\lg \lg n} - 1 \right )
\end{array}
$$

The maximum of $$\displaystyle\frac{\lg\lg\lg n}{\lg \lg n}$$ is $$\displaystyle \frac{1}{e \log(2)} \approx 0.5307$$, and converge to $$0$$ when $$n \rightarrow \infty$$. For a large $$n$$, if $$c > 3$$, the first term is negative and

$$
\lg Q_{k_0} < -3\lg n = \lg \frac{1}{n^3}
$$

$$
\therefore Q_{k_0} < \frac{1}{n^3}
$$

$$
\therefore P_k \le n Q_k < \frac{1}{n^2}
$$

> __*e*__. Argue that

> $$\displaystyle \text{E}[M] \le \text{Pr} \left \{ M > \frac{c \lg n}{\lg \lg n} \right \} \cdot n + \text{Pr} \left \{ M \le \frac{c \lg n}{\lg \lg n} \right \} \cdot \frac{c \lg n}{\lg \lg n}$$.

> Conclude that $$E[M] = O(\lg n/ \lg \lg n)$$.

$$
\begin{array}{rll}
\text{E}[M]
&=& \displaystyle \sum_{i=1}^n \text{Pr}\{M=i\} \cdot i\\
&=& \displaystyle \sum_{i=1}^{\displaystyle \frac{c\lg n}{\lg \lg n}} \text{Pr}\{M=i\} \cdot i + \sum_{\displaystyle i=\frac{c\lg n}{\lg \lg n}+1}^{n} \text{Pr}\{M=i\} \cdot i \\
&\le& \displaystyle \sum_{i=1}^{\displaystyle \frac{c\lg n}{\lg \lg n}} \text{Pr}\{M=i\} \cdot \frac{c\lg n}{\lg \lg n} + \sum_{\displaystyle i=\frac{c\lg n}{\lg \lg n}+1}^{n} \text{Pr}\{M=i\} \cdot n \\
&=& \displaystyle \text{Pr} \left \{ M \le \frac{c \lg n}{\lg \lg n} \right \} \cdot \frac{c \lg n}{\lg \lg n} + \text{Pr} \left \{ M > \frac{c \lg n}{\lg \lg n} \right \} \cdot n \\
&<& \displaystyle 1 \cdot \frac{c \lg n}{\lg \lg n} + \frac{1}{n^2} \cdot n \\
&=& \displaystyle \frac{c \lg n}{\lg \lg n} + \frac{1}{n} \\
&=& \displaystyle O(\lg n/ \lg \lg n) \\
\end{array}
$$

$$
\left ( \lim_{n \rightarrow \infty} \frac{\frac{1}{n}}{\frac{\lg n}{\lg \lg n}} = \lim_{n \rightarrow \infty} \frac{\lg (\lg n)}{\lg (n^n)} = 0 \right )
$$

### 11-3 Quadratic probing

> Suppose that we are given a key $$k$$ to search for in a hash table with positions $$0,1,\dots, m-1$$, and suppose that we have a hash function $$h$$ mapping the key space into the set $$\{0,1,\dots,m-1\}$$. The search scheme is as follows:

> 1. Compute the value $$j=h(k)$$, and set $$i=0$$.
> 2. Probe in position $$j$$ for the desired key $$k$$. If you find it, or if this position is empty, terminate the search.
> 3. Set $$i = i + 1$$. If $$i$$ now equals $$m$$, the table is full, so terminate the search. Otherwise, set $$j = (i + j) ~\text{mod}~ m$$, and return to step 2.

> Assume that $$m$$ is a power of 2.

> __*a*__. Show that this scheme is an instance of the general "quadratic probing" scheme by exhibiting the appropriate constants $$c_1$$ and $$c_2$$ for equation (11.5).

The $$i$$th probing is equivalent to $$(j + \frac{i(i+1)}{2}) ~\text{mod}~ m$$, thus $$c_1 = 1/2$$, $$c_2 = 1/2$$.

> __*b*__. Prove that this algorithm examines every table position in the worst case.

Suppose there are two probing $$i$$ and $$j$$, and $$0 \le j < i < m$$.

Suppose the two probing examine the same position, then:

$$
\begin{array}{rlll}
(i + i^2) - (j + j^2) &=& 2km &(k \ge 0) \\
(i+j+1)(i-j) &=& 2km
\end{array}
$$

Since $$i > j$$, then $$k \ne 0$$.

Note that $$m$$ is a power of 2.

If $$i$$ and $$j$$ are both even or both odd, then only $$(i-j)$$ could be even, since $$i < m$$, $$(i - j) < m < 2m$$, thus $$2m$$ could not be a factor of $$(i - j)$$.

If one of $$i$$ and $$j$$ is odd and the other is even, then only $$(i + j + 1)$$ could be even, since $$i < m$$, $$(i + j + 1) < 2m$$, thus $$2m$$ could not be a factor of $$(i + j + 1)$$.

Therefore $$i$$ and $$j$$ could not probing the same position, this algorithm examines every table position in the worst case.








