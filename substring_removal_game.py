#!/usr/bin/python3
""" substring removal game 800 """


from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def answer():
    """ calculate optimal number of ones from a string """

    s_inp = get_input()
    list1 = sorted([len(ele) for ele in s_inp.split('0') if ele != ''])[::-1]
    return sum([list1[ind] for ind in range(0, len(list1), 2)])


class Test(TestCase):
    """ test cases """

    @patch('substring_removal_game.get_input', return_value='01111001')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(), 4)

    @patch('substring_removal_game.get_input', return_value='0000')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(), 0)

    @patch('substring_removal_game.get_input', return_value='111111')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(), 6)

    @patch('substring_removal_game.get_input', return_value='101010101')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(), 3)

    @patch('substring_removal_game.get_input', return_value='011011110111')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(), 6)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer())


if __name__ == '__main__':
    main()
