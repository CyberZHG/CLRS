## Problems

### 8-1 Probabilistic lower bounds on comparison sorting

> In this problem, we prove a probabilistic $$\Omega(n \lg n)$$ lower bound on the running time of any deterministic or randomized comparison sort on $$n$$ distinct input elements. We begin by examining a deterministic comparison sort $$A$$ with decision tree $$T_A$$. We assume that every permutation of $$A$$'s inputs is equally likely.

> __*a*__. Suppose that each leaf of $$T_A$$ is labeled with the probability that it is reached given a random input. Prove that exactly $$n!$$ leaves are labeled $$1/n!$$ and that the rest are labeled 0.

There should be only $$n!$$ leaves.

> __*b*__. Let $$D(T)$$ denote the external path length of a decision tree $$T$$ ; that is, $$D(T)$$ is the sum of the depths of all the leaves of $$T$$. Let $$T$$ be a decision tree with $$k > 1$$ leaves, and let $$LT$$ and $$RT$$ be the left and right subtrees of $$T$$. Show that $$D(T)=D(LT)+D(RT)+k$$.

Add $$T$$ means all the $$k$$ depths of leaves increase by 1.

> __*c*__. Let $$d(k)$$ be the minimum value of $$D(T)$$ over all decision trees $$T$$ with $$k > 1$$ leaves. Show that $$d(k)=\min _{1 \le i \le k - 1}\{d(i)+d(k-i)+k\}$$.

$$D(T)=D(LT)+D(RT)+k$$, $$d(k)=\min _{1 \le i \le k - 1}\{d(i)+d(k-i)+k\}$$ iterates all the possibilities.

> __*d*__. Prove that for a given value of $$k > 1$$ and $$i$$ in the range $$1 \le i \le k - 1$$, the function $$i \lg i + (k - i) \lg(k - i)$$ is minimized at $$i = k/2$$. Conclude that $$d(k) = \Omega(k \lg k)$$.

$$
\begin{array}{rll}
f(i) &=& i \lg i + (k - i) \lg (k - i) \\
f'(i) &=& \lg i - \lg (k - i) \\
0 &=& \displaystyle \lg \frac{i}{k-i} \\
1 &=& \displaystyle \frac{i}{k-i} \\
i &=& k / 2 \\
\end{array}
$$

> __*e*__. Prove that $$D(T_A)=\Omega(n!\lg (n!))$$, and conclude that the average-case time to sort $$n$$ elements is $$\Omega(n \lg n)$$.

$$d(T_A) = d(n!) = \Omega(n! \lg n!)$$

Average:
$$
\frac{\Omega(n! \lg n!)}{n!} = \Omega(\lg n!) = \Omega(n \lg n)
$$


> Now, consider a _randomized_ comparison sort $$B$$. We can extend the decision-tree model to handle randomization by incorporating two kinds of nodes: ordinary comparison nodes and "randomization" nodes. A randomization node models a random choice of the form RANDOM$$(1, r)$$ made by algorithm $$B$$; the node has $$r$$ children, each of which is equally likely to be chosen during an execution of the algorithm.

> __*f*__. Show that for any randomized comparison sort $$B$$, there exists a deterministic comparison sort $$A$$ whose expected number of comparisons is no more than those made by $$B$$.

$$\dots$$
