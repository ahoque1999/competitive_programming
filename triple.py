#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-07
Purpose: triple 800
"""

from typing import NamedTuple, List, Dict
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """

    t_in: int
    a_in: List[List[int]]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    a_in = []
    for _ in range(t_in):
        input()
        a_in.append(list(map(int, input().split())))

    return Args(t_in, a_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer """

        self.assertEqual(answer([1]), -1)
        self.assertEqual(answer([2, 2, 2]), 2)
        self.assertEqual(answer([2, 2, 3, 4, 4, 2, 2]), 2)
        self.assertEqual(answer([1, 4, 3, 4, 3, 2, 4, 1]), 4)
        self.assertEqual(answer([1, 1, 1, 2, 2, 2, 3, 3, 3]), 1)
        self.assertEqual(answer([1, 5, 2, 4, 3]), -1)
        self.assertEqual(answer([4, 4, 4, 4]), 4)


def answer(lis: List[int]):
    """ print a number that appears at least 3 times """

    counts: Dict[int, int] = {}
    for ele in lis:
        counts[ele] = counts.get(ele, 0) + 1
        if counts[ele] == 3:
            return ele
    return -1


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    t_in = args.t_in
    a_in = args.a_in
    for ind in range(t_in):
        print(answer(a_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
