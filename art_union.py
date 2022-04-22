#!/usr/bin/python3
""" art union 1300 """

from unittest import TestCase
from typing import NamedTuple, List


class Matrix():
    """ matrix class """

    rows = 0
    cols = 0
    eles = []

    def __init__(self, rows, cols, eles) -> None:
        """ constructor for matrix """
        self.rows = rows
        self.cols = cols
        self.eles = eles

    def process(self) -> None:
        """ add the element above or to the left
        whichever is larger """

        for indr in range(1, self.rows):
            self.eles[indr][0] += self.eles[indr-1][0]

        for indc in range(1, self.cols):
            self.eles[0][indc] += self.eles[0][indc-1]

        for indr in range(1, self.rows):
            for indc in range(1, self.cols):
                self.eles[indr][indc] += max(
                    [
                        self.eles[indr-1][indc],
                        self.eles[indr][indc-1]
                    ]
                )

    def last(self) -> List[int]:
        """ return the last column """

        return [self.eles[indr][-1] for indr in range(self.rows)]


class Args(NamedTuple):
    """ arguments """

    mat: Matrix


def get_args() -> Args:
    """ get the input arguments """

    rows, cols = list(map(int, input().split()))
    eles = []
    for _ in range(rows):
        eles.append(list(map(int, input().split())))
    return Args(mat=Matrix(rows, cols, eles))


class Test(TestCase):
    """ test cases """

    def test_process(self):
        """ test matrix method adding the element above or
        to the left whichever is larger """

        test = Matrix(5, 1, [[1], [2], [3], [4], [1]])
        test.process()
        self.assertEqual(test.eles, [[1], [3], [6], [10], [11]])

    def test_last(self):
        """ test that the last column is returned """

        test = Matrix(5, 1, [[1], [2], [3], [4], [1]])
        self.assertEqual(test.last(), [1, 2, 3, 4, 1])
    
    def test_answer(self):
        """ test amswer """

        test = Matrix(5, 1, [[1], [2], [3], [4], [5]])
        self.assertEqual(answer(test), [1, 3, 6, 10, 15])
        test = Matrix(4, 2, [[2, 5], [3, 1], [5, 3], [10, 1]])
        self.assertEqual(answer(test), [7, 8, 13, 21])


def print_list(lis: List[int]) -> None:
    """ print a list aesthetically """

    for ele in lis:
        print(ele, end=' ')
    print()


def answer(mat: Matrix):
    """ get answer given the arguments """

    mat.process()
    return mat.last()


def main() -> None:
    """ do stuff """

    args = get_args()
    mat = args.mat
    print_list(answer(mat))


if __name__ == '__main__':
    main()
