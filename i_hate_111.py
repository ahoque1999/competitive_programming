#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-04-29
Purpose: i hate 111 1400
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """

    n_in: int
    x_in: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    n_in = int(input())
    x_in = [
        int(input())
        for _ in range(n_in)
    ]

    return Args(n_in=n_in, x_in=x_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer function """

        self.assertEqual(answer(121), 'YES')
        self.assertEqual(answer(122), 'YES')
        self.assertEqual(answer(123), 'NO')
        self.assertEqual(answer(444), 'YES')


def answer(int1: int) -> str:
    """ check if number can be represented by 11, 111 ..."""

    if int1 % 11 == 0:
        return "YES"
    if int1 % 111 == 0:
        return "YES"
    if int1 > 110 * (int1 % 11):
        return "YES"
    return "NO"


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    n_in = args.n_in
    x_in = args.x_in
    for ind in range(n_in):
        print(answer(x_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
