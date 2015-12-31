## Problems

### 9-1 Largest $$i$$ numbers in sorted order

> Given a set of $$n$$ numbers, we wish to find the $$i$$ largest in sorted order using a comparison-based algorithm. Find the algorithm that implements each of the following methods with the best asymptotic worst-case running time, and analyze the running times of the algorithms in terms of $$n$$ and $$i$$ .

> __*a*__. Sort the numbers, and list the $$i$$ largest.

Depends on the sorting algorithm, with heap sort the worst-case is $$O(n\lg n + i)$$.

> __*b*__. Build a max-priority queue from the numbers, and call EXTRACT-MAX $$i$$ times.

Build the heap is $$O(n)$$, extract is $$O(\lg n)$$, thus the worst time is $$O(n + i\lg n)$$.

> __*c*__. Use an order-statistic algorithm to find the $$i$$th largest number, partition around that number, and sort the $$i$$ largest numbers.

$$O(n + n + i\lg i) = O(n + i\lg i)$$.

