#!/usr/bin/python3
""" mex and array 1100 """

from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def value(lis):
    """ calculate the value given a subsegment """

    return sum([2 if ele == 0 else 1 for ele in lis])


def answer(n_inp):
    """ calculate the sum of values for all subsegments """

    a_inp = list(map(int, get_input().split()))
    sum_ = 0
    for start in range(n_inp):
        for leng in range(1, n_inp - start + 1):
            sum_ += value(a_inp[start: start + leng])
    return sum_


class Test(TestCase):
    """ test cases """

    def test_case_value_1(self):
        """ test case for value 1 """

        self.assertEqual(value([2, 0]), 3)

    def test_case_value_2(self):
        """ test case for value 2 """

        self.assertEqual(value([2, 0, 1]), 4)

    def test_case_value_3(self):
        """ test case for value 3 """

        self.assertEqual(value([2]), 1)

    def test_case_value_4(self):
        """ test case for value 4 """

        self.assertEqual(value([0, 1]), 3)

    @patch('mex_and_array.get_input', return_value='1 2')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(2), 4)

    @patch('mex_and_array.get_input', return_value='2 0 1')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(3), 14)

    @patch('mex_and_array.get_input', return_value='2 0 5 1')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(4), 26)

    @patch('mex_and_array.get_input', return_value='0 1 1 0 1')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(5), 48)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer(int(input())))


if __name__ == '__main__':
    main()
