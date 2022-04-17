#!/usr/bin/python3
""" maximum splitting 1300 """

from unittest import TestCase


class Test(TestCase):
    """ test cases """

    def test_answer(self):
        """ test maximum composite summands """

        self.assertEqual(answer(12), 3)
        self.assertEqual(answer(6), 1)
        self.assertEqual(answer(8), 2)
        self.assertEqual(answer(1), -1)
        self.assertEqual(answer(2), -1)
        self.assertEqual(answer(3), -1)
        self.assertEqual(answer(11), -1)
        self.assertEqual(answer(9), 1)
        self.assertEqual(answer(19), 3)


def even(int_1):
    """ check if even """

    return int_1 % 2 == 0


def div_4(int_1):
    """ check if divisible by 4 and greater than equal 0 """

    return int_1 % 4 == 0 and int_1 >= 0


def answer(int_1):
    """ given a number find the maximum number
    of composite sumamnds """

    counter = 0
    if not even(int_1):
        int_1 -= 9
        counter += 1
    if not div_4(int_1):
        int_1 -= 6
        counter += 1
    if not div_4(int_1):
        return -1
    else:
        return int_1 // 4 + counter


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        print(answer(int(input())))


if __name__ == '__main__':
    main()
