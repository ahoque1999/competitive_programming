#!/usr/bin/python3
""" two rabbits 800 """

from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def answer():
    """ return how long for both rabbits to meet """

    a = list(map(int, get_input().split()))
    x = (a[1] - a[0]) / (a[2] + a[3])
    if float(x) != int(x):
        return -1
    return int(x)


class Test(TestCase):
    """ test cases """

    @patch('two_rabbits.get_input', return_value='0 10 2 3')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(), 2)

    @patch('two_rabbits.get_input', return_value='0 10 3 3')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(), -1)

    @patch('two_rabbits.get_input', return_value='900000000 1000000000 1 9999999')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(), 10)

    @patch('two_rabbits.get_input', return_value='1 2 1 1')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(), -1)

    @patch('two_rabbits.get_input', return_value='1 3 1 1')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(), 1)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer())


if __name__ == '__main__':
    main()
