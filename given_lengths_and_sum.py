#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-04-26
Purpose: given lengths and sum of digits 1400
"""


from typing import NamedTuple
from unittest import TestCase


class Args(NamedTuple):
    """ Command-line arguments """

    n_in: int
    m_in: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    n_in, m_in = list(map(int, input().split()))

    return Args(n_in=n_in, m_in=m_in)


class Test(TestCase):
    """ test cases """

    def test_gfdismall(self):
        """ test the correct number is returned for
        the first digit given an n and an m"""

        self.assertEqual(gfdismall(2, 15), 6)

    def test_gfdilarge(self):
        """ test the correct number is returned for
        the first digit given an n and an m"""

        self.assertEqual(gfdilarge(2, 15), 9)

    def test_gsmall(self):
        """ return the smallest number given n and m
        where n is the number of digits and m is the
        sum of the digits """

        self.assertEqual(gsmall(2, 15), '69')
        self.assertEqual(gsmall(3, 0), '-1')
        self.assertEqual(gsmall(3, 1), '100')
        self.assertEqual(gsmall(1, 900), '-1')

    def test_glarge(self):
        """ return the largest number given the number
        of digits and sum of said digits """

        self.assertEqual(glarge(2, 15), '96')
        self.assertEqual(glarge(3, 0), '-1')
        self.assertEqual(glarge(3, 1), '100')
        self.assertEqual(glarge(3, 10), '910')

    def test_answer(self):
        """ test answer """

        self.assertEqual(answer(2, 15), '69 96')
        self.assertEqual(answer(3, 0), '-1 -1')
        self.assertEqual(answer(3, 10), '109 910')
        self.assertEqual(answer(1, 900), '-1 -1')
        self.assertEqual(answer(1, 0), '0 0')


def glarge(n_in: int, m_in: int):
    """ return the largest number given the number
    of digits and sum of said digits """

    if n_in == 1 and m_in == 0:
        return '0'
    if m_in == 0:
        return '-1'
    if gsmall(n_in, m_in) == '-1':
        return '-1'
    ret = [0] * n_in
    ret[0] = gfdilarge(n_in, m_in)
    m_in -= ret[0]
    for ind in range(1, n_in, 1):
        if m_in >= 9:
            ret[ind] = 9
            m_in -= 9
        elif m_in == 0:
            ret[ind] = 0
        else:
            ret[ind] = m_in
            m_in = 0
    return ''.join(map(str, ret))


def gsmall(n_in: int, m_in: int):
    """ get the smallest number given the number of
    digits and the sum of said digits """

    if n_in == 1 and m_in == 0:
        return '0'
    if m_in == 0:
        return '-1'
    fir = gfdismall(n_in, m_in)
    if fir > 9:
        return '-1'
    ret = [0] * n_in
    ret[0] = fir
    m_in -= ret[0]
    for ind in range(n_in-1, 1-1, -1):
        if m_in >= 9:
            ret[ind] = 9
            m_in -= 9
        elif m_in == 0:
            ret[ind] = 0
        else:
            ret[ind] = m_in
            m_in = 0
    return ''.join(map(str, ret))


def gfdismall(n_in: int, m_in: int):
    """ return the first digit for the smallest number """

    return max([1, m_in-(n_in-1)*9])


# to do
def gfdilarge(_: int, m_in: int):
    """ return the first digit for the smallest number """

    return min([9, m_in])


def answer(n_in: int, m_in: int):
    """ return the smallest and largest number
    given the number of digits and sum of said
    digits """

    return f'{gsmall(n_in, m_in)} {glarge(n_in, m_in)}'


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(answer(args.n_in, args.m_in))


# --------------------------------------------------
if __name__ == '__main__':
    main()
