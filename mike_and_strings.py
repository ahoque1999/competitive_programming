#!/usr/bin/python3
""" mike and strings 1300 """

from unittest import TestCase
from typing import NamedTuple
from typing import List


class Args(NamedTuple):
    """ arguments """

    strngs: List[str]


def get_args() -> Args:
    """ get the input arguments """

    strngs = []
    for _ in range(int(input())):
        strngs.append(input())

    return Args(strngs)


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test the number of changes required given
        a list of strings """

        temp = [
            'xzzwo',
            'zwoxz',
            'zzwox',
            'xzzwo'
        ]
        self.assertEqual(answer(temp), 5)
        temp = [
            'molzv',
            'lzvmo'
        ]
        self.assertEqual(answer(temp), 2)
        temp = [
            'kc',
            'kc',
            'kc'
        ]
        self.assertEqual(answer(temp), 0)
        temp = [
            'aa',
            'aa',
            'ab'
        ]
        self.assertEqual(answer(temp), -1)

    def test_diff(self):
        """ test the number of changes required given
        two strings """

        self.assertEqual(diff('xzzwo', 'xzzwo'), 0)
        self.assertEqual(diff('xzzwo', 'zwoxz'), 3)
        self.assertEqual(diff('zwoxz', 'xzzwo'), 2)
        self.assertEqual(diff('xzzwo', 'zzwox'), 4)


def diff(str_1: str, str_2: str) -> int:
    """ return the number of differences given two strings """

    for ind in range(len(str_1)):
        if str_1 == str_2[ind:] + str_2[:ind]:
            return ind
    return -1


def answer(strngs: List[str]) -> int:
    """ return the number of changes required given
    a list of strings """

    mini = 50**50 + 1
    for str_j in strngs:
        curr = 0
        for str_i in strngs:
            change = diff(str_j, str_i)
            if change >= 0:
                curr += change
            else:
                return -1
        if curr < mini:
            mini = curr
    return mini


def main() -> None:
    """ do stuff """

    args = get_args()
    print(answer(args.strngs))


if __name__ == '__main__':
    main()
