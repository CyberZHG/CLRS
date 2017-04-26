## 15.4 Longest common subsequence

### 15.4-1

> Determine an LCS of $$\langle 1, 0, 0, 1, 0, 1, 0, 1\rangle$$ and $$\langle 0, 1, 0, 1, 1, 0, 1, 1, 0\rangle$$.

$$\langle 1, 0, 0, 1, 1, 0 \rangle$$.

### 15.4-2

> Give pseudocode to reconstruct an LCS from the completed $$c$$ table and the original sequences $$X = \langle x_1, x_2, \dots, x_m \rangle$$ and $$Y = \langle y_1, y_2, \dots, y_n\rangle$$ in $$O(m + n)$$ time, without using the $$b$$ table.

```
PRINT-LCS(c, X, Y, i, j)
 1 if c[i][j] == 0
 2     return
 3 if X[i] == Y[j]
 4     PRINT-LCS(c, X, Y, i - 1, j - 1)
 5     print X[i]
 6 elseif c[i - 1][j] > c[i][j - 1]
 7     PRINT-LCS(c, X, Y, i - 1, j)
 8 else
 9     PRINT-LCS(c, X, Y, i, j - 1)
```

### 15.4-3

> Give a memoized version of LCS-LENGTH that runs in $$O(mn)$$ time.

```
  1 def LCS-LENGTH(str1, str2):
  2     lens = [[0]*len(str1) for i in range(len(str2))]
  3 
  4     for i in range(len(str1)):
  5         for j in range(len(str2)):
  6             if str1[i] == str2[j]:
  7                 lens[i+1][j+1] = lens[i][j] + 1
  8             else:
  9                 lens[i+1][j+1] = max(lens[i+1][j], lens[i][j+1])
 10 return lens[len(str1)][len(str2)]
```

### 15.4-4

> Show how to compute the length of an LCS using only $$2 \cdot \min(m, n)$$ entries in the $$c$$ table plus $$O(1)$$ additional space. Then show how to do the same thing, but using $$\min(m, n)$$ entries plus $$O(1)$$ additional space.

$$2 \cdot \min(m, n)$$: rolling.

$$\min(m, n)$$: save the old value of the last computed position.

### 15.4-5

> Give an $$O(n^2)$$-time algorithm to find the longest monotonically increasing subsequence of a sequence of $$n$$ numbers.

Calculate the LCS of the original sequence and the sorted sequence, $$O(n \lg n) + O(n^2)=O(n^2)$$ time.

### 15.4-6 $$\star$$

> Give an $$O(n \lg n)$$-time algorithm to find the longest monotonically increasing subsequence of a sequence of $$n$$ numbers.

Binary search.
