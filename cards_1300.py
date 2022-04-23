#!/usr/bin/python3
""" cards cooking 1300 """

from unittest import TestCase
from typing import NamedTuple, List


class Args(NamedTuple):
    """ arguments """

    card: str


def get_args() -> Args:
    """ get the input arguments """

    _ = input()
    card = input()
    return Args(card=card)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test that the correct indices are returned
        given a k and n """

        self.assertEqual(answer('RGB'), ['R', 'G', 'B'])
        self.assertEqual(answer('RRRRR'), ['R'])
        self.assertEqual(answer('RG'), ['B'])
        self.assertEqual(answer('RRGG'), ['R', 'G', 'B'])
        self.assertEqual(answer('RGG'), ['B', 'R'])

    def test_vector(self):
        """ test a sorted list of counts from string is returned """

        self.assertEqual(vector('RGB'), [1, 1, 1])
        self.assertEqual(vector('RGBR'), [2, 1, 1])
    
    def test_count0s(self):
        """ test correct number of 0s returned """

        self.assertEqual(count0s([0, 1, 1]), 1)
        self.assertEqual(count0s([0, 0, 42]), 2)
    
    def test_other(self):
        """ test the other char is returned given 2 characters """

        self.assertEqual(other(['R', 'G']), 'B')

    def test_present(self):
        """ test the correct chars are returned from a vector """

        self.assertEqual(present([1, 1, 0]), ['R', 'G'])
        self.assertEqual(present([1, 42, 0]), ['R', 'G'])
        self.assertEqual(present([1, 42, 99]), ['R', 'G', 'B'])
        self.assertEqual(present([0, 42, 99]), ['G', 'B'])
        self.assertEqual(present([0, 0, 99]), ['B'])


def present(lis: List[int]) -> List[str]:
    """ return a list of characters present in the vector """

    conv = {
        0: 'R',
        1: 'G',
        2: 'B'
    }
    lis = [ind for ind, _ in enumerate(lis) if lis[ind] != 0] 
    return [conv[ele] for ele in lis]


def other(lis: List[str]) -> str:
    """ return the other character given two """

    if 'R' not in lis:
        return 'R'
    if 'G' not in lis:
        return 'G'
    if 'B' not in lis:
        return 'B'


def count0s(lis: List[int]) -> int:
    """ return number of 0s in list """

    return sum([1 for ele in lis if ele == 0])


def vector(str_1: str) -> List[int]:
    """ return a sorted list of counts from string """

    return [
        sum([1 for char in str_1 if char == 'R']),
        sum([1 for char in str_1 if char == 'G']),
        sum([1 for char in str_1 if char == 'B'])
    ]


def print_str(lis: List[int]) -> None:
    """ print a string given cahracters """

    for ele in lis:
        print(ele, end='')
    print()


def answer(card) -> List[str]:
    """ return list of possible final cards """

    vec = vector(card)
    zeroes = count0s(vec)
    if zeroes == 0:
        return ['R', 'G', 'B']
    lis =  present(vec)
    if zeroes == 2:
        return lis
    if zeroes == 1:
        vec = [2 if ele >=2 else ele for ele in vec]
        if sum(vec) == 2:
            return [other(lis)]
        if sum(vec) == 4:
            return ['R', 'G', 'B']
        if sum(vec) == 3:
            conv = {
                0: 'R',
                1: 'G',
                2: 'B'
            }
            return sorted([other(lis), conv[vec.index(1)]])


def main() -> None:
    """ do stuff """

    args = get_args()
    print_str(sorted(answer(args.card)))


if __name__ == '__main__':
    main()
