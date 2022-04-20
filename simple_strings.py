#!/usr/bin/python3
""" mike and strings 1300 """

from unittest import TestCase
from typing import NamedTuple


class Args(NamedTuple):
    """ arguments """

    str_1: str


def get_args() -> Args:
    """ get the input arguments """

    return Args(input())


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test simple string made """

        self.assertEqual(answer('aab'), 'acb')
        self.assertEqual(answer('caaab'), 'cadab')
        self.assertEqual(answer('zscoder'), 'zscoder')
        self.assertEqual(answer('baa'), 'bac')
        self.assertEqual(answer('ttaapttappa'), 'tcacptcapca')

    def test_split_s(self):
        """ test string split correctly """

        self.assertEqual(split_s('caaab'), ['c', 'aaa', 'b'])
    
    def test_unique(self):
        """ test that a unique char is returned """

        self.assertEqual(unique('c', 'aaa', 'b'), 'd')
        self.assertEqual(unique('a', 'aaa', 'b'), 'c')
        self.assertEqual(unique('c', 'b', 'c'), 'a')

    def test_convert(self):
        """ test that the string is converted correctly """

        self.assertEqual(convert('aa', 'b'), 'ab')
        self.assertEqual(convert('aaa', 'b'), 'aba')
        self.assertEqual(convert('aaaa', 'b'), 'abab')


def convert(str_1, char_1):
    """ convert a unit string to a simple string """

    n_str = len(str_1)
    temp = [char for char in str_1]
    for ind in range(1, n_str, 2):
        temp[ind] = char_1

    return ''.join(temp)


def unique(str_1, str_2, str_3):
    """ return a character not in any of the three strings """

    if not str_1:
        str_1 = 'A'
    if not str_2:
        str_2 = 'A'
    if not str_3:
        str_3 = 'A'

    if (
        'c' != str_1[0] and
        'c' != str_2[0] and
        'c' != str_3[0]
    ):
        return 'c'

    if (
        'b' != str_1[0] and
        'b' != str_2[0] and
        'b' != str_3[0]
    ):
        return 'b'

    if (
        'a' != str_1[0] and
        'a' != str_2[0] and
        'a' != str_3[0]
    ):
        return 'a'

    return 'd'


def split_s(str_1: str):
    """ split a string into a list of contiguous strings """

    n_str = len(str_1)
    
    temp = str_1[0]
    lis = []
    for ind in range(1, n_str):
        if str_1[ind] != str_1[ind-1]:
            lis.append(temp)
            temp = str_1[ind]
        else:
            temp += str_1[ind]
    lis.append(temp)

    return lis


def answer(str_1: str) -> str:
    """ return a simple string with minimum
    changes given a string """

    lis = split_s(str_1)
    n_lis  = len(lis)
    for ind in range(n_lis):
        if len(lis[ind]) > 1:
            try:
                lis[ind] = convert(lis[ind], unique(lis[ind-1], lis[ind], lis[ind+1]))
            except IndexError:
                try:
                    lis[ind] = convert(lis[ind], unique('', lis[ind], lis[ind+1]))
                except IndexError:
                    lis[ind] = convert(lis[ind], unique(lis[ind-1], lis[ind], ''))

    return ''.join(lis)


def main() -> None:
    """ do stuff """

    args = get_args()
    print(answer(args.str_1))


if __name__ == '__main__':
    main()
