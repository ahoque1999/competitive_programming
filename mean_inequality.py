#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-11
Purpose: mean inequality 800
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """

    t_in: int
    a_in: List[str]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    a_in = []
    for _ in range(t_in):
        _ = input()
        a_in.append(input())

    return Args(t_in, a_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer  function """

        self.assertEqual(answer('1 2 3 4 5 6'), '1 3 2 5 4 6')
        self.assertEqual(answer('123 456 789 10'), '10 456 123 789')
        self.assertEqual(answer('6 9'), '6 9')


def answer(a_in: str):
    """ given a list of numbers rearrange so it is never surrounded
    by both something smaller and larger than it """

    lis = list(map(int, a_in.split()))
    lis.sort()
    n_in = len(lis)
    for ind in range(1, n_in-1, 2):
        lis[ind], lis[ind+1] = lis[ind+1], lis[ind]
    temp = list(map(str, lis))
    return ' '.join(temp)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for ind in range(args.t_in):
        print(answer(args.a_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
