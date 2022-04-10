#!/usr/bin/python3
""" sum of 2050 800 """

from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def answer():
    """ calculate the minimum number of 2050 numbers to represent """

    a_inp = int(get_input())
    quo = a_inp / 2050
    if a_inp % 2050 != 0:
        return -1
    return sum([int(dig) for dig in str(int(quo))])


class Test(TestCase):
    """ test cases """

    @patch('sum_of_2050.get_input', return_value='205')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(), -1)

    @patch('sum_of_2050.get_input', return_value='2050')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(), 1)

    @patch('sum_of_2050.get_input', return_value='4100')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(), 2)

    @patch('sum_of_2050.get_input', return_value='20500')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(), 1)

    @patch('sum_of_2050.get_input', return_value='22550')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(), 2)

    @patch('sum_of_2050.get_input', return_value='25308639900')
    def test_case_6(self, _):
        """ test case 6 """

        self.assertEqual(answer(), 36)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer())


if __name__ == '__main__':
    main()
