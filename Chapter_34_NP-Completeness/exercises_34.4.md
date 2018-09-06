## 34.4 NP-completeness proofs

### 34.4-1

> Consider the straightforward (nonpolynomial-time) reduction in the proof of Theorem 34.9. Describe a circuit of size $n$ that, when converted to a formula by this method, yields a formula whose size is exponential in $n$.

Construct the circuit as follows: one input $x\_1$ followed by a NOT gate, then followed AND gates which each connects all the outputs of previous steps.

We can encode the circuit in $O(n^k)$, but the formula yielded grows exponentially in each step.

### 34.4-2

> Show the 3-CNF formula that results when we use the method of Theorem 34.10 on the formula (34.3).

$$
\begin{array}{lll}
\phi' = y\_1 &\wedge& (y\_1 \leftrightarrow (y\_2 \wedge \neg x\_2)) \\\\
         &\wedge& (y\_2 \leftrightarrow (y\_3 \vee y\_4)) \\\\
         &\wedge& (y\_3 \leftrightarrow (x\_1 \rightarrow x\_2)) \\\\
         &\wedge& (y\_4 \leftrightarrow \neg y\_5) \\\\
         &\wedge& (y\_5 \leftrightarrow (y\_6 \vee x\_4)) \\\\
         &\wedge& (y\_6 \leftrightarrow (\neg x\_1 \leftrightarrow x\_3)) \\\\
\end{array}
$$

$$
\begin{array}{lll}
\phi'' = y\_1
&\wedge& (\neg y1 \vee \neg y2 \vee \neg x2) \\\\
&\wedge& (\neg y1 \vee y2 \vee \neg x2) \\\\
&\wedge& (\neg y1 \vee y2 \vee x2) \\\\
&\wedge& (y1 \vee \neg y2 \vee x2) \\\\
&\wedge& (\neg y2 \vee y3 \vee y4) \\\\
&\wedge& (y2 \vee \neg y3 \vee \neg y4) \\\\
&\wedge& (y2 \vee \neg y3 \vee y4) \\\\
&\wedge& (y2 \vee y3 \vee \neg y4) \\\\
&\wedge& (\neg y3 \vee \neg x1 \vee x2) \\\\
&\wedge& (y3 \vee \neg x1 \vee \neg x2) \\\\
&\wedge& (y3 \vee x1 \vee \neg x2) \\\\
&\wedge& (y3 \vee x1 \vee x2) \\\\
&\wedge& (\neg y4 \vee \neg y5) \\\\
&\wedge& (y4 \vee y5) \\\\
&\wedge& (\neg y5 \vee y6 \vee x4) \\\\
&\wedge& (y5 \vee \neg y6 \vee \neg x4) \\\\
&\wedge& (y5 \vee \neg y6 \vee x4) \\\\
&\wedge& (y5 \vee y6 \vee \neg x4) \\\\
&\wedge& (\neg y6 \vee \neg x1 \vee \neg x3) \\\\
&\wedge& (\neg y6 \vee x1 \vee x3) \\\\
&\wedge& (y6 \vee \neg x1 \vee x3) \\\\
&\wedge& (y6 \vee x1 \vee \neg x3) \\\\
\end{array}
$$

$$
\begin{array}{lll}
\phi'''
&  =  & (y1 \vee p \vee q) \\\\
&\wedge& (y1 \vee p \vee \neg q) \\\\
&\wedge& (y1 \vee \neg p \vee q) \\\\
&\wedge& (y1 \vee \neg p \vee \neg q) \\\\
&\wedge& (\neg y1 \vee \neg y2 \vee \neg x2) \\\\
&\wedge& (\neg y1 \vee y2 \vee \neg x2) \\\\
&\wedge& (\neg y1 \vee y2 \vee x2) \\\\
&\wedge& (y1 \vee \neg y2 \vee x2) \\\\
&\wedge& (\neg y2 \vee y3 \vee y4) \\\\
&\wedge& (y2 \vee \neg y3 \vee \neg y4) \\\\
&\wedge& (y2 \vee \neg y3 \vee y4) \\\\
&\wedge& (y2 \vee y3 \vee \neg y4) \\\\
&\wedge& (\neg y3 \vee \neg x1 \vee x2) \\\\
&\wedge& (y3 \vee \neg x1 \vee \neg x2) \\\\
&\wedge& (y3 \vee x1 \vee \neg x2) \\\\
&\wedge& (y3 \vee x1 \vee x2) \\\\
&\wedge& (\neg y4 \vee \neg y5 \vee p) \\\\
&\wedge& (\neg y4 \vee \neg y5 \vee \neg p) \\\\
&\wedge& (y4 \vee y5 \vee p) \\\\
&\wedge& (y4 \vee y5 \vee \neg p) \\\\
&\wedge& (\neg y5 \vee y6 \vee x4) \\\\
&\wedge& (y5 \vee \neg y6 \vee \neg x4) \\\\
&\wedge& (y5 \vee \neg y6 \vee x4) \\\\
&\wedge& (y5 \vee y6 \vee \neg x4) \\\\
&\wedge& (\neg y6 \vee \neg x1 \vee \neg x3) \\\\
&\wedge& (\neg y6 \vee x1 \vee x3) \\\\
&\wedge& (y6 \vee \neg x1 \vee x3) \\\\
&\wedge& (y6 \vee x1 \vee \neg x3) \\\\
\end{array}
$$

### 34.4-3

> Professor Jagger proposes to show that SAT $\le\_\text{P}$ 3-CNF-SAT by using only the truth-table technique in the proof of Theorem 34.10, and not the other steps. That is, the professor proposes to take the boolean formula $\phi$, form a truth table for its variables, derive from the truth table a formula in 3-DNF that is equivalent to $\neg \phi$, and then negate and apply DeMorgan's laws to produce a 3-CNF formula equivalent to $\phi$. Show that this strategy does not yield a polynomial-time reduction.

Suppose the number of variables in the formula is $n$, the number of rows in the truth table is $2^n$.

### 34.4-4

> Show that the problem of determining whether a boolean formula is a tautology is complete for co-NP. (Hint: See Exercise 34.3-7.)

Suppose the language of determining whether a boolean formula is a tautology is $L$ and the boolean formula is denoted by $\phi$. Then $\overline{L}$ is equivalent to 3-CNF-SAT with formula $\neg \phi$, therefore $\overline{L}$ is complete for NP. Based on Exercise 34.3-7, $L$ is complete for co-NP.

### 34.4-5

> Show that the problem of determining the satisfiability of boolean formulas in disjunctive normal form is polynomial-time solvable.

The formula in disjunctive normal form evaluates to 1 if any of the clauses in it could be evaluated to 1. A cluase could be evaluated to 1 if there isn't a literal $x$ that both $x$ and $\neg x$ appeared in the clause. Thus suppose there are $n$ clauses and the maximum number of literals in one clause is $m$, the time complexity is $O(nm^2)$.

### 34.4-6

> Suppose that someone gives you a polynomial-time algorithm to decide formula satisfiability. Describe how to use this algorithm to find satisfying assignments in polynomial time.

Suppose the algorithm is $A$, the formula is $\phi$ and the variables are $(x\_1, ..., x\_n)$.

If $A$ rejects $\phi$, then there is no solution.

Else if $A$ accepts $\phi$, then for each $x\_i$, replace $x\_i$ by 0, if the transformed formula $\phi'$ is accepted by $A$, then $x\_i = 0$, otherwise $x\_i = 1$.

### 34.4-7

> Let 2-CNF-SAT be the set of satisfiable boolean formulas in CNF with exactly 2 literals per clause. Show that 2-CNF-SAT $\in$ P. Make your algorithm as efficient as possible. (Hint: Observe that $x \vee y$ is equivalent to $\neg x \rightarrow y$. Reduce 2-CNF-SAT to an efficiently solvable problem on a directed graph.)

[2SAT](http://www.math.ucsd.edu/~sbuss/CourseWeb/Math268_2007WS/2SAT.pdf)
