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

Let $$dp[m]$$ be the minimal sum when we finshed printing $$m$$ words. 
$$
dp[m] = dp[m-k] + cost(m-k+1, m)
$$$$
cost(i, j) = \left \{ 
\begin{matrix}
\infty & \text{if}~M - j + i - \sum_{k=i}^j l_k < 0 \\
0 & \text{if}~j = n\\
\left ( M - j + i - \sum_{k=i}^j l_k \right ) ^ 3 & \text{otherwise}
\end{matrix}
\right .
$$
### 15-5 Edit distance

> In order to transform one source string of text $$x[1 \dots m]$$ to a target string $$y[1 \dots n]$$, we can perform various transformation operations. Our goal is, given $$x$$ and $$y$$, to produce a series of transformations that change $$x$$ to $$y$$. We use an array $$z$$—assumed to be large enough to hold all the characters it will need—to hold the intermediate results. Initially, $$z$$ is empty, and at termination, we should have $$z[j] = y[j]$$ for $$j = 1,2, \dots ,n$$. We maintain current indices $$i$$ into $$x$$ and $$j$$ into $$z$$, and the operations are allowed to alter $$z$$ and these indices. Initially, $$i = j = 1$$. We are required to examine every character in $$x$$ during the transformation, which means that at the end of the sequence of transformation operations, we must have $$i = m + 1$$.

> We may choose from among six transformation operations:

> __Copy__ a character from $$x$$ to $$z$$ by setting $$z[j]=x[i]$$ and then incrementing both $$i$$ and $$j$$. This operation examines $$x[i]$$.

> __Replace__ a character from $$x$$ by another character $$c$$, by setting $$z[j] = c$$, and then incrementing both $$i$$ and $$j$$. This operation examines $$x[i]$$.

> __Delete__ a character from $$x$$ by incrementing $$i$$ but leaving $$j$$ alone. This operation examines $$x[i]$$.

> __Insert__ the character $$c$$ into $$z$$ by setting $$z[j] = c$$ and then incrementing $$j$$, but leaving $$i$$ alone. This operation examines no characters of $$x$$.

> __Twiddle__ (i.e., exchange) the next two characters by copying them from $$x$$ to $$z$$ but in the opposite order; we do so by setting $$z[j] = x[i+1]$$ and $$z[j+1] = x[i]$$ and then setting $$i=i+2$$ and $$j=j+2$$. This operation examines $$x[i]$$ and $$x[i+1]$$.

> __Kill__ the remainder of $$x$$ by setting $$i=m+1$$. This operation examines all characters in $$x$$ that have not yet been examined. This operation, if performed, must be the final operation.

> __*a*__. Given two sequences $$x[1 \dots m]$$ and $$y[1 \dots n]$$ and set of transformation-operation costs, the __*edit distance*__ from $$x$$ to $$y$$ is the cost of the least expensive operatoin sequence that transforms $$x$$ to $$y$$. Describe a dynamic-programming algorithm that finds the edit distance from $$x[1 \dots m]$$ to $$y[1 \dots n]$$ and prints an optimal opeartion sequence. Analyze the running time and space requirements of your algorithm.

* __Copy__: $$dp[i][j] = dp[i - 1][j - 1] + cost(copy)$$ if $$x[i] = y[j]$$. 
* __Replace__: $$dp[i][j] = dp[i-1][j-1] + cost(replace)$$ if $$x[i] \ne y[j]$$.
* __Delete__: $$dp[i][j] = dp[i-1][j] + cost(delete)$$.
* __Insert__: $$dp[i][j] = dp[i][j-1] + cost(insert)$$.
* __Twiddle__: $$dp[i][j] = dp[i-2][j-2] + cost(twiddle)$$ if $$x[i-1] = y[j]$$ and $$x[i] = y[j-1]$$.
* __Kill__: $$dp[i][j] = \min_{k=1}^{i} dp[k][j] + cost(kill)$$ if $$j = n$$.

> The edit-distance problem generalizes the problem of aligning two DNA sequences (see, for example, Setubal and Meidanis [310, Section 3.2]). There are several methods for measuring the similarity of two DNA sequences by aligning them. One such method to align two sequences $$x$$ and $$y$$ consists of inserting spaces at arbitrary locations in the two sequences (including at either end) so that the resulting sequences $$x'$$ and $$y'$$ have the same length but do not have a space in the same position (i.e., for no position $$j$$ are both $$x'[j]$$ and $$y'[j]$$ a space). Then we assign a "score" to each position. Position $$j$$ receives a score as follows:
> * +1 if $$x'[j] = y'[j]$$ and neither is a space,
> * -1 if $$x'[j] \ne y'[j]$$ and neither is a space,
> * -2 if eigher $$x'[j]$$ or $$y'[j]$$ is a space.

> __*b*__. Explain how to cast the problem of finding an optimal alignment as an edit distance problem using a subset of the transformation operations copy, replace, delete, insert, twiddle, and kill.

$$cost(copy) = +1$$, $$cost(replace)=-1$$, $$cost(delete)=cost(insert)=1$$.

### 15-6 Planning a company party

> Professor Stewart is consulting for the president of a corporation that is planning a company party. The company has a hierarchical structure; that is, the supervisor relation forms a tree rooted at the president. The personnel office has ranked each employee with a conviviality rating, which is a real number. In order to make the party fun for all attendees, the president does not want both an employee and his or her immediate supervisor to attend. 

> Professor Stewart is given the tree that describes the structure of the corporation, using the left-child, right-sibling representation described in Section 10.4. Each node of the tree holds, in addition to the pointers, the name of an employee and that employee’s conviviality ranking. Describe an algorithm to make up a guest list that maximizes the sum of the conviviality ratings of the guests. Analyze the running time of your algorithm.

Let $$dp[i][j]$$ be the maximal sum rooted at $$i$$, $$j=0$$ means $$i$$ will not attend, $$j=1$$ means $$i$$ will attend. $$dp[i][0] = \max_{j} (dp[j][0], dp[j][1])$$, $$dp[i][1] = \max_j dp[j][0]$$.

### 15-7 Viterbi algorithm

> We can use dynamic programming on a directed graph $$G = (V, E)$$ for speech recognition. Each edge $$(u, v) \in E$$ is labeled with a sound $$\sigma(u, v)$$ from a finite set $$\Sigma$$ of sounds. The labeled graph is a formal model of a person speaking a restricted language. Each path in the graph starting from a distinguished vertex $$v_0 \in V$$ corresponds to a possible sequence of sounds producted by the model. We define the label of a directed path to be the concatenation of the labels of the edges on that path.

> __*a*__. Describe an efficient algorithm that, given an edge-labeled graph $$G$$ with distinguished vertex $$v_0$$ and a sequence $$s = \left \langle \sigma_1, \sigma_2, \dots \sigma_k \right \rangle$$ of sounds from $$\Sigma$$, returns a path in $$G$$ that begins at $$v_0$$ and has $$s$$ as its label, if any such path exists. Otherwise, the algorithm should return NO-SUCH-PATH. Analyze the running time of your algorithm.

Let $$dp[i][j]$$ be the state of vertex $$j$$ in iteration $$i$$, $$dp[0][v_0] = true$$.

$$
dp[i][j] = \left \{ \begin{matrix}
1 & \exists_{k} dp[i-1][k]=1 ~\text{and}~ \sigma(k, i) = \sigma_i \\
0 & \text{otherwise}
\end{matrix} \right .
$$

> Now, suppose that every edge $$(u, v) \in E$$ has an associated nonnegatve probability $$p(u, v)$$ of traversing the edge $$(u, v)$$ from vertex $$u$$ and thus producing the corresponding sound. The sum of the probabilities of the edges leaving any vertex equals $$1$$. The probability of a path is defined to the product of the probabilities of its edges. We can view the probability of a path beginning at $$v_0$$ as the probability that a "random walk" beginning at $$v_0$$ will follow the specified path, where we randomly choose which edge to take leaving a vertex $$u$$ according to the probabilities of the available edges leaving $$u$$.

> __*b*__. Extend your answer to part (a) so that if a path is returned, it is a _most probable path_ starting at $$v_0$$ and having label $$s$$. Analyze the running time of your algorithm.

$$dp[0][v_0] = 1.0$$.

$$
dp[i][j] = \max_{dp[i-1][k]=1 ~\text{and}~ \sigma(k, i) = \sigma_i} dp[i-1][k] \cdot p(k, i)
$$
### 15-8 Image compression by seam carving

> We are given a color picture consisting of an $$m \times n$$ array $$A[1 \dots m, 1 \dots n]$$ of pixels, where each pixel specifies a triple of red, green, and blue (RGB) intensities. Suppose that we wish to compress this picture slightly. Specifically, we wish to remove one pixel from each of the $$m$$ rows, so that the whole picture becomes one pixel narrower. To avoid disturbing visual effects, however, we require that the pixels removed in two adjacent rows be in the same or adjacent columns; the pixels removed form a "seam" from the top row to the bottom row where successive pixels in the seam are adjacent vertically or diagonally.

> __*a*__. Show that the number of such possible seams grows at least exponentially in $$m$$, assuming that $$n > 1$$.

num$$\ge 2^n$$.

> __*b*__. Suppose now that along with each pixel $$A[i, j]$$, we have calculated a real-valued disruption measure $$d[i, j]$$, indicating how disruptive it would be to remove pixel $$A[i, j]$$. Intuitively, the lower a pixel's disruption measure, the more similar the pixel is to its neighbors. Suppose further that we define the disruption measure of a seam to be the sum of the disruption measures of its pixels.

> Give an algorithm to find a seam with the lowest disruption measure. How efficient is your algorithm?

$$dp[i,j] = d[i,j] + \min (dp[i-1,j-1], dp[i-1,j], dp[i-1,j+1])$$.

### 15-9 Breaking a string

A certain string-processing language allows a programmer to break a string into two pieces. Because this operation copies the string, it costs $$n$$ time units to break a string of $$n$$ characters into two pieces. Suppose a programmer wants to break a string into many pieces. The order in which the breaks occur can affect the total amount of time used. For example, suppose that the programmer wants to break a 20-character string after characters 2, 8, and 10 (numbering the characters in ascending order from the left-hand end, starting from 1). If she programs the breaks to occur in left-to-right order, then the first break costs 20 time units, the second break costs 18 time units (breaking the string from characters 3 to 20 at character 8), and the third break costs 12 time units, totaling 50 time units. If she programs the breaks to occur in right-to-left order, however, then the first break costs 20 time units, the second break costs 10 time units, and the third break costs 8 time units, totaling 38 time units. In yet another order, she could break first at 8 (costing 20), then break the left piece at 2 (costing 8), and finally the right piece at 10 (costing 12), for a total cost of 40.

Design an algorithm that, given the numbers of characters after which to break, determines a least-cost way to sequence those breaks. More formally, given a string $$S$$ with $$n$$ characters and an array $$L[1 \dots m]$$ containing the break points, compute the lowest cost for a sequence of breaks, along with a sequence of breaks that achieves this cost.

$$
dp[i][j] = len(i, j) + \min_{k=i+1}^{j-1} (dp[i][k] + dp[k+1][j])
$$
### 15-10 Planning an investment strategy

> Your knowledge of algorithms helps you obtain an exciting job with the Acme Computer Company, along with a $10,000 signing bonus. You decide to invest this money with the goal of maximizing your return at the end of 10 years. You decide to use the Amalgamated Investment Company to manage your investments. Amalgamated Investments requires you to observe the following rules. It offers $$n$$ different investments, numbered $$1$$ through $$n$$. In each year $$j$$, investment $$i$$ provides a return rate of $$r_{ij}$$ . In other words, if you invest $$d$$ dollars in investment $$i$$ in year $$j$$, then at the end of year $$j$$ , you have $$dr_{ij}$$ dollars. The return rates are guaranteed, that is, you are given all the return rates for the next 10 years for each investment. You make investment decisions only once per year. At the end of each year, you can leave the money made in the previous year in the same investments, or you can shift money to other investments, by either shifting money between existing investments or moving money to a new investement. If you do not move your money between two consecutive years, you pay a fee of $$f_1$$ dollars, whereas if you switch your money, you pay a fee of $$f_2$$ dollars, where $$f_2 > f_1$$.

Let $$dp[j][i]$$ be the maximal profit in year $$j$$ with the last investment $$i$$.

$$
dp[j][i] = \left \{ \begin{matrix}
dp[j-1][k] \cdot r_{kj} + f_2 & (k \ne i) \\
dp[j-1][i] \cdot r_{ij} + f_1
\end{matrix} \right .
$$
