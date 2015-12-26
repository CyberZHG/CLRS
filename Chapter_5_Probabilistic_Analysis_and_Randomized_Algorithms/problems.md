## Problems

### 5-1 Probabilistic counting

> With a $$b$$-bit counter, we can ordinarily only count up to $$2^b - 1$$. With R. Morris’s __*probabilistic counting*__, we can count up to a much larger value at the expense of some loss of precision.

> We let a counter value of $$i$$ represent a count of $$n_i$$ for $$i = 0, 1, \dots , 2^b-1$$, where the $$n_i$$ form an increasing sequence of nonnegative values. We assume that the initial
value of the counter is $$0$$, representing a count of $$n_0 = 0$$. The INCREMENT operation works on a counter containing the value $$i$$ in a probabilistic manner. If $$i = 2^b - 1$$, then the operation reports an overflow error. Otherwise, the INCREMENT
operation increases the counter by 1 with probability $$1/(n_{i+1}-n_i)$$, and it leaves the counter unchanged with probability $$1-1/(n_{i+1}-n_i)$$.

> If we select $$n_i = i$$ for all $$i \ge 0$$, then the counter is an ordinary one. More interesting situations arise if we select, say, $$n_i = 2^{i-1}$$ for $$i > 0$$ or $$n_i = F_i$$ (the
$$i$$th Fibonacci number—see Section 3.2).

> For this problem, assume that $$n_{2^b-1}$$ is large enough that the probability of an overflow error is negligible.

> __*a*__. Show that the expected value represented by the counter after $$n$$ INCREMENT operations have been performed is exactly $$n$$.

> __*b*__. The analysis of the variance of the count represented by the counter depends on the sequence of the $$n_i$$. Let us consider a simple case: $$n_i = 100i$$ for all $$i \ge 0$$. Estimate the variance in the value represented by the register after $$n$$
INCREMENT operations have been performed.

### 5-2 Searching an unsorted array

> This problem examines three algorithms for searching for a value $$x$$ in an unsorted array $$A$$ consisting of $$n$$ elements.

> Consider the following randomized strategy: pick a random index $$i$$ into $$A$$. If $$A[i]=x$$, then we terminate; otherwise, we continue the search by picking a new random index into $$A$$. We continue picking random indices into $$A$$ until we find an index $$j$$ such that $$A[j]=x$$ or until we have checked every element of $$A$$. Note that we pick from the whole set of indices each time, so that we may examine a given element more than once.

> __*a*__. Write pseudocode for a procedure RANDOM-SEARCH to implement the strategy above. Be sure that your algorithm terminates when all indices into $$A$$ have been picked.

> __*b*__. Suppose that there is exactly one index $$i$$ such that $$A[i]=x$$. What is the expected number of indices into $$A$$ that we must pick before we find $$x$$ and RANDOM-SEARCH terminates?

> __*c*__. Generalizing your solution to part (b), suppose that there are $$k \ge 1$$ indices $$i$$ such that $$A[i]=x$$. What is the expected number of indices into $$A$$ that we must pick before we find $$x$$ and RANDOM-SEARCH terminates? Your answer should be a function of $$n$$ and $$k$$.

> __*d*__. Suppose that there are no indices $$i$$ such that $$A[i]=x$$. What is the expected number of indices into $$A$$ that we must pick before we have checked all elements of $$A$$ and RANDOM-SEARCH terminates?


> Now consider a deterministic linear search algorithm, which we refer to as DETERMINISTIC-SEARCH. Specifically, the algorithm searches $$A$$ for $$x$$ in order, considering $$A[1], A[2], A[3], \dots, A[n]$$ until either it finds $$A[i]=x$$ or it reaches the end of the array. Assume that all possible permutations of the input array are equally likely.

> __*e*__. Suppose that there is exactly one index $$i$$ such that $$A[i]=x$$. What is the average-case running time of DETERMINISTIC-SEARCH? What is the worst-case running time of DETERMINISTIC_SERACH?

> __*f*__. Generalizing your solution to part (e), suppose that there are $$k \ge 1$$ indices $$i$$ such that $$A[i]=x$$. What is the average-case running time of DETERMINISTICSEARCH? What is the worst-case running time of DETERMINISTIC-SEARCH? Your answer should be a function of $$n$$ and $$k$$.

> __*g*__. Suppose that there are no indices $$i$$ such that $$A[i]=x$$. What is the average-case running time of DETERMINISTIC-SEARCH? What is the worst-case running time of DETERMINISTIC-SEARCH? 

> Finally, consider a randomized algorithm SCRAMBLE-SEARCH that works by first randomly permuting the input array and then running the deterministic linear search given above on the resulting permuted array.

> __*h*__. Letting $$k$$ be the number of indices $$i$$ such that $$A[i]=x$$, give the worst-case and expected running times of SCRAMBLE-SEARCH for the cases in which $$k = 0$$ and $$k = 1$$. Generalize your solution to handle the case in which $$k \ge 1$$. 

> __*i*__. Which of the three searching algorithms would you use? Explain your answer.

