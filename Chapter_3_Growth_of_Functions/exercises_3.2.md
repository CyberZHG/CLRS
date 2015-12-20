## Standard notations and common functions


### 3.2-1

> Show that if $$f(n)$$ and $$g(n)$$ are monotonically increasing functions, then so are the functions $$f(n) + g(n)$$ and $$f(g(n))$$, and if $$f(n)$$ and $$g(n)$$ are in addition nonnegative, then $$f(n) \cdot g(n)$$ is monotonically increasing.

* $$f(n) + g(n)$$

$$n \le m$$

$$f(n) \le f(m)$$ and $$g(n) \le g(m)$$

$$f(n) + g(n) \le f(m) + g(m)$$

* $$f(g(n))$$

$$n \le m$$

$$f(n) \le f(m)$$

$$g(f(n)) \le g(f(m))$$

* $$f(n) \cdot g(n)$$

$$n \le m$$

$$f(n) \le f(m)$$ and $$g(n) \le g(m)$$

$$f(n) \cdot g(n) \le f(m) \cdot g(m)$$

### 3.2-2

> Prove equation (3.16).
>
> $$a^{log_bc}=c^{log_ba}$$ (3.16)

$$a^{log_bc}=a^{\frac{log_ac}{log_ab}}=c^{\frac{1}{log_ab}}=c^{log_ba}$$

### 3.2-3

> Prove equation (3.19). Also prove that $$n! = \omega(2^n)$$ and $$n!=o(n^n)$$.
>
> $$\lg(n!)=\Theta(n \lg n)$$ (3.19)

* $$\lg(n!)=\Theta(n \lg n)$$

Use Stirling's approximation:

$$\lg(n!) = \lg(\sqrt{2 \pi n}\left (\frac{n}{e}\right )^n e^{\alpha n})$$ $$=\lg(\sqrt{2 \pi n}) + \lg(\left (\frac{n}{e}\right )^n) + \lg (e^{\alpha n})$$ $$=\Theta(\lg \sqrt{n}) + \Theta(n\lg n) + \Theta(n)$$ $$=\Theta(n\lg n)$$

* $$n! = \omega(2^n)$$

$$n!=n \cdot (n-1) \cdot \cdots \cdot 1 \ge 4 \cdot 2 \cdot \cdots \cdot 2 \cdot 1 = 2^n$$

* $$n!=o(n^n)$$

$$n!=n \cdot (n-1) \cdot \cdots \cdot 1 \le n \cdot n \cdot \cdots \cdot n = n^n$$

### 3.2-4 $$\ast$$

> Is the function $$\left \lceil \lg n \right \rceil!$$ polynomially bounded? Is the function $$\left \lceil \lg \lg n \right \rceil!$$ polynomially
bounded?

### 3.2-5 $$\ast$$

> Which is asymptotically larger: $$\lg (\lg^{\ast}n)$$ or $$\lg^{\ast}(\lg n)$$?

### 3.2-6

> Show that the golden ratio $$\phi$$ and its conjugate $$\hat{\phi}$$ both satisfy the equation $$x^2=x+1$$.

### 3.2-7

> Prove by induction that the $$i$$th Fibonacci number satisfies the equality
>
> $$
F_i=\frac{\phi^{i}-\hat{\phi^i}}{\sqrt{(5)}}
$$
>
> where $$\phi$$ is the golden ratio and $$\hat{\phi}$$ is its conjugate.

### 3.2-8

> Show that $$k \ln k = \Theta(n)$$ implies $$k = \Theta(n / \ln n)$$.

