## Problems

### 15-1 Longest simple path in a directed acyclic graph

> Suppose that we are given a directed acyclic graph $$G = (V, E)$$ with real-valued edge weights and two distinguished vertices $$s$$ and $$t$$ . Describe a dynamic-programming approach for finding a longest weighted simple path from $$s$$ to $$t$$ . What does the subproblem graph look like? What is the efficiency of your algorithm?

Topological sort.

### 15-2 Longest palindrome subsequence

> A __*palindrome*__ is a nonempty string over some alphabet that reads the same forward and backward. Examples of palindromes are all strings of length 1, civic, racecar, and aibohphobia (fear of palindromes). 
> Give an efficient algorithm to find the longest palindrome that is a subsequence of a given input string. For example, given the input character, your algorithm should return carac. What is the running time of your algorithm?

LCS of the original string and the reversed string.

### 15-3 Bitonic euclidean traveling-salesman problem

> In the __*euclidean traveling-salesman problem*__, we are given a set of n points in the plane, and we wish to find the shortest closed tour that connects all n points. Figure 15.11(a) shows the solution to a 7-point problem. The general problem is NP-hard, and its solution is therefore believed to require more than polynomial time (see Chapter 34).
J. L. Bentley has suggested that we simplify the problem by restricting our attention to __*bitonic tours*__, that is, tours that start at the leftmost point, go strictly rightward to the rightmost point, and then go strictly leftward back to the starting point. Figure 15.11(b) shows the shortest bitonic tour of the same 7 points. In this case, a polynomial-time algorithm is possible.
Describe an $$O(n^2)$$-time algorithm for determining an optimal bitonic tour. You may assume that no two points have the same $$x$$-coordinate and that all operations on real numbers take unit time.

Sort the points by their $$x$$-coordinates, and suppose there are $$n$$ points. Let $$dp[i][j]$$ be the minimal distance from $$i$$ to the first point and from the first point to $$j$$. Since $$dp[i][j]$$ is symmetric, suppose that $$j < i$$, then $$\displaystyle \min_{j} dp[j][n]$$ is the shortest bitnoic tour. If $$j=i-1$$, $$\displaystyle dp[i][j]=\min_{k=1}^{i-2} dp[i-1][k] + dist(k, i)$$; if $$j<i-1$$, $$dp[i][j] = dp[i-1][j] + dist(i - 1, i)$$.

### 15-4 Printing neatly

> Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of $$n$$ words of lengths $$l_1, l_2, \dots , l_n$$, measured in characters. We want to print this paragraph neatly on a number of lines that hold a maximum of $$M$$ characters each. Our criterion of "neatness" is as follows. If a given line contains words $$i$$ through $$j$$, where $$i \le j$$ , and we leave exactly one space between words, the number of extra space characters at the end of the line is $$M - j + i - \sum_{k=i}^j l_k$$, which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. Give a dynamic-programming algorithm to print a paragraph of $$n$$ words neatly on a printer. Analyze the running time and space requirements of your algorithm.
