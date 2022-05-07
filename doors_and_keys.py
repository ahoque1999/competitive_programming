#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-05-06
Purpose: doors and keys 800
"""

from typing import NamedTuple, List
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """
    
    t_in: int
    hall: List[str]

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    t_in = int(input())
    hall = []
    for _ in range(t_in):
        hall.append(input())

    return Args(t_in, hall)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test correct result returned given a hallway """

        self.assertEqual(answer('rgbBRG'), "YES")
        self.assertEqual(answer('RgbrBG'), "NO")
        self.assertEqual(answer('bBrRgG'), "YES")
        self.assertEqual(answer('rgRGBb'), "NO")


def answer(hall: str):
    """ given a hallway return whether the knight can pass """

    keys = []
    for ele in hall:
        if ele in ['r', 'g', 'b']:
            keys.append(ele)
            continue
        if ele.lower() not in keys:
            return "NO"
    return "YES"


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    t_in = args.t_in
    hall = args.hall

    for ind in range(t_in):
        print(answer(hall[ind]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
