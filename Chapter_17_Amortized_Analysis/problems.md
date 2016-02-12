## Problems

### 17-1 Bit-reversed binary counter

> Chapter 30 examines an important algorithm called the fast Fourier transform, or FFT. The first step of the FFT algorithm performs a __*bit-reversal permutation*__ on an input array $$A[0 \dots n-1]$$ whose length is $$n = 2^k$$ for some nonnegative integer $$k$$. This permutation swaps elements whose indices have binary representations that are the reverse of each other.

> We can express each index $$a$$ as a $$k$$-bit sequence $$\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle$$, where $$a = \sum_{i=0}^{k-1} a_i 2^i$$. We define

> $$\text{rev}_k(\langle a_{k-1}, a_{k-2}, \dots, a_0 \rangle) = \langle a_0, a_1, \dots, a_{k-1} \rangle$$;

> thus,

> $$\displaystyle \text{rev}_k(a) = \sum_{i=0}^{k-1} a_{k-i-1} 2^i$$.

> For example, if $$n = 16$$ (or, equivalently, $$k = 4$$), then $$\text{rev}_k(3) = 12$$, since the $$4$$-bit representation of $$3$$ is $$0011$$, which when reversed gives $$1100$$, the $$4$$-bit representation of $$12$$.

> __*a*__. Given a function $$\text{rev}_k$$ that runs in $$\Theta(k)$$ time, write an algorithm to perform the bit-reversal permutation on an array of length $$n = 2^k$$ in $$O(nk)$$ time.

```python
def rev_k(k, a):
    x = 0
    for _ in xrange(k):
        x <<= 1
        x += a & 1
        a >>= 1
    return x
```

