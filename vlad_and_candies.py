#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-08
Purpose: vlad and candies 800
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
        input()
        a_in.append(input())

    return Args(t_in, a_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer function """

        self.assertEqual(answer('2 3'), 'YES')
        self.assertEqual(answer('2'), 'NO')
        self.assertEqual(answer('1 6 2 4 3'), 'NO')
        self.assertEqual(answer('2 2 2 1'), 'YES')
        self.assertEqual(answer('1 1000000000 999999999'), 'YES')
        self.assertEqual(answer('1'), 'YES')
        self.assertEqual(answer('6 10 13 10 5 14 5 7 12 8 10'), 'YES')


def answer(str_1: str):
    """ given a list return if we second largest
    is less than 1 different """

    lis: List[int] = list(map(int, str_1.split()))
    nlis = len(lis)
    if nlis == 1:
        if lis[0] == 1:
            return "YES"
        return "NO"
    temp = sorted(lis, reverse=True)
    if temp[0] - temp[1] <= 1:
        return "YES"
    return "NO"


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for ind in range(args.t_in):
        print(answer(args.a_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
