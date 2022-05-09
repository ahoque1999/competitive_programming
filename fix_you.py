#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-09
Purpose: fix you 800
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """

    t_in: int
    a_in: List[List[str]]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    a_in = []
    for _ in range(t_in):
        n_in, ___ = list(map(int, input().split()))
        temp = []
        for __ in range(n_in):
            temp.append(input())
        a_in.append(temp)

    return Args(t_in, a_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer function """

        a_in = [
            'RRD',
            'DDR',
            'RRC'
        ]
        self.assertEqual(answer(a_in), 1)
        a_in = [
            'DDDC',
        ]
        self.assertEqual(answer(a_in), 3)
        a_in = [
            'RDDDDDRRR',
            'RRDDRRDDD',
            'RRDRDRRDR',
            'DDDDRDDRR',
            'DRRDRDDDR',
            'DDRDRRDDC',
        ]
        self.assertEqual(answer(a_in), 9)
        a_in = [
            'C'
        ]
        self.assertEqual(answer(a_in), 0)


def answer(lis: List[str]):
    """ return the number of differences
    in the last col and last row """

    n_row = len(lis)
    n_col = len(lis[0])
    las_row = [
        1
        for ele in lis[-1]
        if ele not in ['R', 'C']
    ]
    las_col = [
        1
        for row in range(n_row)
        if lis[row][n_col-1] not in ['D', 'C']
    ]
    return sum(las_col) + sum(las_row)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for ind in range(args.t_in):
        print(answer(args.a_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
