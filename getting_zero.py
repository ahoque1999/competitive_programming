#!/usr/bin/python3
""" getting zero 1300 """

from unittest import TestCase
import math


class Test(TestCase):
    """ test cases """

    def test_case_1(self):
        """ test case 1 """

        self.assertEqual(answer(19), 14)

    def test_case_2(self):
        """ test case 2 """

        self.assertEqual(answer(32764), 4)

    def test_case_3(self):
        """ test case 3 """

        self.assertEqual(answer(10240), 4)

    def test_case_4(self):
        """ test case 4 """

        self.assertEqual(answer(49), 15)

    def test_gcd(self):
        """ test gcd function """

        self.assertEqual(gcd(20, 32768), 4)


def gcd(num_1, num_2):
    """ get greatest common divisor """

    while num_2:
        num_1, num_2 = num_2, num_1%num_2
    return num_1


def answer(num_1):
    """ find the minimum number of operations to get a remainder of zero """

    min_ = 15
    for ind in range(15):
        curr = num_1 + ind
        twos = int(math.log(gcd(curr, 32768), 2))
        steps = ind + 15 - twos
        if steps < min_:
            min_ = steps
    return min_


def main() -> None:
    """ do stuff """

    _ = input()
    a_inp = list(map(int, input().split()))
    for a_inp_i in a_inp:
        print(answer(a_inp_i), end=' ')
    print()


if __name__ == '__main__':
    main()
