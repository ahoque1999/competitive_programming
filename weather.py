#!/usr/bin/python3
""" weather 1300 """

from unittest import TestCase
from typing import NamedTuple, List


class Args(NamedTuple):
    """ arguments """

    t_in: List[int]


def get_args() -> Args:
    """ get the input arguments """

    with open('input.txt', 'rt', encoding='utf-8') as ifh:
        next(ifh)
        for line in ifh:
            t_in = list(map(int, line.split()))

    return Args(t_in=t_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ check that minimum required
        number of changes returned """

        self.assertEqual(answer([-1, 1, -2, 1]), 1)
        self.assertEqual(answer([0, -1, 1, 2, -5]), 2)

    def test_nonpos(self):
        """ check that correct non
        positive list is returned"""

        self.assertEqual(nonpos([-1, 1, -2, 1]), [1, 1, 0])

    def test_nonneg(self):
        """ check that correct non
        positive list if returned """

        self.assertEqual(nonneg([-1, 1, -2, 1]), [0, 1, 1])


def nonneg(lis: List[int]) -> List[int]:
    """ return number of non negative numbers
    to the right of each boundary """

    n_lis = len(lis)
    ret = [0] * (n_lis-1)
    ret[0] = 1 if lis[0] >= 0 else 0
    for ind in range(1, n_lis-2+1, 1):
        ret[ind] = ret[ind-1] + (1 if lis[ind] >= 0 else 0)
    return ret


def nonpos(lis: List[int]) -> List[int]:
    """ return number of non positive numbers
    to the left of each boundary """

    n_lis = len(lis)
    ret = [0] * (n_lis-1)
    for ind in range(n_lis-1, 1-1, -1):
        try:
            ret[ind-1] = ret[ind] + (1 if lis[ind] <= 0 else 0)
        except IndexError:
            ret[ind-1] = 1 if lis[ind] <= 0 else 0
    return ret


def answer(lis: List[int]) -> int:
    """ return minimum required changes """

    n_bo = len(lis) - 1
    nonneg_ = nonneg(lis)
    nonpos_ = nonpos(lis)
    return min(
        [
            nonneg_[ind] + nonpos_[ind]
            for ind in range(n_bo)
        ]
    )


def main() -> None:
    """ do stuff """

    args = get_args()
    with open('output.txt', 'wt', encoding='utf-8') as ofh:
        ofh.write(str(answer(args.t_in)))


if __name__ == '__main__':
    main()
