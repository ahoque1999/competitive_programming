#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-05
Purpose: division ? 800
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """
    t_in: int
    r_in: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    r_in = []
    for _ in range(t_in):
        r_in.append(int(input()))

    return Args(t_in, r_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test answer """

        self.assertEqual(answer(-789), "Division 4")
        self.assertEqual(answer(1299), "Division 4")
        self.assertEqual(answer(1300), "Division 4")
        self.assertEqual(answer(1399), "Division 4")
        self.assertEqual(answer(1400), "Division 3")
        self.assertEqual(answer(1679), "Division 2")
        self.assertEqual(answer(2300), "Division 1")


def answer(r_in: int) -> str:
    """ return division given rating """

    if r_in <= 1399:
        return "Division 4"
    if r_in <= 1599:
        return "Division 3"
    if r_in <= 1899:
        return "Division 2"
    return "Division 1"

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    t_in = args.t_in
    r_in = args.r_in
    for ind in range(t_in):
        print(answer(r_in[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
