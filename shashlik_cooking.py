#!/usr/bin/python3
""" shashlik cooking 1300 """

from unittest import TestCase
from typing import NamedTuple, List


class Args(NamedTuple):
    """ arguments """

    n_in: int
    k_in: int


def get_args() -> Args:
    """ get the input arguments """

    n_in, k_in = list(map(int, input().split()))
    return Args(n_in=n_in, k_in=k_in)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test that the correct indices are returned
        given a k and n """

        self.assertEqual(answer(7, 2), [1, 6])


def print_list(lis: List[int]) -> None:
    """ print a list aesthetically """

    for ele in lis:
        print(ele, end=' ')
    print()


def answer(n_in, k_in):
    """ calculate the indices given a k and n """

    k2p1 = 2 * k_in + 1
    kp1 = k_in + 1

    rem = n_in % k2p1
    if rem == 0:
        rem = k2p1

    if rem <= kp1:
        return list(range(1, n_in+1, k2p1))
    else:
        return list(range(1+rem-(k_in+1), n_in+1, k2p1))


def main() -> None:
    """ do stuff """

    args = get_args()
    lis = answer(args.n_in, args.k_in)
    print(len(lis))
    print_list(lis)


if __name__ == '__main__':
    main()
