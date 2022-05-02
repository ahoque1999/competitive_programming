#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-01
Purpose: orac and models 1400
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """
    t_in: int
    n_in: List[int]
    s_in: List[List[int]]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    n_in = []
    s_in = []
    for _ in range(t_in):
        n_in.append(int(input()))
        s_in.append(list(map(int, input().split())))

    return Args(t_in=t_in, n_in=n_in, s_in=s_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer fucntion """

        n_ini = 6
        s_ini = [3, 6, 7, 7, 7, 7]
        self.assertEqual(answer(n_ini, s_ini), 3)
        n_ini = 7
        s_ini = [1, 4, 2, 3, 6, 4, 9]
        self.assertEqual(answer(n_ini, s_ini), 3)
        n_ini = 4
        s_ini = [5, 3, 4, 6]
        self.assertEqual(answer(n_ini, s_ini), 2)
        n_ini = 5
        s_ini = [5, 4, 3, 2, 1]
        self.assertEqual(answer(n_ini, s_ini), 1)
        n_ini = 1
        s_ini = [9]
        self.assertEqual(answer(n_ini, s_ini), 1)


def answer(n_ini: int, s_ini: List[int]):
    """ given a list of numbers find largest
    size of list obtained under conditions """

    maxi = [1] * n_ini

    for ind in range(n_ini, 1-1, -1):
        cand = [
            indp
            for indp in range(ind*2, n_ini+1, ind)
            if s_ini[indp-1] > s_ini[ind-1]
        ]
        if cand == []:
            continue
        maxi[ind-1] += max([maxi[indp-1] for indp in cand])

    return max(maxi)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for ind in range(args.t_in):
        print(answer(args.n_in[ind], args.s_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
