#!/usr/bin/python3
""" vasya and coins 800 """


from unittest.mock import patch
from unittest import TestCase


def answer():
    """ calculate answer """

    a_inp, b_inp = list(map(int, input().split()))
    if a_inp == 0:
        return 1
    return a_inp + b_inp * 2 + 1


class Test(TestCase):
    """ test cases """

    @patch('vasya_and_coins.input', return_value='1 1')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(), 4)

    @patch('vasya_and_coins.input', return_value='4 0')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(), 5)

    @patch('vasya_and_coins.input', return_value='0 2')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(), 1)

    @patch('vasya_and_coins.input', return_value='0 0')
    def test_case_4(self, _):
        """ test case 4"""

        self.assertEqual(answer(), 1)

    @patch('vasya_and_coins.input', return_value='2314 2374')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(), 7063)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer())


if __name__ == '__main__':
    main()
