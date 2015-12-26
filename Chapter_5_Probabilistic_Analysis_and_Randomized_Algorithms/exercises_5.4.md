## Probabilistic analysis and further uses of indicator random variables

### 5.4-1 

> How many people must there be in a room before the probability that someone has the same birthday as you do is at least $$1/2$$? How many people must there be before the probability that at least two people have a birthday on July 4 is greater than $$1/2$$?

$$
1 - \left ( \frac{n - 1}{n} \right ) ^ {m} \ge \frac{1}{2}
$$

$$
m \ge \log_{364/365}\frac{1}{2} = 252.6519888441586
$$

Thus there must be 253 people.

$$
1 - \binom{m}{1}\frac{1}{n} \left ( \frac{n-1}{n} \right ) ^ {m-1} - \left ( \frac{n-1}{n} \right ) ^ {m} \ge \frac{1}{2}
$$

There must be 613 people.

### 5.4-2

> Suppose that we toss balls into $$b$$ bins until some bin contains two balls. Each toss is independent, and each ball is equally likely to end up in any bin. What is the expected number of ball tosses?

Same as the birthday paradox.

### 5.4-3 $$\star$$

> For the analysis of the birthday paradox, is it important that the birthdays be mutually independent, or is pairwise independence sufficient? Justify your answer.

$$X_{ij}$$ uses the pairwise independence, thus it is sufficient for proving.

### 5.4-4 $$\star$$

> How many people should be invited to a party in order to make it likely that there are _three_ people with the same birthday?

$$
X_{ijk}=\frac{1}{n^2}
$$

$$
\begin{array}{rll}
E[X] &=& E \left [ \sum_{i=1}^m \sum_{j=i+1}^m \sum_{k=j+1}^m X_{ijk} \right ] \\
&=& \sum_{i=1}^m \sum_{j=i+1}^m \sum_{k=j+1}^m E \left [ X_{ijk} \right ] \\
&=& \sum_{i=1}^m \sum_{j=i+1}^m \sum_{k=j+1}^m \frac{1}{n^2} \\
&=& \binom{m}{3} \frac{1}{n^2} \\
&=& \frac{m \cdot (m-1) \cdot (m-2)}{6n^2}
\end{array}
$$

$$
m \cdot (m-1) \cdot (m-2) \ge 6n^2
$$

At least 94 people.

### 5.4-5 $$\star$$

> What is the probability that a $$k$$-string over a set of size $$n$$ forms a $$k$$-permutation? How does this question relate to the birthday paradox?

Complementary to the birthday paradox.

$$
Pr = 1 \cdot \frac{n-1}{n} \cdot \frac{n-2}{n} \cdot \cdots \cdot \frac{n-k + 1}{n}
$$

### 5.4-6 $$\star$$

> Suppose that $$n$$ balls are tossed into $$n$$ bins, where each toss is independent and the ball is equally likely to end up in any bin. What is the expected number of empty bins? What is the expected number of bins with exactly one ball?

* the expected number of empty bins

$$
E[X_i] = \left ( 1 - \frac{1}{n} \right )^n \approx \frac{1}{e}
$$

$$
\begin{array}{rll}
E[X] &=& \sum_{i=1}^n E[X_i] \\
&=& \sum_{i=1}^n \frac{1}{e} \\
&=& n/e \\
\end{array}
$$

* the expected number of bins with exactly one ball

$$
E[X_i] = \binom{n}{1}\frac{1}{n}\left ( 1 - \frac{1}{n} \right )^{n-1} = \left ( 1 - \frac{1}{n} \right )^n\frac{n}{n-1} \approx \frac{1}{e}
$$

$$
E[X] = \frac{n}{e}
$$


### 5.4-7 $$\star$$

> Sharpen the lower bound on streak length by showing that in $$n$$ flips of a fair coin, the probability is less than $$1/n$$ that no streak longer than $$\lg n - 2 \lg \lg n$$ consecutive heads occurs.

$$\dots$$
