#!/usr/bin/python3
""" sget an even string 1300 """

from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def answer():
    """ find the minimum number of deletions neeeded to get an even string """

    str_ = get_input()
    n_str = len(str_)
    count_ = 0
    comp = str_[0]
    for ind in range(1, n_str+1):
        try:
            if str_[ind] in comp:
                comp = ''
            elif comp == '':
                comp = str_[ind]
            else:
                comp += str_[ind]
                count_ += 1
        except IndexError:
            if comp != '':
                count_ += 1
    return count_


class Test(TestCase):
    """ test cases """

    @patch('get_an_even_string.get_input', return_value='aabbdabdccc')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(), 3)

    @patch('get_an_even_string.get_input', return_value='zyx')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(), 3)

    @patch('get_an_even_string.get_input', return_value='aaababbb')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(), 2)

    @patch('get_an_even_string.get_input', return_value='aabbcc')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(), 0)

    @patch('get_an_even_string.get_input', return_value='oaoaaaoo')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(), 2)

    @patch('get_an_even_string.get_input', return_value='bmefbmuyw')
    def test_case_6(self, _):
        """ test case 6 """

        self.assertEqual(answer(), 7)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer())


if __name__ == '__main__':
    main()
