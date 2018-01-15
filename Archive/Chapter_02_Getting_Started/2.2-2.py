import random
import unittest


def selection_sort(a):
    for i in range(len(a)):
        k = i
        for j in range(i + 1, len(a)):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]


class SelectionSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            selection_sort(arr)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
