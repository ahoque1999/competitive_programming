#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-04-30
Purpose: basketball exercise 1400
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """
    n_in: int
    l_in: List[int]
    r_in: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    n_in = int(input())
    l_in = list(map(int, input().split()))
    r_in = list(map(int, input().split()))

    return Args(n_in=n_in, l_in=l_in, r_in=r_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ check that maximum height is returned """

        test_args = Args(
            5,
            [9, 3, 5, 7, 3],
            [5, 8, 1, 4, 5]
        )
        self.assertEqual(answer(test_args), 29)
        test_args = Args(
            3,
            [1, 2, 9],
            [10, 1, 1]
        )
        self.assertEqual(answer(test_args), 19)
        test_args = Args(
            1,
            [7],
            [4]
        )
        self.assertEqual(answer(test_args), 7)


def answer(args: Args):
    """ return the maximum height """

    n_in = args.n_in
    l_in = args.l_in
    r_in = args.r_in

    ret = init(n_in)
    ret[0] = [l_in[0], r_in[0], 0]
    for ind in range(1, n_in):
        ret[ind][0] = l_in[ind] + max([ret[ind-1][1], ret[ind-1][2]])
        ret[ind][1] = r_in[ind] + max([ret[ind-1][0], ret[ind-1][2]])
        ret[ind][2] = max([ret[ind-1][0], ret[ind-1][1], ret[ind-1][2]])

    return max(ret[-1])


def init(n_in: int):
    """ initialize matrix """

    return [
        [0] * 3
        for _ in range(n_in)
    ]


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(answer(args))


# --------------------------------------------------
if __name__ == '__main__':
    main()
