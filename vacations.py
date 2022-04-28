#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-04-27
Purpose: vacations 1400
"""

from typing import NamedTuple, List
from unittest import TestCase

# from utilities import split_s, count0s


def split_s(str_1: str):
    """ split a string into a list of contiguous strings """

    n_str = len(str_1)

    temp = str_1[0]
    lis = []
    for ind in range(1, n_str):
        if str_1[ind] != str_1[ind-1]:
            lis.append(temp)
            temp = str_1[ind]
        else:
            temp += str_1[ind]
    lis.append(temp)

    return lis


def count0s(lis: List[int]) -> int:
    """ return number of 0s in list """

    return sum([1 for ele in lis if ele == 0])


class Args(NamedTuple):
    """ Command-line arguments """
    n_in: int
    a_in: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    n_in = int(input())
    a_in = list(map(int, input().split()))

    return Args(n_in=n_in, a_in=a_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test actualy conversion of string """

        test = Args(4, [1, 3, 2, 0])
        # self.assertEqual(test, 2)
    
    def test_init(self):
        """ test matrix is initialized correctly """

        self.assertEqual(init(3), [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

def init(n_in: int):
    """ initialize matrix """

    return [
        [0] * 3
        for _ in range(n_in+1)
    ]

def answer(args: Args) -> int:
    """ return the minimum number of rest days """

    n_in = args.n_in
    a_in = args.a_in
    ret = init(n_in)
    for ind in range(1, n_in+1):
        if a_in[ind-1] == 0:
            ret[ind][0] = min(ret[ind-1]) + 1
            ret[ind][1] = ret[ind-1][1] + 1
            ret[ind][2] = ret[ind-1][2] + 1
            continue
        if a_in[ind-1] == 1:
            ret[ind][0] = min(ret[ind-1]) + 1
            ret[ind][1] = min([ret[ind-1][0], ret[ind-1][2]])
            ret[ind][2] = ret[ind-1][2] + 1
        if a_in[ind-1] == 2:
            ret[ind][0] = min(ret[ind-1]) + 1
            ret[ind][2] = min([ret[ind-1][0], ret[ind-1][1]])
            ret[ind][1] = ret[ind-1][1] + 1
        if a_in[ind-1] == 3:
            ret[ind][0] = min(ret[ind-1]) + 1
            ret[ind][1] = min([ret[ind-1][0], ret[ind-1][2]])
            ret[ind][2] = min([ret[ind-1][0], ret[ind-1][1]])
    return min(ret[-1])


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(answer(args))


# --------------------------------------------------
if __name__ == '__main__':
    main()
