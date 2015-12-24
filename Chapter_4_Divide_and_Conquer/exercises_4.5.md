## The master method for solving recurrences

### 4.5-1

> Use the master method to give tight asymptotic bounds for the following recurrences.

> __a__. $$T(n)=2T(n/4)+1$$.

$$\Theta(n^{\log_42}=\Theta(\sqrt{n})$$

> __b__. $$T(n)=2T(n/4)+\sqrt{n}$$.

$$\Theta(\sqrt{n}\lg n)$$

> __c__. $$T(n)=2T(n/4)+n$$.

$$\Theta(n)$$

> __d__. $$T(n)=2T(n/4)+n^2$$

$$\Theta(n^2)$$

### 4.5-2

> Professor Caesar wishes to develop a matrix-multiplication algorithm that is asymptotically faster than Strassen’s algorithm. His algorithm will use the divide and conquer method, dividing each matrix into pieces of size $$n/4\times n/4$$, and the divide and combine steps together will take $$\Theta(n^2)$$ time. He needs to determine how many subproblems his algorithm has to create in order to beat Strassen’s algorithm. If his algorithm creates a subproblems, then the recurrence for the running time $$T(n)$$ becomes $$T(n)=aT(n/4)+\Theta(n^2)$$. What is the largest integer value of $$a$$ for which Professor Caesar’s algorithm would be asymptotically faster than Strassen’s algorithm?

$$\log_4a<\log_27$$

The largest $$a$$ is 48.

### 4.5-3

> Use the master method to show that the solution to the binary-search recurrence $$T(n)=T(n/2)+\Theta(1)$$ is $$T(n)=\Theta(\lg n)$$. (See Exercise 2.3-5 for a description of binary search.)

$$n^{log_21}=1$$

$$T(n)=\lg n$$

### 4.5-4

> Can the master method be applied to the recurrence $$T(n)=4T(n/2)+n^2\lg n$$? Why or why not? Give an asymptotic upper bound for this recurrence.

No. $$O(n^2\lg^n)$$.

### 4.5-5 $$\star$$

> Consider the regularity condition $$af(n/b) \le cf(n)$$ for some constant $$c < 1$$, which is part of case 3 of the master theorem. Give an example of constants $$a \ge 1$$ and $$b > 1$$ and a function $$f(n)$$ that satisfies all the conditions in case 3 of the master theorem except the regularity condition.

$$T(n)=T(n/2)+n(sin(n-\pi/2)+2)$$
