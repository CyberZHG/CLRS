## Problems

### 18-1 Stacks on secondary storage

> Consider implementing a stack in a computer that has a relatively small amount of fast primary memory and a relatively large amount of slower disk storage. The operations PUSH and POP work on single-word values. The stack we wish to support can grow to be much larger than can fit in memory, and thus most of it must be stored on disk.

> A simple, but inefficient, stack implementation keeps the entire stack on disk. We maintain in-memory a stack pointer, which is the disk address of the top element on the stack. If the pointer has value $$p$$, the top element is the $$( p ~\text{mod}~ m )$$th word on page $$\lceil p / m \rceil$$ of the disk, where $$m$$ is the number of words per page.

> To implement the PUSH operation, we increment the stack pointer, read the appropriate page into memory from disk, copy the element to be pushed to the appropriate word on the page, and write the page back to disk. A POP operation is similar. We decrement the stack pointer, read in the appropriate page from disk, and return the top of the stack. We need not write back the page, since it was not modified.

> Because disk operations are relatively expensive, we count two costs for any implementation: the total number of disk accesses and the total CPU time. Any disk access to a page of $$m$$ words incurs charges of one disk access and $$\Theta(m)$$ CPU time.

> __*a*__. Asymptotically, what is the worst-case number of disk accesses for $$n$$ stack operations using this simple implementation? What is the CPU time for $$n$$ stack operations? (Express your answer in terms of $$m$$ and $$n$$ for this and subsequent parts.)

> Now consider a stack implementation in which we keep one page of the stack in memory. (We also maintain a small amount of memory to keep track of which page is currently in memory.) We can perform a stack operation only if the relevant disk page resides in memory. If necessary, we can write the page currently in memory to the disk and read in the new page from the disk to memory. If the relevant disk page is already in memory, then no disk accesses are required.

> __*b*__. What is the worst-case number of disk accesses required for $$n$$ PUSH operations? What is the CPU time?

> __*c*__. What is the worst-case number of disk accesses required for $$n$$ stack operations? What is the CPU time?

> Suppose that we now implement the stack by keeping two pages in memory (in addition to a small number of words for bookkeeping).

> __*d*__. Describe how to manage the stack pages so that the amortized number of disk accesses for any stack operation is $$O(1/m)$$ and the amortized CPU time for any stack operation is $$O(1)$$.