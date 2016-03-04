## 21.1 Disjoint-set operations

### 21.1-1

> Suppose that CONNECTED-COMPONENTS is run on the undirected graph $$G = (V, E)$$, where $$V = \{a, b, c, d, e, f, g, h, i, j, k\}$$ and the edges of $$E$$ are processed in the order $$(d, i), (f, k), (g, i), (b, g), (a, h), (i, j), (d, k), (b, j), (d, f), (g, j), (a, e)$$. List the vertices in each connected component after each iteration of lines 3–5.

| Edge processed | Collection of disjoint sets |
|:--------------:|:---------------------------:|
|  initial sets  | {$$a$$} {$$b$$} {$$c$$} {$$d$$} {$$e$$} {$$f$$} {$$g$$} {$$h$$} {$$i$$} {$$j$$} {$$k$$} |
| $$(d, i)$$ | {$$a$$} {$$b$$} {$$c$$} {$$d, i$$} {$$e$$} {$$f$$} {$$g$$} {$$h$$} {$$j$$} {$$k$$} |
| $$(f, k)$$ | {$$a$$} {$$b$$} {$$c$$} {$$d, i$$} {$$e$$} {$$f, k$$} {$$g$$} {$$h$$} {$$j$$} |
| $$(g, i)$$ | {$$a$$} {$$b$$} {$$c$$} {$$d, i$$} {$$e$$} {$$f, k$$} {$$g$$} {$$h$$} {$$j$$} |
| $$(b, g)$$ | {$$a$$} {$$b, g$$} {$$c$$} {$$d, i$$} {$$e$$} {$$f, k$$} {$$h$$} {$$j$$} |
| $$(a, h)$$ | {$$a, h$$} {$$b, g$$} {$$c$$} {$$d, i$$} {$$e$$} {$$f, k$$} {$$j$$} |
| $$(i, j)$$ | {$$a, h$$} {$$b, g$$} {$$c$$} {$$d, i, j$$} {$$e$$} {$$f, k$$} |
| $$(d, k)$$ | {$$a, h$$} {$$b, g$$} {$$c$$} {$$d, f, i, j, k$$} {$$e$$} |
| $$(b, j)$$ | {$$a, h$$} {$$b, d, f, g, i, j, k$$} {$$c$$} {$$e$$} |
| $$(d, f)$$ | {$$a, h$$} {$$b, d, f, g, i, j, k$$} {$$c$$} {$$e$$} |
| $$(g, j)$$ | {$$a, h$$} {$$b, d, f, g, i, j, k$$} {$$c$$} {$$e$$} |
| $$(a, e)$$ | {$$a, e, h$$} {$$b, d, f, g, i, j, k$$} {$$c$$} |

### 21.1-2

> Show that after all edges are processed by CONNECTED-COMPONENTS, two vertices are in the same connected component if and only if they are in the same set.

$$\dots$$

### 21.1-3

> During the execution of CONNECTED-COMPONENTS on an undirected graph $$G = (V, E)$$ with $$k$$ connected components, how many times is FIND-SET called? How many times is UNION called? Express your answers in terms of $$|V|$$, $$|E|$$, and $$k$$.

FIND-SET: $$2|E|$$.

UNION: Initially, there are $$|V|$$ components, and each UNION operation decreases the number of connected components by 1, thus UNION is called $$|V| - k$$ times.
