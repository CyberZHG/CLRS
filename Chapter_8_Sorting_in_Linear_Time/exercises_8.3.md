## 8.3 Radix sort

### 8.3-1

> Using Figure 8.3 as a model, illustrate the operation of RADIX-SORT on the following list of English words: COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.

| 0 |   1   |   2   |   3   |
|:-:|:-----:|:-----:|:-----:|
|COW|SE__A__|T__A__B|__B__AR|
|DOG|TE__A__|B__A__R|__B__IG|
|SEA|MO__B__|E__A__R|__B__OX|
|RUG|TA__B__|T__A__R|__C__OW|
|ROW|DO__G__|S__E__A|__D__IG|
|MOB|RU__G__|T__E__A|__D__OG|
|BOX|DI__G__|D__I__G|__E__AR|
|TAB|BI__G__|B__I__G|__F__OX|
|BAR|BA__R__|M__O__B|__M__OB|
|EAR|EA__R__|D__O__G|__N__OW|
|TAR|TA__R__|C__O__W|__R__OW|
|DIG|CO__W__|R__O__W|__R__UG|
|BIG|RO__W__|N__O__W|__S__EA|
|TEA|NO__W__|B__O__X|__T__AB|
|NOW|BO__X__|F__O__X|__T__AR|
|FOX|FO__X__|R__U__G|__T__EA|

### 8.3-2

> Which of the following sorting algorithms are stable: insertion sort, merge sort, heapsort, and quicksort? Give a simple scheme that makes any sorting algorithm stable. How much additional time and space does your scheme entail?

Stable: insertion sort, merge sort.

When two values are equals, compare the original index. Additional space: $$\Theta(n)$$


### 8.3-3

> Use induction to prove that radix sort works. Where does your proof need the assumption that the intermediate sort is stable?

$$\dots$$

### 8.3-4

> Show how to sort n integers in the range $$0$$ to $$n^3 - 1$$ in $$O(n)$$ time.

$$n$$-ary radix sort, including three $$O(n)$$ counting sort.

#### 8.3-5 $$\star$$

> In the first card-sorting algorithm in this section, exactly how many sorting passes are needed to sort $$d$$-digit decimal numbers in the worst case? How many piles of cards would an operator need to keep track of in the worst case?

$$\Theta(k^d)$$ passes.

$$\Theta(nk)$$ piles.
