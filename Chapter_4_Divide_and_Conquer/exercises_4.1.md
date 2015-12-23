## The maximum-subarray problem

### 4.1-1

> What does FIND-MAXIMUM-SUBARRAY return when all elements of $$A$$ are negative?

(smallest_index, smallest_index, smallest_value)

### 4.1-2

> Write pseudocode for the brute-force method of solving the maximum-subarray problem. Your procedure should run in $$\Theta(n^2)$$ time.

```python
def find_maximum_subarray(arr):
    sums = [0]
    for a in arr:
        sums.append(sums[-1] + a)
    max_sum = -1e100
    left_index = -1
    right_index = -1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sums[j + 1] - sums[i] > max_sum:
                max_sum = sums[j + 1] - sums[i]
                left_index = i
                right_index = j
    return left_index, right_index, max_sum
```

### 4.1-3

> Implement both the brute-force and recursive algorithms for the maximumsubarray problem on your own computer. What problem size $$n_0$$ gives the crossover point at which the recursive algorithm beats the brute-force algorithm? Then, change the base case of the recursive algorithm to use the brute-force algorithm whenever the problem size is less than $$n_0$$. Does that change the crossover point?

```python
def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -1e100
    sum = 0
    for i in range(mid - 1, low - 1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1e100
    sum = 0
    for j in range(mid, high):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(arr, low, high):
    if low >= high:
        return -1, -1, -1e100
    if low + 1 == high:
        return low, low, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum
```

### 4.1-4

> Suppose we change the definition of the maximum-subarray problem to allow the result to be an empty subarray, where the sum of the values of an empty subarray is 0. How would you change any of the algorithms that do not allow empty subarrays to permit an empty subarray to be the result?

Return empty if the result is negative.

### 4.1-5

> Use the following ideas to develop a nonrecursive, linear-time algorithm for the maximum-subarray problem. Start at the left end of the array, and progress toward subarray seen so far. Knowing a maximum subarray of $$A[1 \dots j]$$, extend the answer to find a maximum subarray ending at index $$j+1$$ by using the following observation: a maximum subarray of $$A[1 \dots j+1]$$ is either a maximum subarray of $$A[1 \dots j]$$ or a subarray $$A[i \dots j+1]$$, for some $$1 \le i \le j + 1$$. Determine a maximum subarray of the form $$A[i \dots j+1]$$ in constant time based on knowing a maximum subarray ending at index $$j$$ .

```python
def find_maximum_subarray(arr):
    max_sum = -1e100
    max_left, max_right = -1, -1
    sum = 0
    last_left = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            max_left = last_left
            max_right = i
        if sum < 0:
            sum = 0
            last_left = i + 1
    return max_left, max_right, max_sum
```
