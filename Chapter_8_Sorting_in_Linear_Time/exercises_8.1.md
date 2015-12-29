## 8.1 Lower bounds for sorting

### 8.1-1

> What is the smallest possible depth of a leaf in a decision tree for a comparison sort?

For a permutation $$a_1 \le a_2 \le \dots \le a_n$$, there are $$n-1$$ pairs of relative ordering, thus the smallest possible depth is $$n-1$$.

### 8.1-2

> Obtain asymptotically tight bounds on $$\lg(n!)$$ without using Stirling’s approximation. Instead, evaluate the summation $$\sum_{k=1}^n\lg k$$ using techniques from Section A.2.

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n\lg k &\le& \displaystyle \sum_{k=1}^n\lg n \\
&=& n\lg n
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \sum_{k=1}^n\lg k &=& \displaystyle \sum_{k=2}^{n/2}\lg k + \sum_{k=n/2}^n\lg k \\
&\ge& \displaystyle \sum_{k=1}^{n/2}1 + \sum_{k=n/2}^n\lg n/2 \\
&=& \displaystyle \frac{n}{2} + \frac{n}{2}(\lg n - 1) \\
&=& \displaystyle \frac{n}{2}\lg n \\
\end{array}
$$

### 8.1-3

> Show that there is no comparison sort whose running time is linear for at least half of the $$n!$$ inputs of length $$n$$. What about a fraction of $$1/n$$ of the inputs of length $$n$$? What about a fraction $$1/2^n$$?

$$
\begin{array}{rll}
\displaystyle \frac{n!}{2} &\le& 2^h \\
h &\ge& \displaystyle \lg \left (\frac{n!}{2} \right ) \\
&=& (\lg n!) - 1 \\
&=& \Omega(n \lg n) - 1 \\
&=& \Omega(n \lg n)\\
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \frac{n!}{n} &\le& 2^h \\
h &\ge& \displaystyle \lg \left (\frac{n!}{n} \right ) \\
&=& (\lg n!) - \lg n \\
&=& \Omega(n \lg n) - \lg n \\
&=& \Omega(n \lg n)\\
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \frac{n!}{2^n} &\le& 2^h \\
h &\ge& \displaystyle \lg \left (\frac{n!}{2^n} \right ) \\
&=& (\lg n!) - n \\
&=& \Omega(n \lg n) - n \\
&=& \Omega(n \lg n)\\
\end{array}
$$

All of them have the lower-bound $$\Omega(n \lg n)$$.

### 8.1-4

> Suppose that you are given a sequence of $$n$$ elements to sort. The input sequence consists of $$n/k$$ subsequences, each containing $$k$$ elements. The elements in a given subsequence are all smaller than the elements in the succeeding subsequence and larger than the elements in the preceding subsequence. Thus, all that is needed to sort the whole sequence of length n is to sort the $$k$$ elements in each of the $$n/k$$ subsequences. Show an $$\Omega(n\lg k)$$ lower bound on the number of comparisons needed to solve this variant of the sorting problem.