#!/usr/bin/python3
""" homecoming 1300 """

from unittest import TestCase
from typing import NamedTuple


class Args(NamedTuple):
    """ arguments """

    a_i: int
    b_i: int
    c_i: int
    str_i: str


def get_args() -> Args:
    """ get the input arguments """

    a_i, b_i, c_i = list(map(int, input().split()))
    s_i = input()

    return Args(a_i, b_i, c_i, s_i)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test returning smallest index """

        temp = Args(a_i=2, b_i=2, c_i=1, str_i='BB')
        self.assertEqual(answer(temp), 2)
        temp = Args(a_i=1, b_i=1, c_i=1, str_i='AB')
        self.assertEqual(answer(temp), 1)
        temp = Args(a_i=3, b_i=2, c_i=8, str_i='AABBBBAABB')
        self.assertEqual(answer(temp), 3)
        temp = Args(a_i=5, b_i=3, c_i=4, str_i='BBBBB')
        self.assertEqual(answer(temp), 1)
        temp = Args(a_i=2, b_i=1, c_i=1, str_i='ABABAB')
        self.assertEqual(answer(temp), 6)


def answer(inp: Args):
    """ given a string and costs, return the smallest
    index that corresponds to the cost that
    can cover the remaining string """

    # dict for price
    conv = {
        'A': inp.a_i,
        'B': inp.b_i
    }

    # make input easier to write
    str_i = inp.str_i
    n_str = len(str_i)

    # initialize cost
    if str_i[-1] == str_i[-2]:
        cost = conv[str_i[-1]]
    else:
        cost = 0

    # initialise previous char
    prev = str_i[-1]

    # iterate
    for ind in range(n_str-1, -1, -1):
        if cost > inp.c_i:
            break
        if prev != str_i[ind]:
            if cost+conv[str_i[ind]] <= inp.c_i:
                prev = str_i[ind]
                cost += conv[str_i[ind]]
            else:
                ind += 1
                break
    
    return ind + 1


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        args = get_args()
        print(answer(args))


if __name__ == '__main__':
    main()
