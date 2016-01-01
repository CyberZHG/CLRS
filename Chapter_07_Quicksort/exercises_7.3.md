## 7.3 A randomized version of quicksort

### 7.3-1

> Why do we analyze the expected running time of a randomized algorithm and not its worst-case running time?

Even with the same input, the running time will be different.

### 7.3-2

> When RANDOMIZED-QUICKSORT runs, how many calls are made to the random-number generator RANDOM in the worst case? How about in the best case? Give your answer in terms of $$\Theta$$-notation.

Worst: 
$$T(n)=T(n-1)+\Theta(1)=\Theta(n)$$

Best: 
$$T(n)=2T(n/2)+\Theta(1)=\Theta(n)$$
