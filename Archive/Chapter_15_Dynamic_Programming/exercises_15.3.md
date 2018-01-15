## 15.3 Elements of dynamic programming

### 15.3-1

> Which is a more efficient way to determine the optimal number of multiplications in a matrix-chain multiplication problem: enumerating all the ways of parenthesizing the product and computing the number of multiplications for each, or running RECURSIVE-MATRIX-CHAIN? Justify your answer.

RECURSIVE-MATRIX-CHAIN

### 15.3-2

> Draw the recursion tree for the MERGE-SORT procedure from Section 2.3.1 on an array of 16 elements. Explain why memoization fails to speed up a good divide-and-conquer algorithm such as MERGE-SORT.

It's not overlapping.

### 15.3-3

> Consider a variant of the matrix-chain multiplication problem in which the goal is to parenthesize the sequence of matrices so as to maximize, rather than minimize, the number of scalar multiplications. Does this problem exhibit optimal substructure?

Yes.

### 15.3-4

> As stated, in dynamic programming we first solve the subproblems and then choose which of them to use in an optimal solution to the problem. Professor Capulet claims that we do not always need to solve all the subproblems in order to find an optimal solution. She suggests that we can find an optimal solution to the matrix-chain multiplication problem by always choosing the matrix $$A_k$$ at which to split the subproduct $$A_iA_{i+1} \cdots A_j$$ (by selecting $$k$$ to minimize the quantity $$p_{i-1}p_kp_j$$) before solving the subproblems. Find an instance of the matrix-chain multiplication problem for which this greedy approach yields a suboptimal solution.

### 15.3-5

> Suppose that in the rod-cutting problem of Section 15.1, we also had limit $$l_i$$ on the number of pieces of length $$i$$ that we are allowed to produce, for $$i = 1,2, \dots ,n$$. Show that the optimal-substructure property described in Section 15.1 no longer holds.

Not independent.

### 15.3-6

> Imagine that you wish to exchange one currency for another. You realize that instead of directly exchanging one currency for another, you might be better off making a series of trades through other currencies, winding up with the currency you want. Suppose that you can trade $$n$$ different currencies, numbered $$1,2,\dots,n$$, where you start with currency $$1$$ and wish to wind up with currency $$n$$. You are given, for each pair of currencies $$i$$ and $$j$$ , an exchange rate $$r_{ij}$$, meaning that if you start with $$d$$ units of currency $$i$$ , you can trade for $$dr_{ij}$$ units of currency $$j$$. A sequence of trades may entail a commission, which depends on the number of trades you make. Let $$c_k$$ be the commission that you are charged when you make $$k$$ trades. Show that, if $$c_k = 0$$ for all $$k = 1,2, \dots, n$$, then the problem of finding the best sequence of exchanges from currency $$1$$ to currency $$n$$ exhibits optimal substructure. Then show that if commissions $$c_k$$ are arbitrary values, then the problem of finding the best sequence of exchanges from currency $$1$$ to currency $$n$$ does not necessarily exhibit optimal substructure.

$$c_k=0$$: $$\displaystyle r_{ij} = \max_k{r_{ik} \cdot r_{kj}}$$.

If $$c_k$$ are arbitrary values, then it's not independent.
