## 11.1 Direct-address tables

### 11.1-1

> Suppose that a dynamic set $$S$$ is represented by a direct-address table $$T$$ of length $$m$$. Describe a procedure that finds the maximum element of $$S$$. What is the worst-case performance of your procedure?

Traverse the table, $$O(m)$$.


### 11.1-2

> A __*bit vector*__ is simply an array of bits (0s and 1s). A bit vector of length $$m$$ takes much less space than an array of $$m$$ pointers. Describe how to use a bit vector to represent a dynamic set of distinct elements with no satellite data. Dictionary operations should run in $$O(1)$$ time.

Set the corresponding bit to 0 or 1.

### 11.1-3

> Suggest how to implement a direct-address table in which the keys of stored elements do not need to be distinct and the elements can have satellite data. All three dictionary operations (INSERT, DELETE, and SEARCH) should run in $$O(1)$$ time. (Don't forget that DELETE takes as an argument a pointer to an object to be deleted, not a key.)

Each key contains a linked list.

### 11.1-4 $$\star$$

> We wish to implement a dictionary by using direct addressing on a huge array. At the start, the array entries may contain garbage, and initializing the entire array is impractical because of its size. Describe a scheme for implementing a direct-address dictionary on a huge array. Each stored object should use $$O(1)$$ space; the operations SEARCH, INSERT, and DELETE should take $$O(1)$$ time each; and initializing the data structure should take $$O(1)$$ time. 

Use an additional array, treated somewhat like a stack whose size is the number of keys actually stored in the dictionary. When INSERT, the value in the huge array is set to the top index of the additional array, and the additional array records the corresponding index in the huge array (and the satellite data). When DELETE, set the value in the huge array to -1.

```python
class Item:
    def __init__(self):
        self.key = id(self) // 64 % 10007
        self.value = id(self)


huge_array = [random.randint(0, 10000) for _ in range(10007)]
additional_array = []


def insert(x):
    global huge_array
    global additional_array
    huge_array[x.key] = len(additional_array)
    additional_array.append((x.key, x))


def delete(x):
    global huge_array
    huge_array[x.key] = -1


def search(k):
    global huge_array
    global additional_array
    idx = huge_array[k]
    if 0 <= idx < len(additional_array):
        if additional_array[idx][0] == k:
            return additional_array[idx][1]
    return None
```
