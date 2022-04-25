#!/usr/bin/python3
""" bear and compression 1300 """

from unittest import TestCase
from typing import NamedTuple, List, Tuple


class Args(NamedTuple):
    """ arguments """

    n_in: int
    lis: List[Tuple[str, str]]


def get_args() -> Args:
    """ get the input arguments """

    n_in, q_in = list(map(int, input().split()))
    temp = []
    for _ in range(q_in):
        (a_in, b_in) = input().split()
        temp.append((a_in, b_in))

    return Args(n_in=n_in, lis=temp)


class Test(TestCase):
    """ test cases """

    def test_bdict(self):
        """ test a dictionary is built correctly from
        a list of tuples and returned """

        temp_inp = [
            ('ab', 'a'),
            ('cc', 'c')
        ]
        temp_exp = {
            'a': ['a'],
            'c': ['c']
        }
        self.assertEqual(bdict(temp_inp), temp_exp)

    def test_answer(self):
        """ test that the correct number of elements
        returned at a depth of n """

        temp_lis = [
            ('ab', 'a'),
            ('cc', 'c'),
            ('ca', 'a'),
            ('ee', 'c'),
            ('ff', 'd'),
        ]
        self.assertEqual(answer(3, temp_lis), 4)


def bdict(lis: List[Tuple[str, str]]):
    """ given a list of tuples return a dictionary that links
    them correctly, the second element in the tuple is the key
    and the first char in the first element in appended into
    a list which the value """

    ret = {}
    for ele in lis:
        if ele[1] not in ret:
            ret[ele[1]] = [ele[0][0]]
        else:
            ret[ele[1]].append(ele[0][0])

    return ret


def answer(n_in: int, lis: List[Tuple[str, str]]) -> int:
    """ return number of elements in depth n by building
    a tree using the dictionary provided """

    dic = bdict(lis)
    ret = ['a']
    for _ in range(1, n_in):
        temp = []
        for ele in ret:
            if ele not in dic:
                continue
            temp += dic[ele]
        ret = temp

    return len(ret)


def main() -> None:
    """ do stuff """

    args = get_args()
    print(answer(args.n_in, args.lis))


if __name__ == '__main__':
    main()
