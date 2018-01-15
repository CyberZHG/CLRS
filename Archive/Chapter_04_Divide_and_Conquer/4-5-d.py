import unittest
import random


class Chip:
    def __init__(self, state):
        self.state = state

    def check(self, other):
        if self.state:
            return other.state
        return random.randint(0, 1)


def check(chip_a, chip_b):
    return chip_a.check(chip_b) and chip_b.check(chip_a)


def choose_good_chip(chips):
    assert(len(chips) > 0)
    if len(chips) == 1:
        return chips[0]
    mid = len(chips) // 2
    next_chips = []
    for i in range(mid):
        if check(chips[i], chips[mid + i]):
            next_chips.append(chips[i])
    if len(chips) % 2 == 1 and len(next_chips) % 2 == 0:
        next_chips.append(chips[-1])
    return choose_good_chip(next_chips)


class ChooseChipTestCase(unittest.TestCase):
    def random_chips(self):
        n = random.randint(1, 1000)
        good_num = n // 2 + 1
        bad_num = n - good_num
        good_chips = [Chip(True) for _ in range(good_num)]
        bad_chips = [Chip(False) for _ in range(bad_num)]
        chips = good_chips + bad_chips
        random.shuffle(chips)
        return chips

    def test_random(self):
        for _ in range(10000):
            chips = self.random_chips()
            good_chip = choose_good_chip(chips)
            self.assertTrue(good_chip.state)


if __name__ == '__main__':
    unittest.main()
