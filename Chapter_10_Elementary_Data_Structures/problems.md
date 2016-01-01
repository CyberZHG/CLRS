## Problems

### 10-1 Comparisons among lists

> For each of the four types of lists in the following table, what is the asymptotic worst-case running time for each dynamic-set operation listed?

> | |unsorted, singly linked|sorted, singly linked|unsorted, doubly linked|sorted, doubly linked|
|:-:|:-:|:-:|:-:|:-:|
|SEARCH$$(L,k)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|
|INSERT$$(L,x)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|
|DELETE$$(L,x)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(1)$$|
|SUCCESSOR$$(L,x)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|PREDECESSOR$$(L,x)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|MINIMUM$$(L)$$|$$\Theta(n)$$|$$\Theta(1)$$|$$\Theta(n)$$|$$\Theta(1)$$|
|MAXIMUM$$(L)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|$$\Theta(n)$$|

