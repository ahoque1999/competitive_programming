#!/usr/bin/python3
""" fun with subarrays 1100 """

from unittest.mock import patch
from unittest import TestCase


def get_input():
    """ safe input """

    return input()


def answer(n_of_a):
    """ return minimum number of operations needed to make list homogenous """

    a_inp = list(map(int, get_input().split()))
    val = a_inp[-1]
    ind = n_of_a-1
    # length of longest contiguous substring
    count = 0
    step = 0
    while ind >= 0:
        while a_inp[ind] == val and ind >= 0:
            count += 1
            ind -= 1
        if ind < 0:
            break
        step += 1
        ind -= count
        count *= 2
    return step


class Test(TestCase):
    """ test cases """

    @patch('fun_with_subarrays.get_input', return_value='1 1 1')
    def test_case_1(self, _):
        """ test case 1 """

        self.assertEqual(answer(3), 0)

    @patch('fun_with_subarrays.get_input', return_value='2 1')
    def test_case_2(self, _):
        """ test case 2 """

        self.assertEqual(answer(2), 1)

    @patch('fun_with_subarrays.get_input', return_value='4 4 4 2 4')
    def test_case_3(self, _):
        """ test case 3 """

        self.assertEqual(answer(5), 1)

    @patch('fun_with_subarrays.get_input', return_value='4 2 1 3')
    def test_case_4(self, _):
        """ test case 4 """

        self.assertEqual(answer(4), 2)

    @patch('fun_with_subarrays.get_input', return_value='1')
    def test_case_5(self, _):
        """ test case 5 """

        self.assertEqual(answer(1), 0)


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer(int(input())))


if __name__ == '__main__':
    main()
