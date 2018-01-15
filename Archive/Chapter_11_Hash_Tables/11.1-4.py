import random
import unittest


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


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        item = Item()
        huge_array[item.key] = 0
        self.assertEqual(search(item.key), None)
        insert(item)
        self.assertEqual(search(item.key), item)
        delete(item)
        self.assertEqual(search(item.key), None)


if __name__ == '__main__':
    unittest.main()
