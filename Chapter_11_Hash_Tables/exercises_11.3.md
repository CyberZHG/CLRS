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

