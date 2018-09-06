## 11.3 Hash functions

### 11.3-1

> Suppose we wish to search a linked list of length $$n$$, where each element contains a key $$k$$ along with a hash value $$h(k)$$. Each key is a long character string. How might we take advantage of the hash values when searching the list for an element with a given key?

Compare the long character strings only when they have the same hash values.

### 11.3-2

> Suppose that we hash a string of $$r$$ characters into $$m$$ slots by treating it as a radix-128 number and then using the division method. We can easily represent the number $$m$$ as a 32-bit computer word, but the string of $$r$$ characters, treated as a radix-128 number, takes many words. How can we apply the division method to compute the hash value of the character string without using more than a constant number of words of storage outside the string itself?

We should calculate

$$\sum_{i=0}^{r-1} c_i \cdot 128^i \mod m$$

It cannot be calculated with a constant number of words of storage because the sum may exceed 2^32 - 1. However, Equation 31.18 suggests

$$
\begin{align*}
\sum_{i=0}^{r-1} c_i \cdot 128^i
 &\equiv \sum_{i=0}^{r-1} (c_i \cdot 128^i) \bmod m \pmod m \\
 &\equiv \sum_{i=0}^{r-1} (c_i \cdot 128^i \bmod m) \pmod m \\
 &\equiv \sum_{i=1}^{r-1} (c_i \cdot 128^i \bmod m) + c_1 \cdot 128 \bmod m+ c_0 \bmod m \pmod m \\
 &\equiv \sum_{i=1}^{r-1} ((c_i \cdot 128^{i-1} \bmod m) + c_1 \bmod m) \bmod m \cdot (128 \bmod m) \bmod m + c_0 \bmod m \pmod m \\
 &\equiv ... \\
 &\equiv (...(c_{r-1} \bmod m \cdot (128 \bmod m) \bmod m + c_{r-2} \bmod m) \bmod m \cdot ... \cdot (128 \bmod m) + c_1 \bmod m) \bmod m + c_0 \bmod m \pmod m
\end{align*}
$$

It can be calculated with a loop.

```
sum := 0
for i = 1 to r
    sum := ((sum % m) * (128 % m) % m + s[i] % m) % m
```

And it fits in a word now. Futhermore, we may apply Equation 31.18 again and get

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

Suppose $$|U|=n$$ and $$|B|=m$$

$$
\begin{array}{rll}
\displaystyle \sum_{i=1}^{m} \frac{n_i (n_i - 1)}{2}
&=& \displaystyle \frac{1}{2}\sum_{i=1}^{m} n_i^2 - \frac{1}{2}\sum_{i=1}^{m} n_i \\
&\ge& \displaystyle \frac{1}{2}\sum_{i=1}^{m} \left (\frac{n}{m} \right )^2 - \frac{n}{2} \\
&=& \displaystyle \frac{n^2}{2{m}} - \frac{n}{2} \\
\end{array}
$$

$$
\begin{array}{rll}
\displaystyle \epsilon &\ge& \displaystyle \frac{\displaystyle \sum_{i=1}^{m} \frac{n_i (n_i - 1)}{2}}{\displaystyle \frac{n(n-1)}{2}} \\
&=& \displaystyle \frac{\displaystyle \frac{n^2}{m} - n}{n(n-1)} \\
&=& \displaystyle \frac{n - m}{m(n - 1)} \\
&=& \displaystyle \frac{n}{m(n - 1)} - \frac{1}{n - 1} \\
&\ge& \displaystyle \frac{n}{mn} - \frac{1}{n} \\
&=& \displaystyle \frac{1}{m} - \frac{1}{n} \\
\end{array}
$$

Therefore $$\displaystyle \epsilon \ge \frac{1}{|B|} - \frac{1}{|U|}$$.

### 11.3-6 $$\star$$

> Let $$U$$ be the set of $$n$$-tuples of values drawn from $$\mathbb{Z}_p$$, and let $$B=\mathbb{Z}_p$$, where $$p$$ is prime. Define the hash function $$h_b$$: $$U \rightarrow B$$ for $$b \in \mathbb{Z}_p$$ on an input $$n$$-tuple $$\langle a_0, a_1, \dots, a_{n-1} \rangle$$ from $$U$$ as

> $$\displaystyle h_b(\langle a_0, a_1, \dots, a_{n-1} \rangle)=\left ( \sum_{j=0}^{n-1}a_jb^j \right ) ~\text{mod}~p$$,

> and let $$\mathcal{H}=\{ h_b : b \in \mathbb{Z}_p \}$$. Argue that $$\mathcal{H}$$ is $$((n-1)/p)$$-universal according to the definition of $$\epsilon$$-universal in Exercise 11.3-5.

$$\dots$$
