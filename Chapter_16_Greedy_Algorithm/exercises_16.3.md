## 16.3 Huffman codes

### 16.3-1

> Explain why, in the proof of Lemma 16.2, if $x.freq = b.freq$, then we must have $a.freq = b.freq = x.freq = y.freq$.

### 16.3-2

> Prove that a binary tree that is not full cannot correspond to an optimal prefix code.

### 16.3-3

> What is an optimal Huffman code for the following set of frequencies, based on
the first 8 Fibonacci numbers? 

> a:1 b:1 c:2 d:3 e:5 f:8 g:13 h:21 

> Can you generalize your answer to find the optimal code when the frequencies are the first $n$ Fibonacci numbers?

* a: 1111111
* b: 1111110
* c: 111110
* d: 11110
* e: 1110
* f: 110
* g: 10
* h: 0

### 16.3-4

> Prove that we can also express the total cost of a tree for a code as the sum, over all internal nodes, of the combined frequencies of the two children of the node.

### 16.3-5

> Prove that if we order the characters in an alphabet so that their frequencies are monotonically decreasing, then there exists an optimal code whose codeword lengths are monotonically increasing.

### 16.3-6

> Suppose we have an optimal prefix code on a set $C = \\{0, 1, \dots, n - 1\\}$ of characters and we wish to transmit this code using as few bits as possible. Show how to represent any optimal prefix code on $C$ using only $2n - 1 + n \lceil lg n \rceil$ bits.

Use one bit for representing internal or leaf node, which is $2n - 1$ bits.

### 16.3-7

> Generalize Huffman’s algorithm to ternary codewords (i.e., codewords using the symbols 0, 1, and 2), and prove that it yields optimal ternary codes.

Merge three nodes.

### 16.3-8

> Suppose that a data file contains a sequence of 8-bit characters such that all 256 characters are about equally common: the maximum character frequency is less than twice the minimum character frequency. Prove that Huffman coding in this case is no more efficient than using an ordinary 8-bit fixed-length code.

Full binary tree, another 8-bit encoding.

### 16.3-9

> Show that no compression scheme can expect to compress a file of randomly chosen 8-bit characters by even a single bit.

$2^n >> 2^{n-1}$
