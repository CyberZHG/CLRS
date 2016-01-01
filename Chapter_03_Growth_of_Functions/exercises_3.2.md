## 3.2 Standard notations and common functions


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

### 3.2-4 $$\star$$

> Is the function $$\left \lceil \lg n \right \rceil!$$ polynomially bounded? Is the function $$\left \lceil \lg \lg n \right \rceil!$$ polynomially bounded?

* $$\left \lceil \lg n \right \rceil!$$

$$\left \lceil \lg n \right \rceil!$$ $$= \sqrt{2 \pi \lg n}\left (\frac{\lg n}{e}\right )^{\lg n} e^{\alpha \lg n}$$ $$= \Theta((\lg n)^{\lg n})$$

$$\lg \left \lceil \lg n \right \rceil!$$ $$= \Theta(\lg n \lg \lg n)$$

$$\lg n^p$$ $$=\Theta(\lg n)$$

$$\Theta(\lg n \lg \lg n) > \Theta(\lg n)$$

$$\therefore$$ not bounded.

* $$\left \lceil \lg \lg n \right \rceil!$$

$$\left \lceil \lg \lg n \right \rceil!$$ $$= \Theta((\lg\lg n)^{\lg \lg n})$$

$$\lg \left \lceil \lg \lg n \right \rceil!$$ $$= \Theta(\lg \lg n \lg \lg \lg n)$$ $$=o(\lg^2\lg n)$$

$$\because$$ $$\lg^bn=o(n^a)$$

$$\therefore$$ $$o(\lg^2\lg n)$$ $$=o(\lg n)$$, is polynomially bounded.


### 3.2-5 $$\star$$

> Which is asymptotically larger: $$\lg (\lg^{\ast}n)$$ or $$\lg^{\ast}(\lg n)$$?

$$\lg (\lg^{\ast} (2^m))$$ and $$\lg^{\ast}(\lg (2^m))$$

$$\lg (1 + \lg^{\ast}m)$$ and $$\lg^{\ast}m$$

$$\because$$ $$\lg (x)$$ < $$x$$

$$\therefore$$ The right hand side is larger.

### 3.2-6

> Show that the golden ratio $$\phi$$ and its conjugate $$\hat{\phi}$$ both satisfy the equation $$x^2=x+1$$.

$$\phi = \frac{1 + \sqrt{5}}{2}$$

$$\phi^2=\frac{6+2\sqrt{5}}{4}=\frac{1 + \sqrt{5}}{2} + 1 = \phi + 1$$

$$\hat{\phi} = \frac{1 - \sqrt{5}}{2}$$

$$\hat{\phi}^2=\frac{6-2\sqrt{5}}{4}=\frac{1 - \sqrt{5}}{2} + 1 = \hat{\phi} + 1$$

### 3.2-7

> Prove by induction that the $$i$$th Fibonacci number satisfies the equality
>
> $$
F_i=\frac{\phi^{i}-\hat{\phi^i}}{\sqrt{5}}
$$
>
> where $$\phi$$ is the golden ratio and $$\hat{\phi}$$ is its conjugate.

$$F_0=0$$, $$\frac{\phi^{0}-\hat{\phi^0}}{\sqrt{5}}=0$$

$$F_1=1$$, $$\frac{\phi-\hat{\phi}}{\sqrt{5}}=1$$

Suppose $$F_{i-2}=\frac{\phi^{i-2}-\hat{\phi^{i-2}}}{\sqrt{5}}$$ and $$F_{i-1}=\frac{\phi^{i-1}-\hat{\phi^{i-1}}}{\sqrt{5}}$$,

$$F_i=F_{i-2}+F_{i-1}=\frac{1}{\sqrt{5}}(\phi^{i-2}-\hat{\phi^{i-2}} + \phi^{i-1}-\hat{\phi^{i-1}})$$

Based on the previous exercise,

$$\phi^{i-2} + \phi^{i-1} = \phi^{i-2}(1+\phi) = \phi^{i-2}\phi^2 = \phi ^ i$$

$$\therefore$$ $$F_i=\frac{\phi^{i}-\hat{\phi^i}}{\sqrt{5}}$$


### 3.2-8

> Show that $$k \ln k = \Theta(n)$$ implies $$k = \Theta(n / \ln n)$$.

$$c_1n \le k \ln k \le c_2n$$

$$\ln (c_1n) \le \ln(k \ln k) \le \ln (c_2n)$$

$$\ln c_1 + \ln n \le \ln k + \ln \ln k \le \ln c_2 + \ln n$$

$$\because$$ $$\ln k + \ln \ln k \le 2\ln k \ge \ln c_1 + \ln n$$

$$\therefore$$ $$\frac{\ln k}{\ln n} \ge \frac{1}{2}$$

$$\because$$ $$\ln k + \ln \ln k \ge \ln k \le \ln c_2 + \ln n$$

$$\therefore$$ $$\frac{\ln k}{\ln n} \le 1$$

$$\because$$ $$c_1n \le k \ln k \le c_2n$$

$$\therefore$$ $$\frac{c_1 n}{\ln n} \le \frac{k \ln k}{\ln n} \le \frac{c_2 n}{\ln n}$$

$$\therefore$$ $$\frac{c_1 n}{\ln n} \le \frac{k \ln k}{\ln n} \le k$$ and $$\frac{c_2 n}{\ln n} \ge \frac{k \ln k}{\ln n} \ge \frac{1}{2}k$$

$$\therefore$$ $$c_1\frac{n}{\ln n} \le k \le (2c_2)\frac{n}{\ln n}$$

$$\therefore$$ $$k = \Theta(n / \ln n)$$
