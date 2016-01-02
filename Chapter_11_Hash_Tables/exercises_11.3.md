## 11.3 Hash functions

### 11.3-1

> Suppose we wish to search a linked list of length $$n$$, where each element contains a key $$k$$ along with a hash value $$h(k)$$. Each key is a long character string. How might we take advantage of the hash values when searching the list for an element with a given key?

Compare the long character strings only when they have the same hash values.

### 11.3-2

> Suppose that we hash a string of $$r$$ characters into $$m$$ slots by treating it as a radix-128 number and then using the division method. We can easily represent the number $$m$$ as a 32-bit computer word, but the string of $$r$$ characters, treated as a radix-128 number, takes many words. How can we apply the division method to compute the hash value of the character string without using more than a constant number of words of storage outside the string itself?

```
sum := 0
for i = 1 to r
    sum := (sum * 128 + s[i]) % m
```

Use `sum` as the key.

### 11.3-3

> Consider a version of the division method in which $$h(k) = k~\text{mod}~m$$, where $$m = 2^p - 1$$ and $$k$$ is a character string interpreted in radix $$2^p$$. Show that if we can derive string $$x$$ from string $$y$$ by permuting its characters, then $$x$$ and $$y$$ hash to the same value. Give an example of an application in which this property would be undesirable in a hash function.

$$2^p ~\text{mod}~ (2^p-1)=1$$

$$c \cdot (2^p)^x ~\text{mod}~ (2^p-1)= c \cdot 1^x = c$$

Thus the hashing is equivalent to $$(\sum c_i)~\text{mod}~m$$, the strings with different permutations will have the same hashing value.

### 11.3-4

> Consider a hash table of size $$m=1000$$ and a corresponding hash function $$h(k) = \lfloor m (kA ~\text{mod}~ 1) \rfloor$$ for $$A=(\sqrt{5}-1)/2$$. Compute the locations to which the keys 61, 62, 63, 64, and 65 are mapped.

$$h(61)=700$$

$$h(62)=318$$

$$h(63)=936$$

$$h(64)=554$$

$$h(65)=172$$

### 11.3-5 $$\star$$

> Define a family $$\mathcal{H}$$ of hash functions from a finite set $$U$$ to a finite set $$B$$ to be __*$$\epsilon$$-universal*__ if for all pairs of distinct elements $$k$$ and $$l$$ in $$U$$,

> $$\text{Pr}\{h(k)=h(l)\} \le \epsilon$$,

> where the probability is over the choice of the hash function $$h$$ drawn at random from the family $$\mathcal{H}$$. Show that an $$\epsilon$$-universal family of hash functions must have

> $$\displaystyle \epsilon \ge \frac{1}{|B|} - \frac{1}{|U|}$$.

Suppose $$n_i$$ is the number of elements in slot $$i$$, then the total number of collisions is:

$$
\begin{array}{rll}
\displaystyle \sum_{i=1}^{|B|} \frac{n_i (n_i - 1)}{2}
&=& \displaystyle \frac{1}{2}\sum_{i=1}^{|B|} n_i^2 - \frac{1}{2}\sum_{i=1}^{|B|} n_i \\
&\ge& \displaystyle \frac{1}{2}\sum_{i=1}^{|B|} \left (\frac{|U|}{|B|} \right )^2 - \frac{|U|}{2} \\
&=& \displaystyle \frac{{|U|}^2}{2{|B|}} - \frac{|U|}{2} \\
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \epsilon &\ge& \displaystyle \frac{\displaystyle \sum_{i=1}^{|B|} \frac{n_i (n_i - 1)}{2}}{\displaystyle \frac{|U|(|U|-1)}{2}} \\
&=& \displaystyle \frac{\displaystyle \frac{{|U|}^2}{|B|} - |U|}{|U|(|U|-1)} \\
&=& \displaystyle \frac{|U| - |B|}{|B|(|U| - 1)} \\
&=& \displaystyle \frac{|U|}{|B|(|U| - 1)} - \frac{1}{|U| - 1} \\
&\ge& \displaystyle \frac{|U|}{|B||U|} - \frac{1}{|U|} \\
&=& \displaystyle \frac{1}{|B|} - \frac{1}{|U|} \\
\end{array}
$$



