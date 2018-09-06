## 10.3 Implementing pointers and objects

### 10.3-1

> Draw a picture of the sequence $\langle 13; 4; 8; 19; 5; 11\rangle$ stored as a doubly linked list using the multiple-array representation. Do the same for the single-array representation.

$\dots$

### 10.3-2

> Write the procedures ALLOCATE-OBJECT and FREE-OBJECT for a homogeneous collection of objects implemented by the single-array representation.

$\dots$

### 10.3-3

> Why don’t we need to set or reset the prev attributes of objects in the implementation of the ALLOCATE-OBJECT and FREE-OBJECT procedures?

Because we do not need to know prev.

### 10.3-4

> It is often desirable to keep all elements of a doubly linked list compact in storage, using, for example, the first $m$ index locations in the multiple-array representation. (This is the case in a paged, virtual-memory computing environment.) Explain how to implement the procedures ALLOCATE-OBJECT and FREE-OBJECT so that the representation is compact. Assume that there are no pointers to elements of the linked list outside the list itself.

See 10.3-5.

### 10.3-5

> Let $L$ be a doubly linked list of length $n$ stored in arrays $key$, $prev$, and $next$ of length $m$. Suppose that these arrays are managed by ALLOCATE-OBJECT and FREE-OBJECT procedures that keep a doubly linked free list $F$. Suppose further that of the $m$ items, exactly $n$ are on list $L$ and $m - n$ are on the free list. Write a procedure COMPACTIFY-LIST$(L,F)$ that, given the list $L$ and the free list $F$, moves the items in $L$ so that they occupy array positions $1,2,\dots,n$ and adjusts the free list $F$ so that it remains correct, occupying array positions $n+1, n+2, \dots ,m$. The running time of your procedure should be $\Theta(n)$, and it should use only a constant amount of extra space. Argue that your procedure is correct.

For the $i$th element, if it is not in position $i$ and position $i$ is not free, we move the element at position $i$ to a new allocated position, and move the $i$th element to position $i$.
